import os
from PIL import Image, ImageDraw, ImageFont

def build_banner():
    base_path = 'assets/banner3.png'
    logo_path = 'assets/logo2.png'
    output_path = 'assets/banner3.png'

    print("Opening base banner...")
    im = Image.open(base_path).convert('RGBA')

    # 1. Erase the old "U" logo
    # Coordinates from grid inspector: x: 82 to 235, y: 35 to 220
    draw = ImageDraw.Draw(im)
    draw.rectangle([80, 32, 238, 224], fill=(255, 255, 255, 255))

    # 2. Add the official UCA Logo (logo2.png)
    # Center: cx = 158, cy = 125
    logo = Image.open(logo_path).convert('RGBA')
    target_w = 168
    target_h = int(target_w * (logo.height / logo.width))
    logo_resized = logo.resize((target_w, target_h), Image.Resampling.LANCZOS)

    logo_x = int(158 - target_w / 2)
    logo_y = int(125 - target_h / 2)

    # Paste logo with alpha mask
    im.paste(logo_resized, (logo_x, logo_y), logo_resized)

    # 3. Clean up the 4 Professional Certification Subtitles
    # Font setup
    try:
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
        font_sub_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)
    except:
        font_sub = font_sub_bold = ImageFont.load_default()

    sub_color = (71, 85, 105, 255) # #475569

    # Cleanups
    cleanups = [
        # (x1, y1, x2, y2), line1, line2
        ((94, 534, 240, 578), "GST, Billing, Inventory", "& Real Accounting"),
        ((297, 534, 450, 578), "MS Word, Excel, PPT", "& Professional Suite"),
        ((94, 624, 240, 666), "Formulas, Pivot Table", "& MIS Reports"),
        ((297, 624, 465, 666), "Fundamental Skills,", "Hindi/Eng Typing & PC")
    ]

    for box, l1, l2 in cleanups:
        draw.rectangle(box, fill=(255, 255, 255, 255))
        draw.text((box[0], box[1] + 2), l1, fill=sub_color, font=font_sub_bold)
        draw.text((box[0], box[1] + 19), l2, fill=sub_color, font=font_sub)

    # 4. Update the Address in the Bottom Bar
    # Sample background color in the address area:
    # At (580, 715), color is deep navy: around (7, 23, 62)
    sample_col = im.getpixel((585, 720))
    print("Sampled bottom bar color:", sample_col)

    # Cover the old address text: x: 575 to 945, y: 706 to 758
    # We can create a subtle vertical gradient or solid matching fill
    c1 = (5, 18, 50, 255)
    c2 = (10, 32, 85, 255)
    for y_curr in range(706, 759):
        factor = (y_curr - 706) / (759 - 706)
        r = int(c1[0] * (1 - factor) + c2[0] * factor)
        g = int(c1[1] * (1 - factor) + c2[1] * factor)
        b = int(c1[2] * (1 - factor) + c2[2] * factor)
        draw.line([(575, y_curr), (955, y_curr)], fill=(r, g, b, 255))

    # Draw updated official address text
    try:
        font_addr = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 17)
    except:
        font_addr = ImageFont.load_default()

    addr_color = (255, 255, 255, 255)
    draw.text((580, 710), "Banaras Road, Near Mishra Sweets, RG Tower,", fill=addr_color, font=font_addr)
    draw.text((580, 733), "Ambikapur, Surguja, Chhattisgarh - 497001", fill=addr_color, font=font_addr)

    # Save output as high quality PNG
    im.save(output_path, "PNG", optimize=True)
    print("Banner successfully generated and saved to", output_path)

if __name__ == '__main__':
    build_banner()
