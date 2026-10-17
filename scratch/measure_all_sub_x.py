from PIL import Image

im = Image.open('assets/banner3.png')

# Let's inspect x from 250 to 480 for row 1 (y: 480..555) and row 2 (y: 600..650)
print("Row 1 (Office) subtitle x-bounds:")
for y in range(482, 550, 4):
    dark_xs = [x for x in range(320, 480) if sum(im.getpixel((x, y))[:3]) < 600]
    if dark_xs:
        print(f"y={y}: min_x={min(dark_xs)}, max_x={max(dark_xs)}, count={len(dark_xs)}")

print("\nRow 2 (BCC) subtitle x-bounds:")
for y in range(600, 645, 4):
    dark_xs = [x for x in range(320, 480) if sum(im.getpixel((x, y))[:3]) < 600]
    if dark_xs:
        print(f"y={y}: min_x={min(dark_xs)}, max_x={max(dark_xs)}, count={len(dark_xs)}")

# Let's also check Tally & Excel text starting x:
print("\nTally text starting x:")
for y in range(482, 550, 4):
    dark_xs = [x for x in range(80, 240) if sum(im.getpixel((x, y))[:3]) < 600]
    if dark_xs:
        print(f"y={y}: min_x={min(dark_xs)}, max_x={max(dark_xs)}")
