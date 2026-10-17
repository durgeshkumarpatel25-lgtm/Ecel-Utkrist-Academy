from PIL import Image, ImageDraw, ImageFont

# Check pristine image from git
im = Image.open('assets/banner3.png').convert('RGBA')
draw = ImageDraw.Draw(im)

try:
    font_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 11)
    font_reg = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 10)
except Exception:
    font_bold = font_reg = ImageFont.load_default()

sub_color = (71, 85, 105, 255) # #475569 Slate

# 1. Tally Prime Subtitle (y: 512..555, below Tally Prime title at 482..506)
draw.rectangle([101, 512, 310, 555], fill=(255, 255, 255, 255))
draw.text((104, 515), "GST, E-Way Bill & Inventory", fill=sub_color, font=font_bold)
draw.text((104, 533), "Complete Accounting & Taxation", fill=sub_color, font=font_reg)

# 2. MS Office Subtitle (y: 512..555, below MS Office title at 482..506)
draw.rectangle([404, 512, 620, 555], fill=(255, 255, 255, 255))
draw.text((408, 515), "MS Word, Excel & PowerPoint", fill=sub_color, font=font_bold)
draw.text((408, 533), "Complete Office Productivity Suite", fill=sub_color, font=font_reg)

# 3. Advance Excel Subtitle (y: 596..642, below Advance Excel title at 568..592)
draw.rectangle([101, 596, 310, 642], fill=(255, 255, 255, 255))
draw.text((104, 600), "Formulas, Pivot Table & VLOOKUP", fill=sub_color, font=font_bold)
draw.text((104, 618), "Data Analysis & MIS Reporting", fill=sub_color, font=font_reg)

# 4. Basic Computer Course Subtitle (y: 596..642, below BCC title at 568..592)
draw.rectangle([404, 596, 625, 642], fill=(255, 255, 255, 255))
draw.text((408, 600), "Fundamental Computer Skills & OS", fill=sub_color, font=font_bold)
draw.text((408, 618), "Hindi & English Typing, Internet", fill=sub_color, font=font_reg)

# Let's crop the whole cards region (x: 40..630, y: 440..660) to inspect:
crop = im.crop((40, 440, 630, 660))
crop.save('scratch/test_cards_perfect.png')
print("Saved test_cards_perfect.png")
