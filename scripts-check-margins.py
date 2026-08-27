#!/usr/bin/env python3
"""全スライドの描画範囲を測り、安全域からはみ出したものを報告する。

目視では下端のはみ出しを見落とす。build/png/*.png を1枚ずつ走査し、
白でない画素の最小・最大の x / y を出して安全域と比べる。

    python3 scripts-check-margins.py

安全域は theme/deck.css の section padding（76px 64px 56px）に合わせてある。
除外するもの:
  - 表紙・章扉は全面塗りなので自動で除外する（四辺すべてに達しているもの）
  - box-shadow を持つ枠は左右に6pxほど滲む。欠陥ではない
"""
import subprocess, sys, pathlib

W, H = 1280, 720
LEFT, RIGHT, TOP, BOTTOM = 64, 1216, 40, 664
SHADOW = 8          # box-shadow の滲みとして見逃す幅
# 全面塗り（表紙・章扉）は四辺すべてに達する。番号を書くと枚数が変わるたび腐るので自動判定

def scan(png):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(png), "-f", "rawvideo", "-pix_fmt", "gray", "-"],
        capture_output=True, check=True).stdout
    xs, ys = set(), set()
    for y in range(0, H, 2):
        row = raw[y * W:(y + 1) * W]
        for x in range(W):
            if row[x] < 245:
                xs.add(x); ys.add(y)
    return (min(xs), max(xs), min(ys), max(ys)) if xs else None

def main():
    pngs = sorted(pathlib.Path("build/png").glob("s.0*.png"))
    if not pngs:
        sys.exit("build/png/*.png がない。先に marp でPNGを書き出すこと")
    bad = 0
    for p in pngs:
        box = scan(p)
        if box is None:
            continue
        l, r, t, b = box
        if l == 0 and r >= W - 1 and t == 0 and b >= H - 2:
            print(f"{p.name}  （全面塗り・除外）"); continue
        msgs = []
        if l < LEFT - SHADOW:  msgs.append(f"左が{LEFT-l}px出ている")
        if r > RIGHT + SHADOW: msgs.append(f"右が{r-RIGHT}px出ている")
        if t < TOP:            msgs.append(f"上が{TOP-t}px出ている")
        if b > BOTTOM:         msgs.append(f"下が{b-BOTTOM}px出ている")
        if msgs:
            bad += 1
            print(f"{p.name}  x:{l}-{r} y:{t}-{b}  ← " + "、".join(msgs))
        else:
            print(f"{p.name}  x:{l}-{r} y:{t}-{b}")
    print(f"\nはみ出し {bad} 枚 / {len(pngs)} 枚")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
