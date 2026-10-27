from PIL import Image

def find_colored_regions(img_path, target_rgb, tolerance=30):
    img = Image.open(img_path).convert('RGB')
    w, h = img.size
    points = []
    tr, tg, tb = target_rgb
    for y in range(0, h, 5):
        for x in range(0, w, 5):
            r, g, b = img.getpixel((x, y))
            if abs(r - tr) <= tolerance and abs(g - tg) <= tolerance and abs(b - tb) <= tolerance:
                points.append((x, y))
    if not points:
        return None
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    return (min_x, min_y, max_x, max_y)

print("Finder ready")
