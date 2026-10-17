from PIL import Image

im = Image.open('assets/banner3.png')

# Let's inspect:
# 1. Tally subtitle:
# The icon circle ends around x = 70..80. Let's see:
for x in range(60, 95):
    # find where icon circle ends (white background)
    colors = [im.getpixel((x, y)) for y in range(430, 500)]
    # count non-white
    non_white = [c for c in colors if sum(c[:3]) < 700]
    if len(non_white) == 0:
        print(f"White vertical separator at x={x}")
        break

# Let's find Tally title bottom y and subtitle top y:
print("\nScanning Tally text x=100..220:")
for y in range(420, 560):
    dark_px = [x for x in range(100, 240) if sum(im.getpixel((x, y))[:3]) < 600]
    if dark_px:
        print(f"y={y}: count={len(dark_px)}, min_x={min(dark_px)}, max_x={max(dark_px)}")
