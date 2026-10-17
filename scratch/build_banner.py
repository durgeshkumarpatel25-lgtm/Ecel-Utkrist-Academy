import os
from PIL import Image, ImageDraw, ImageFont

def build_banner():
    base_path = 'assets/banner3.png'
    output_path = 'assets/banner3.png'

    print("Opening base banner...")
    im = Image.open(base_path).convert('RGBA')
    draw = ImageDraw.Draw(im)

    # 1. Cleanly erase the old "U" logo and all floating digital pixel blocks
    # Bounds: x: 75 to 312, y: 14 to 230
    draw.rectangle([75, 14, 312, 230], fill=(255, 255, 255, 255))

    # 2. Add the official UCA Emblem Logo (assets/logo2.png)
    logo_path = 'assets/logo2.png'
    logo = Image.open(logo_path).convert('RGBA')
    
    # Scale logo elegantly to fit the header
    target_w = 190
    target_h = int(target_w * (logo.height / logo.width))
    logo_resized = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)

    # Position logo: x: 98, y: 38
    logo_x = 98
    logo_y = 38
    im.paste(logo_resized, (logo_x, logo_y), logo_resized)

    # 3. Clean up the 4 Professional Certification Subtitles
    # Fonts
    try:
        font_sub_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
        font_sub_reg = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
    except Exception:
        font_sub_bold = font_sub_reg = ImageFont.load_default()

    sub_color = (60, 75, 95, 255) # Slate navy-tinted grey

    # 1) Tally Prime Subtitle (under title at y: 482..506)
    draw.rectangle([101, 510, 310, 555], fill=(255, 255, 255, 255))
    draw.text((104, 513), "GST, E-Way Bill & Inventory", fill=sub_color, font=font_sub_bold)
    draw.text((104, 532), "Complete Accounting & Taxation", fill=sub_color, font=font_sub_reg)

    # 2) MS Office Subtitle (under title at y: 482..506)
    draw.rectangle([404, 510, 620, 555], fill=(255, 255, 255, 255))
    draw.text((408, 513), "MS Word, Excel & PowerPoint", fill=sub_color, font=font_sub_bold)
    draw.text((408, 532), "Complete Office Productivity Suite", fill=sub_color, font=font_sub_reg)

    # 3) Advance Excel Subtitle (under title at y: 568..592)
    draw.rectangle([101, 595, 310, 642], fill=(255, 255, 255, 255))
    draw.text((104, 599), "Formulas, Pivot Table & VLOOKUP", fill=sub_color, font=font_sub_bold)
    draw.text((104, 618), "Data Analysis & MIS Reporting", fill=sub_color, font=font_sub_reg)

    # 4) Basic Computer Course Subtitle (under title at y: 568..592)
    draw.rectangle([404, 595, 625, 642], fill=(255, 255, 255, 255))
    draw.text((408, 599), "Fundamental Computer Skills & OS", fill=sub_color, font=font_sub_bold)
    draw.text((408, 618), "Hindi & English Typing, Internet", fill=sub_color, font=font_sub_reg)

    # 4. Correct the Address in the Bottom Navy Bar
    # Erase old text "Bharas Road..."
    bar_bg = (2, 34, 87, 255)
    draw.rectangle([805, 688, 1310, 746], fill=bar_bg)

    # Draw updated official address
    try:
        font_addr = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 15)
    except Exception:
        font_addr = ImageFont.load_default()

    addr_color = (255, 255, 255, 255)
    draw.text((810, 693), "Banaras Road, Near Mishra Sweets, RG Tower,", fill=addr_color, font=font_addr)
    draw.text((810, 719), "Ambikapur, Surguja, Chhattisgarh - 497001", fill=addr_color, font=font_addr)

    # Save final optimized banner
    im.save(output_path, "PNG", optimize=True)
    print("SUCCESS: banner3.png generated cleanly and saved!")

if __name__ == '__main__':
    build_banner()
