from PIL import Image, ImageDraw, ImageFont
import math

def draw_arrow_pointer(draw, start_xy, end_xy, arrow_color=(225, 29, 72), line_width=4, arrow_size=16):
    """Draws a crisp arrow from start_xy to end_xy pointing at end_xy."""
    x0, y0 = start_xy
    x1, y1 = end_xy
    
    # Draw arrow shaft line
    draw.line([x0, y0, x1, y1], fill=arrow_color, width=line_width)
    
    # Calculate angle for arrow head
    angle = math.atan2(y1 - y0, x1 - x0)
    
    # Left and right points of arrow head
    head_angle = math.pi / 6 # 30 degrees
    left_x = x1 - arrow_size * math.cos(angle - head_angle)
    left_y = y1 - arrow_size * math.sin(angle - head_angle)
    right_x = x1 - arrow_size * math.cos(angle + head_angle)
    right_y = y1 - arrow_size * math.sin(angle + head_angle)
    
    # Draw filled triangle for arrowhead
    draw.polygon([(x1, y1), (left_x, left_y), (right_x, right_y)], fill=arrow_color)

def draw_badge_with_pointer(draw, box, label_text, pointer_from, font, badge_bg=(225, 29, 72), badge_fg=(255, 255, 255)):
    """Draws a highlighted bounding box, an arrow pointing to it, and a text badge."""
    bx1, by1, bx2, by2 = box
    
    # 1. Draw glowing highlight bounding box
    # Outer glow
    for offset in range(3, 0, -1):
        draw.rounded_rectangle([bx1 - offset, by1 - offset, bx2 + offset, by2 + offset], radius=12, outline=(249, 115, 22, 100), width=1)
    # Main border
    draw.rounded_rectangle([bx1, by1, bx2, by2], radius=10, outline=badge_bg, width=4)
    
    # 2. Draw text badge
    # Measure text
    bbox = font.getbbox(label_text)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    px, py = pointer_from
    badge_x1 = px - 12
    badge_y1 = py - 10
    badge_x2 = px + text_w + 16
    badge_y2 = py + text_h + 12
    
    # Badge shadow
    draw.rounded_rectangle([badge_x1 + 3, badge_y1 + 3, badge_x2 + 3, badge_y2 + 3], radius=8, fill=(0, 0, 0, 80))
    # Badge pill
    draw.rounded_rectangle([badge_x1, badge_y1, badge_x2, badge_y2], radius=8, fill=badge_bg, outline=(255, 255, 255), width=2)
    # Badge text
    draw.text((px, py), label_text, font=font, fill=badge_fg)
    
    # 3. Arrow from badge edge to target box edge
    # Target center on closest edge
    target_x = (bx1 + bx2) / 2
    target_y = by1 if py < by1 else by2
    if px < bx1:
        start_x = badge_x2
        start_y = (badge_y1 + badge_y2) / 2
    elif px > bx2:
        start_x = badge_x1
        start_y = (badge_y1 + badge_y2) / 2
    else:
        start_x = (badge_x1 + badge_x2) / 2
        start_y = badge_y2 if py < by1 else badge_y1
        
    draw_arrow_pointer(draw, (start_x, start_y), (target_x, target_y), arrow_color=badge_bg, line_width=4, arrow_size=14)

print("Annotation helper defined successfully.")
