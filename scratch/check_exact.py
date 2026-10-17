from PIL import Image

im = Image.open('assets/banner3.png')
print("Image width:", im.width, "height:", im.height)

# Check location circle center
# Find yellow pixels around x: 700-800, y: 680-740
yellow_pixels = []
for x in range(650, 850):
    for y in range(670, 750):
        r, g, b = im.getpixel((x, y))[:3]
        if r > 220 and g > 150 and b < 50:
            yellow_pixels.append((x, y))

if yellow_pixels:
    xs = [p[0] for p in yellow_pixels]
    ys = [p[1] for p in yellow_pixels]
    print(f"Location circle found: x from {min(xs)} to {max(xs)}, y from {min(ys)} to {max(ys)}")
    print(f"Center: ({sum(xs)//len(xs)}, {sum(ys)//len(ys)})")

# Check address text area
# Sample dark blue background behind address
for x in [820, 900, 1000, 1100]:
    print(f"Color at ({x}, 725):", im.getpixel((x, 725)))

# Check gap between U logo and UTKRIST text
for x in range(260, 360, 5):
    col = [im.getpixel((x, y))[:3] for y in range(60, 160)]
    dark_count = sum(1 for c in col if c[0] < 50 and c[1] < 50 and c[2] > 60)
    print(f'x={x}: dark pixels={dark_count}')

# Check course subtitles exact y
print("Tally text area:")
for y in range(480, 560, 5):
    p = im.getpixel((150, y))
    print(f"y={y}: {p}")

