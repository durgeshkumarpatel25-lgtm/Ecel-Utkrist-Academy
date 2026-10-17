from PIL import Image

tally = Image.open('scratch/crop_tally_text.png')
print("Tally text size:", tally.size)

# Subtitle is between "Tally Prime" title and "Advance Excel" title
# In tally crop coordinates (where y=0 corresponds to full banner y = 340 + 130 = 470):
for y in range(0, tally.height, 2):
    row_px = [x for x in range(70, tally.width) if sum(tally.getpixel((x, y))[:3]) < 600]
    if row_px:
        print(f"crop_y={y} (full_y={470+y}): min_x={min(row_px)+40}, max_x={max(row_px)+40}, count={len(row_px)}")
    else:
        print(f"crop_y={y} (full_y={470+y}): BLANK")
