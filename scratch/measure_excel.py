from PIL import Image

excel = Image.open('scratch/crop_excel_text.png')
# excel crop top is at crop y=220, which is full banner y = 340 + 220 = 560
print("Excel crop analysis:")
for y in range(0, excel.height, 2):
    row_px = [x for x in range(70, excel.width) if sum(excel.getpixel((x, y))[:3]) < 600]
    if row_px:
        print(f"excel_y={y} (full_y={560+y}): min_x={min(row_px)+40}, max_x={max(row_px)+40}, count={len(row_px)}")
    else:
        print(f"excel_y={y} (full_y={560+y}): BLANK")
