from PIL import Image

im = Image.open('scratch/test_banner_out.png')
# Crop y: 420 to 560
crop = im.crop((70, 420, 600, 560))
crop.save('scratch/test_row1_crop.png')
print("Saved test_row1_crop.png")
