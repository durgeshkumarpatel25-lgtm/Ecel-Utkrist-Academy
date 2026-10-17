import os
from PIL import Image, ImageDraw, ImageFont

def build_banner():
    base_path = 'assets/banner3.png'
    output_path = 'assets/banner3.png'

    print("Opening base banner...")
    im = Image.open(base_path).convert('RGBA')
    draw = ImageDraw.Draw(im)

    # 1. Erase the old "U" logo and all blue pixel blocks & yellow dots completely
    # x: 75 to 285, y: 28 to 230
    draw.rectangle([75, 28, 285, 230], fill=(255, 255, 255, 255))

    # 2. Add the official UCA Logo (assets/logo2.png)
    logo_path = 'assets/logo2.png'
    logo = Image.open(logo_path).convert('RGBA')
    
    # Scale logo to fit elegantly in the header
    target_w = 188
    target_h = int(target_w * (logo.height / logo.width))
    logo_resized = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)

    # Position logo: x: 96, y: 36
    logo_x = 96
    logo_y = 36
    im.paste(logo_resized, (logo_x, logo_y), logo_resized)

    # 3. Clean up the 4 Professional Certification Subtitles
    try:
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 11)
        font_sub_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 11)
    except:
        font_sub = font_sub_bold = ImageFont.load_default()

    sub_color = (71, 85, 105, 255) # #475569

    # Exact measured subtitle boxes:
    # Row 1: y: 525 to 572
    # Row 2: y: 615 to 658
    subtitles = [
        ([94, 524, 240, 572], "GST, Billing, Inventory", "& Real Accounting"),
        ([295, 524, 480, 572], "MS Word, Excel, PPT", "& Professional Suite"),
        ([94, 614, 240, 658], "Formulas, Pivot Table", "& MIS Reports"),
        ([295, 614, 480, 658], "Fundamental Skills,", "Hindi/Eng Typing & PC")
    ]

    for box, line1, line2 in subtitles:
        # Wipe old garbled text completely
        draw.rectangle(box, fill=(255, 255, 255, 255))
        draw.text((box[0] + 1, box[1] + 3), line1, fill=sub_color, font=font_sub_bold)
        draw.text((box[0] + 1, box[1] + 20), line2, fill=sub_color, font=font_sub)

    # 4. Correct the Address in the Bottom Bar
    # Address text is at x: 811 to 1299, y: 690 to 737
    # Background color is (2, 34, 87)
    bar_bg = (2, 34, 87, 255)
    draw.rectangle([805, 688, 1310, 746], fill=bar_bg)

    # Draw the exact updated official address
    try:
        font_addr = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 15)
    except:
        font_addr = ImageFont.load_default()

    addr_color = (255, 255, 255, 255)
    draw.text((810, 692), "Banaras Road, Near Mishra Sweets, RG Tower,", fill=addr_color, font=font_addr)
    draw.text((810, 718), "Ambikapur, Surguja, Chhattisgarh - 497001", fill=addr_color, font=font_addr)

    # Save to assets/banner3.png
    im.save(output_path, "PNG", optimize=True)
    print("SUCCESS: banner3.png updated cleanly!")

if __name__ == '__main__':
    build_banner()
