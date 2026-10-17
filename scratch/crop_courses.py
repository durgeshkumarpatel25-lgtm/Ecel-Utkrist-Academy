from PIL import Image

im = Image.open('assets/banner3.png')

# Let's crop x: 50 to 500, y: 350 to 670
crop = im.crop((40, 340, 520, 670))
crop.save('scratch/courses_crop.png')
print("Cropped successfully to scratch/courses_crop.png")
