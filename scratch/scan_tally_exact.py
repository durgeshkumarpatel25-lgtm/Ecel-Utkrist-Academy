from PIL import Image

crop = Image.open('scratch/pristine_tally_crop.png')
# crop y=0 corresponds to full banner y = 410.
print("Scanning pristine_tally_crop.png:")
for y in range(0, crop.height, 2):
    dark = [x for x in range(30, crop.width) if sum(crop.getpixel((x, y))[:3]) < 400]
    print(f"y={y} (full_y={410+y}): count={len(dark)}")
