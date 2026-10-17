from PIL import Image

im = Image.open('assets/banner3.png')

# 1. Tally subtitle:
# x: between icon circle right edge (x=103) and divider line (x=315)
# y: between Tally Prime title (y=470) and Advance Excel title (y=565)
tally_sub = [(x, y) for y in range(470, 565) for x in range(103, 315) if sum(im.getpixel((x, y))[:3]) < 600]
print("Tally sub bounds: min_x=", min(p[0] for p in tally_sub), "max_x=", max(p[0] for p in tally_sub), "min_y=", min(p[1] for p in tally_sub), "max_y=", max(p[1] for p in tally_sub))

# 2. Advance Excel subtitle:
# x: between icon circle right edge (x=103) and divider line (x=315)
# y: between Advance Excel title (y=592) and bottom swoosh (y=650)
excel_sub = [(x, y) for y in range(592, 655) for x in range(103, 315) if sum(im.getpixel((x, y))[:3]) < 600]
print("Excel sub bounds: min_x=", min(p[0] for p in excel_sub), "max_x=", max(p[0] for p in excel_sub), "min_y=", min(p[1] for p in excel_sub), "max_y=", max(p[1] for p in excel_sub))

# 3. MS Office subtitle:
# x: between icon circle right edge (x=398) and right edge of text (search x: 398..600)
# y: between MS Office title (y=470) and Basic Computer title (y=565)
office_sub = [(x, y) for y in range(470, 565) for x in range(398, 620) if sum(im.getpixel((x, y))[:3]) < 600]
print("Office sub bounds: min_x=", min(p[0] for p in office_sub), "max_x=", max(p[0] for p in office_sub), "min_y=", min(p[1] for p in office_sub), "max_y=", max(p[1] for p in office_sub))

# 4. Basic Computer Course subtitle:
# x: between icon circle right edge (x=398) and right edge of text
# y: between BCC title (y=592) and bottom swoosh (y=650)
bcc_sub = [(x, y) for y in range(592, 655) for x in range(398, 620) if sum(im.getpixel((x, y))[:3]) < 600]
print("BCC sub bounds: min_x=", min(p[0] for p in bcc_sub), "max_x=", max(p[0] for p in bcc_sub), "min_y=", min(p[1] for p in bcc_sub), "max_y=", max(p[1] for p in bcc_sub))
