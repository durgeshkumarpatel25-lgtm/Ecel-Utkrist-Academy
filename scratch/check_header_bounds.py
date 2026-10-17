from PIL import Image

im = Image.open('assets/banner3.png')

# Header area:
# Blue corner on left ends around x=75.
# Let's find all non-white pixels in x: 70..335, y: 15..245
u_logo_px = [(x, y) for y in range(15, 245) for x in range(70, 335) if sum(im.getpixel((x, y))[:3]) < 720]
print("Old U logo non-white bounds:", min(p[0] for p in u_logo_px), min(p[1] for p in u_logo_px), max(p[0] for p in u_logo_px), max(p[1] for p in u_logo_px))

# Where does UTKRIST text start?
utkrist_px = [(x, y) for y in range(15, 160) for x in range(320, 400) if sum(im.getpixel((x, y))[:3]) < 400]
print("UTKRIST text min x:", min(p[0] for p in utkrist_px))

# Where does DIPLOMA COURSES pill start?
diploma_px = [(x, y) for y in range(235, 280) for x in range(70, 300) if im.getpixel((x, y))[2] > 70 and im.getpixel((x, y))[0] < 50]
print("DIPLOMA COURSES pill min y:", min(p[1] for p in diploma_px))
