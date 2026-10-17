from PIL import Image

im = Image.open('assets/banner3.png')
print("Original banner pixel at (210, 42):", im.getpixel((210, 42)))
print("Original banner pixel at (210, 84):", im.getpixel((210, 84)))

logo = Image.open('assets/logo2.png')
print("Logo size:", logo.size)
