from PIL import Image

im = Image.open('assets/banner3.png')
crop = im.crop((700, 660, 1350, 760))
crop.save('scratch/address_crop.png')
print("Saved address_crop.png")
