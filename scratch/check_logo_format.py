from PIL import Image

logo = Image.open('assets/logo2.png')
print("Logo mode:", logo.mode, "size:", logo.size)
print("Top-left pixel (0,0):", logo.getpixel((0,0)))
print("Pixel at (10, 10):", logo.getpixel((10,10)))
