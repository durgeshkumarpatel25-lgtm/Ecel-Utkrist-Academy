from PIL import Image

crop = Image.open('scratch/courses_crop.png')
print("Crop size:", crop.size) # should be 480 x 330

# In crop coordinates:
# Tally subtitle:
# Below "Tally Prime" title.
# Let's crop just the Tally block in crop coordinates:
tally_crop = crop.crop((50, 60, 240, 160))
tally_crop.save('scratch/crop_tally.png')

# Office crop:
office_crop = crop.crop((240, 60, 470, 160))
office_crop.save('scratch/crop_office.png')

# Excel crop:
excel_crop = crop.crop((50, 160, 240, 280))
excel_crop.save('scratch/crop_excel.png')

# BCC crop:
bcc_crop = crop.crop((240, 160, 470, 280))
bcc_crop.save('scratch/crop_bcc.png')

print("Saved sub crops successfully.")
