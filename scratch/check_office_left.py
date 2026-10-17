from PIL import Image

im = Image.open('scratch/crop_office_text.png')
# This was crop.crop((240, 130, 480, 240)) from courses_crop.png
# courses_crop.png x=0 is full banner x=40.
# So crop_office_text.png x=0 is full banner x = 40 + 240 = 280!
print("crop_office_text left edge is x=280")
for x in range(0, 30):
    c = im.getpixel((x, 30))
    print(f"office_crop x={x} (full x={280+x}): {c}")
