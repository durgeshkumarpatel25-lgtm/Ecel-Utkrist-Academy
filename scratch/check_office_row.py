from PIL import Image

im = Image.open('assets/banner3.png')

# Let's inspect x from 320 to 390 at y=450 (middle of MS Office icon and title)
print("MS Office row at y=450:")
for x in range(320, 420, 4):
    p = im.getpixel((x, 450))
    print(f"x={x}: {p}")

print("\nMS Office subtitle row at y=500:")
for x in range(320, 420, 4):
    p = im.getpixel((x, 500))
    print(f"x={x}: {p}")
