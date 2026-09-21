#!/usr/bin/env python3
"""スクリーンショットの指定範囲を塗りつぶしてから、スライド用に保存する。

投影・配布に載せる前に、パス、アカウント名、プロジェクト名、トークン数以外の数値など
見せる必要のない情報を必ず消す。元画像は assets/shots/raw/ に置き、git には載せない。

    python3 scripts-blur.py assets/shots/raw/context.png assets/shots/context.png \
        --box 120,80,600,40 --box 120,300,900,32

--box は x,y,w,h（元画像のピクセル）。複数指定できる。
ぼかしやモザイクは、文字なら復元される手法が知られているため使わない。
指定範囲は不透明の灰色で完全に塗りつぶす（見た目の「ぼかし」より秘匿を優先）。
範囲が画像の外に出ている、幅や高さが0のときは、無加工のまま成功にならないよう終了コード1で止める。
"""
import argparse, json, pathlib, subprocess, sys

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("dst")
ap.add_argument("--box", action="append", default=[], help="x,y,w,h")
a = ap.parse_args()

if not a.box:
    sys.exit("--box を1つ以上指定すること（塗る範囲がない画像なら、このスクリプトは不要）")

try:
    probe = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
         "-of", "json", a.src], capture_output=True, text=True, check=True)
    st = json.loads(probe.stdout)["streams"][0]
    W, H = int(st["width"]), int(st["height"])
except subprocess.CalledProcessError as e:
    sys.exit(f"ffprobe が失敗した（{a.src} を画像として読めない）: {e.stderr.strip()}")
except (ValueError, KeyError, IndexError):
    sys.exit(f"{a.src} の寸法を取得できない（画像ストリームがない）")
if W <= 0 or H <= 0:
    sys.exit(f"{a.src} を画像として読めない（寸法 {W}x{H}）")

boxes = []
for b in a.box:
    try:
        x, y, w, h = (int(v) for v in b.split(","))
    except ValueError:
        sys.exit(f"--box の形式が違う: {b}（x,y,w,h の整数4つ）")
    if w <= 0 or h <= 0:
        sys.exit(f"--box {b}: 幅と高さは1以上にする")
    if x < 0 or y < 0 or x + w > W or y + h > H:
        sys.exit(f"--box {b}: 画像（{W}x{H}）の外に出ている。範囲を画像内に収める")
    boxes.append((x, y, w, h))

vf = ",".join(f"drawbox=x={x}:y={y}:w={w}:h={h}:color=gray@1.0:t=fill" for x, y, w, h in boxes)
pathlib.Path(a.dst).parent.mkdir(parents=True, exist_ok=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.src, "-vf", vf, a.dst], check=True)
print(f"{a.dst} に保存（{len(boxes)}箇所を塗りつぶし）。投影前に拡大して、伏せ忘れがないことを目視で確認する")
