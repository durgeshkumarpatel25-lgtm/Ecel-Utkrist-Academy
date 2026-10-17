from PIL import Image

im = Image.open('assets/banner3.png')
crop = im.crop((70, 400, 600, 650))
crop.save('scratch/pristine_cards.png')
print("Saved pristine_cards.png")
