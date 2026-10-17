from PIL import Image

im = Image.open('assets/banner3.png')

# Tally text box
# Search for dark pixels in x: 80 to 300, y: 500 to 570
tally_px = [(x, y) for y in range(500, 570) for x in range(80, 240) if sum(im.getpixel((x, y))[:3]) < 500]
print("Tally sub bounds:", min(p[0] for p in tally_px), min(p[1] for p in tally_px), max(p[0] for p in tally_px), max(p[1] for p in tally_px))

# Office text box: search x: 280 to 480, y: 500 to 570
office_px = [(x, y) for y in range(500, 570) for x in range(290, 480) if sum(im.getpixel((x, y))[:3]) < 500]
print("Office sub bounds:", min(p[0] for p in office_px), min(p[1] for p in office_px), max(p[0] for p in office_px), max(p[1] for p in office_px))

# Excel text box: search x: 80 to 240, y: 590 to 655
excel_px = [(x, y) for y in range(590, 655) for x in range(80, 240) if sum(im.getpixel((x, y))[:3]) < 500]
print("Excel sub bounds:", min(p[0] for p in excel_px), min(p[1] for p in excel_px), max(p[0] for p in excel_px), max(p[1] for p in excel_px))

# BCC text box: search x: 290 to 480, y: 590 to 655
bcc_px = [(x, y) for y in range(590, 655) for x in range(290, 480) if sum(im.getpixel((x, y))[:3]) < 500]
print("BCC sub bounds:", min(p[0] for p in bcc_px), min(p[1] for p in bcc_px), max(p[0] for p in bcc_px), max(p[1] for p in bcc_px))
