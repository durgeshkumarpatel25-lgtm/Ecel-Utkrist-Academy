from PIL import Image

crop = Image.open('scratch/row1_crop.png')

# In crop y (where full_y = 460 + crop_y):
# Check for Tally (x=30..150):
print("Scanning Tally y:")
for y in range(0, crop.height, 2):
    dark = [x for x in range(30, 180) if sum(crop.getpixel((x, y))[:3]) < 600]
    print(f"crop_y={y} (full_y={460+y}): count={len(dark)}")
