from PIL import Image

# Check pristine image from git
im = Image.open('scratch/pristine_cards.png') # pristine crop y: 400..650
# Let's crop just the area around Tally Prime title:
crop = im.crop((10, 10, 250, 150)) # y: 410..550
crop.save('scratch/pristine_tally_crop.png')
print("Saved pristine_tally_crop.png")
