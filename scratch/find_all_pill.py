from PIL import Image

im = Image.open('assets/banner3.png')
print("Image size:", im.size)

# Find all occurrences of blue pill color
pill_px = [(x, y) for y in range(200, 600) for x in range(40, 500) if im.getpixel((x, y))[0] < 50 and im.getpixel((x, y))[1] < 80 and im.getpixel((x, y))[2] > 80]
print("Full Pill bounds:", min(p[0] for p in pill_px), min(p[1] for p in pill_px), max(p[0] for p in pill_px), max(p[1] for p in pill_px))
