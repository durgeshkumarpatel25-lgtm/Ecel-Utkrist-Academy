from PIL import Image

im = Image.open('assets/banner3.png')

print("Analyzing Tally area (x: 50..250, y: 440..580)...")
for y in range(440, 580, 5):
    dark_xs = [x for x in range(50, 250) if sum(im.getpixel((x, y))[:3]) < 500]
    if dark_xs:
        print(f"y={y}: min_x={min(dark_xs)}, max_x={max(dark_xs)}, count={len(dark_xs)}")
