from PIL import Image

crop = Image.open('scratch/courses_crop.png')
# search across x=200..300, y=100..200 for grey vertical line
for x in range(200, 300):
    greys = [y for y in range(80, 250) if 100 < crop.getpixel((x, y))[0] < 220 and abs(crop.getpixel((x, y))[0] - crop.getpixel((x, y))[1]) < 10]
    if len(greys) > 50:
        print(f"Found grey line at crop x={x} (full banner x={x+40}), count={len(greys)}")
