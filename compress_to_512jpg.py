#!/usr/bin/env python3
# 生成済みPNG/画像を 512x512 JPEG(品質90) に一括変換して images/ に出力する保険スクリプト。
# 使い方:  python compress_to_512jpg.py <入力フォルダ> [出力フォルダ]
#   既定の出力は ./images
# 依存:  pip install pillow
import sys, os, glob
from PIL import Image

src = sys.argv[1] if len(sys.argv) > 1 else "."
dst = sys.argv[2] if len(sys.argv) > 2 else "images"
os.makedirs(dst, exist_ok=True)

exts = ("*.png","*.PNG","*.jpg","*.jpeg","*.webp")
files = []
for e in exts:
    files += glob.glob(os.path.join(src, e))

count = 0
for f in sorted(files):
    name = os.path.splitext(os.path.basename(f))[0]
    out = os.path.join(dst, name + ".jpg")
    try:
        im = Image.open(f).convert("RGB")
        # 中央クロップして正方形→512にリサイズ
        w, h = im.size
        s = min(w, h)
        im = im.crop(((w-s)//2, (h-s)//2, (w-s)//2+s, (h-s)//2+s))
        im = im.resize((512, 512), Image.LANCZOS)
        im.save(out, "JPEG", quality=90, optimize=True)
        count += 1
    except Exception as ex:
        print("skip", f, ex)
print(f"done: {count} images -> {dst}")
