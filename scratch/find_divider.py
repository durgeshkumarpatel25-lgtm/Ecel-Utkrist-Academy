from PIL import Image

im = Image.open('assets/banner3.png')

# Divider line is between x=240 and 280, y=430..650
for x in range(240, 280):
    dark_y = [y for y in range(430, 650) if sum(im.getpixel((x, y))[:3]) < 600]
    if len(dark_y) > 100:
        print(f"Divider line at x={x}, count={len(dark_y)}")
