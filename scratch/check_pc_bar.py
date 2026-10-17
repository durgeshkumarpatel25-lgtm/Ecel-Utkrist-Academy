from PIL import Image

im = Image.open('assets/banner3.png')

# Let's find the blue banner of "PROFESSIONAL CERTIFICATIONS":
for y in range(300, 420, 5):
    # check color in center x=200
    p = im.getpixel((200, y))
    print(f"y={y}: color={p}")
