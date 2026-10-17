import os
from PIL import Image, ImageDraw, ImageFont

# Load pristine original banner3.png
im = Image.open('assets/banner3.png').convert('RGBA')
draw = ImageDraw.Draw(im)

# 1. Erase old "U" logo
# Coordinates: x: 75 to 290, y: 25 to 235
draw.rectangle([75, 25, 290, 235], fill=(255, 255, 255, 255))

# Paste UCA Logo
logo = Image.open('assets/logo2.png').convert('RGBA')
target_w = 195
target_h = int(target_w * (logo.height / logo.width))
logo_resized = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)
im.paste(logo_resized, (98, 42), logo_resized)

# 2. Subtitles:
# Fonts
font_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13)
font_reg = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
text_color = (55, 65, 81, 255) # Slate-700 for clear, elegant contrast

# Tally: erase [101, 478, 310, 556]
draw.rectangle([101, 478, 310, 556], fill=(255, 255, 255, 255))
draw.text((104, 485), "GST, E-Way Bill & Inventory", fill=text_color, font=font_bold)
draw.text((104, 512), "Complete Accounting & Taxation", fill=text_color, font=font_reg)

# Advance Excel: erase [101, 592, 310, 646]
draw.rectangle([101, 592, 310, 646], fill=(255, 255, 255, 255))
draw.text((104, 598), "Formulas, Pivot Table & VLOOKUP", fill=text_color, font=font_bold)
draw.text((104, 622), "Data Analysis & MIS Reporting", fill=text_color, font=font_reg)

# MS Office: erase [404, 478, 620, 554]
draw.rectangle([404, 478, 620, 554], fill=(255, 255, 255, 255))
draw.text((408, 485), "MS Word, Excel & PowerPoint", fill=text_color, font=font_bold)
draw.text((408, 512), "Complete Office Productivity Suite", fill=text_color, font=font_reg)

# BCC: erase [404, 590, 625, 656]
draw.rectangle([404, 590, 625, 656], fill=(255, 255, 255, 255))
draw.text((408, 598), "Fundamental Computer Skills & OS", fill=text_color, font=font_bold)
draw.text((408, 622), "Hindi & English Typing, Internet", fill=text_color, font=font_reg)

# 3. Address in Bottom Bar
bar_bg = (2, 34, 87, 255)
draw.rectangle([805, 688, 1310, 746], fill=bar_bg)

font_addr = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 15)
draw.text((810, 692), "Banaras Road, Near Mishra Sweets, RG Tower,", fill=(255, 255, 255, 255), font=font_addr)
draw.text((810, 718), "Ambikapur, Surguja, Chhattisgarh - 497001", fill=(255, 255, 255, 255), font=font_addr)

# Save test banner
im.save('scratch/test_banner_out.png', 'PNG', optimize=True)
print("Saved to scratch/test_banner_out.png")
