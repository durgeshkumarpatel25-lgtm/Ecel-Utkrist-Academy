from PIL import Image

im = Image.open('assets/banner3.png')
crop = im.crop((60, 0, 360, 260))
crop.save('scratch/header_crop.png')
print("Saved header_crop.png")
