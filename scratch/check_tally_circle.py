from PIL import Image

im = Image.open('assets/banner3.png')

# Let's inspect x from 70 to 125 at y=500 (middle of Tally subtitle row 1):
print("Pixel colors across x=75..120 at y=500:")
for x in range(75, 120, 2):
    p = im.getpixel((x, 500))
    print(f"x={x}: {p}")
