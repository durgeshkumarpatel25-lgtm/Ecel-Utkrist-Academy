from PIL import Image

crop = Image.open('scratch/courses_crop.png')

# Tally: let's crop y from 130 to 230
tally_crop = crop.crop((0, 130, 240, 240))
tally_crop.save('scratch/crop_tally_text.png')

# Excel: crop y from 220 to 320
excel_crop = crop.crop((0, 220, 240, 325))
excel_crop.save('scratch/crop_excel_text.png')

# Office: crop y from 130 to 240
office_crop = crop.crop((240, 130, 480, 240))
office_crop.save('scratch/crop_office_text.png')

# BCC: crop y from 220 to 320
bcc_crop = crop.crop((240, 220, 480, 325))
bcc_crop.save('scratch/crop_bcc_text.png')

print("Saved detailed text crops.")
