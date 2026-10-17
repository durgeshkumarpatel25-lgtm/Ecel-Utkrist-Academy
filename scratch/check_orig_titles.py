from PIL import Image

# Let's restore from git original f8cd3d2 to inspect the pristine image:
im = Image.open('assets/banner3.png')

# Let's crop x: 70..600, y: 400..500 from the original image:
crop = im.crop((70, 400, 600, 500))
crop.save('scratch/titles_crop_orig.png')
print("Saved titles_crop_orig.png")
