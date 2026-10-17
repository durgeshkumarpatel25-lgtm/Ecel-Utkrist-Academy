import os
from PIL import Image, ImageDraw, ImageFont

# Let's test typography rendering
test_im = Image.new('RGBA', (600, 300), (255, 255, 255, 255))
draw = ImageDraw.Draw(test_im)

fonts = [
    ("Segoe UI", "C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/segoeui.ttf"),
    ("Arial", "C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arial.ttf"),
    ("Calibri", "C:/Windows/Fonts/calibrib.ttf", "C:/Windows/Fonts/calibri.ttf"),
]

for name, bold_path, reg_path in fonts:
    print(f"Testing font: {name}")
    try:
        fb = ImageFont.truetype(bold_path, 13)
        fr = ImageFont.truetype(reg_path, 12)
        print(f"  Loaded successfully!")
    except Exception as e:
        print(f"  Failed: {e}")
