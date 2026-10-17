from PIL import Image

crop = Image.open('scratch/pristine_tally_crop.png')
# Let's inspect the colors across x at y=50 (full_y=460):
for x in range(0, crop.width, 10):
    print(f"x={x}: {crop.getpixel((x, 50))}")
