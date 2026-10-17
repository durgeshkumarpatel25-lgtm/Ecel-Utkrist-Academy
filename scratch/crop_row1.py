from PIL import Image

im = Image.open('assets/banner3.png')

# Let's crop y: 460 to 560, x: 70 to 600
crop = im.crop((70, 460, 600, 560))
crop.save('scratch/row1_crop.png')
print("Saved row1_crop.png")
