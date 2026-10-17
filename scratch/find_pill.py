from PIL import Image

im = Image.open('assets/banner3.png')

for y in range(340, 420):
    for x in range(40, 100):
        c = im.getpixel((x, y))
        # Blue pill color is dark navy/blue
        if c[0] < 50 and c[1] < 80 and c[2] > 80:
            print(f"Found blue pill at x={x}, y={y}, color={c}")
            break
    else:
        continue
    break

# Let's find full bounding box of the blue pill:
pill_px = [(x, y) for y in range(340, 420) for x in range(40, 500) if im.getpixel((x, y))[0] < 50 and im.getpixel((x, y))[1] < 80 and im.getpixel((x, y))[2] > 80]
if pill_px:
    print(f"Pill bounds: min_x={min(p[0] for p in pill_px)}, min_y={min(p[1] for p in pill_px)}, max_x={max(p[0] for p in pill_px)}, max_y={max(p[1] for p in pill_px)}")
