from PIL import Image

crop = Image.open('scratch/pristine_cards.png')
# pristine_cards top is at y=400.
# Let's inspect where "Tally Prime" title is:
for y in range(0, crop.height, 5):
    dark = [x for x in range(30, 180) if sum(crop.getpixel((x, y))[:3]) < 400]
    if dark:
        print(f"crop_y={y} (full_y={400+y}): count={len(dark)}, min_x={min(dark)+70}, max_x={max(dark)+70}")
