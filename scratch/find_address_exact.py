from PIL import Image

im = Image.open('assets/banner3.png')

# Find white text pixels in y: 690 to 760, x: 500 to 1350
white_pixels = []
for y in range(680, 760):
    for x in range(500, 1350):
        r, g, b = im.getpixel((x, y))[:3]
        if r > 200 and g > 200 and b > 200:
            white_pixels.append((x, y))

# Group pixels into columns
by_x = {}
for x, y in white_pixels:
    by_x[x] = by_x.get(x, 0) + 1

# Print x intervals
active_xs = sorted(by_x.keys())
print(f"Total white pixels in bottom bar: {len(white_pixels)}")
print(f"Min X: {min(active_xs)}, Max X: {max(active_xs)}")

# Find gaps > 20px
addr_ys = [y for x, y in white_pixels if x >= 811]
print(f"Address Y range: {min(addr_ys)} to {max(addr_ys)}")

# Check course subtitles exact bounds
for name, rx in [("Tally", (100, 260)), ("Office", (300, 480))]:
    sub_px = [(x, y) for y in range(500, 560) for x in range(rx[0], rx[1]) if im.getpixel((x, y))[0] < 80]
    if sub_px:
        print(f"{name} subtitle: X from {min(p[0] for p in sub_px)} to {max(p[0] for p in sub_px)}, Y from {min(p[1] for p in sub_px)} to {max(p[1] for p in sub_px)}")

for name, rx in [("Excel", (100, 260)), ("BCC", (300, 480))]:
    sub_px = [(x, y) for y in range(590, 650) for x in range(rx[0], rx[1]) if im.getpixel((x, y))[0] < 80]
    if sub_px:
        print(f"{name} subtitle: X from {min(p[0] for p in sub_px)} to {max(p[0] for p in sub_px)}, Y from {min(p[1] for p in sub_px)} to {max(p[1] for p in sub_px)}")

