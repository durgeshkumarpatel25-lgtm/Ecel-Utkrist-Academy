from PIL import Image

im = Image.open('assets/banner3.png')

# Let's inspect where "Tally Prime" title starts (y: 430..465)
title_xs = []
for y in range(430, 465):
    dark = [x for x in range(100, 140) if sum(im.getpixel((x, y))[:3]) < 400]
    if dark:
        title_xs.append(min(dark))

print("Tally Prime title starts at x =", min(title_xs))

# Check Excel title starting x:
excel_title_xs = []
for y in range(565, 595):
    dark = [x for x in range(100, 140) if sum(im.getpixel((x, y))[:3]) < 400]
    if dark:
        excel_title_xs.append(min(dark))

print("Excel title starts at x =", min(excel_title_xs))

# Check Office title starting x:
office_title_xs = []
for y in range(430, 465):
    dark = [x for x in range(315, 360) if sum(im.getpixel((x, y))[:3]) < 400]
    if dark:
        office_title_xs.append(min(dark))

print("Office title starts at x =", min(office_title_xs))

# Check BCC title starting x:
bcc_title_xs = []
for y in range(565, 595):
    dark = [x for x in range(315, 360) if sum(im.getpixel((x, y))[:3]) < 400]
    if dark:
        bcc_title_xs.append(min(dark))

print("BCC title starts at x =", min(bcc_title_xs))
