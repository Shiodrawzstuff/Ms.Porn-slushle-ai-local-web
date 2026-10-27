from PIL import Image, ImageDraw, ImageFont
import math
from annotate_helper import draw_badge_with_pointer

font_bold = ImageFont.truetype('arialbd.ttf', 16)
font_regular = ImageFont.truetype('arial.ttf', 14)

# -------------------------------------------------------------
# 1. GUIDE 1: HERO & NAVIGATION (guide_1_hero.png)
# -------------------------------------------------------------
im_hero = Image.open('shot_home.png').convert('RGB')
draw_hero = ImageDraw.Draw(im_hero)

draw_badge_with_pointer(
    draw_hero,
    box=(950, 48, 1200, 105),
    label_text='👉 [1] CLICK HERE: Quick Call Hotline or Jump to Delivery',
    pointer_from=(600, 48),
    font=font_bold,
    badge_bg=(225, 29, 72) # Red
)

draw_badge_with_pointer(
    draw_hero,
    box=(75, 545, 335, 605),
    label_text='👉 [2] CLICK HERE: Check Your 20km Delivery Eligibility',
    pointer_from=(75, 660),
    font=font_bold,
    badge_bg=(234, 88, 12) # Orange
)

draw_badge_with_pointer(
    draw_hero,
    box=(350, 545, 580, 605),
    label_text='👉 [3] CLICK HERE: Dial 086-557-8822 Instantly',
    pointer_from=(420, 660),
    font=font_bold,
    badge_bg=(5, 150, 105) # Green
)

draw_badge_with_pointer(
    draw_hero,
    box=(740, 185, 1195, 750),
    label_text='⭐ MAIN PRODUCE: Signature Orange Slushie (100% Citrus)',
    pointer_from=(680, 140),
    font=font_bold,
    badge_bg=(217, 119, 6) # Amber
)
im_hero.save('guide_1_hero.png')
print('guide_1_hero.png done')

# -------------------------------------------------------------
# 2. GUIDE 2: FLAVORS MENU (guide_2_flavors.png)
# -------------------------------------------------------------
im_flavors = Image.open('shot_flavors.png').convert('RGB')
draw_flavors = ImageDraw.Draw(im_flavors)

# Highlight Card 1: Orange Slushie (Main Produce)
draw_badge_with_pointer(
    draw_flavors,
    box=(75, 180, 345, 620),
    label_text='👑 #1 MAIN PRODUCE: Signature Fresh Orange Slushie',
    pointer_from=(75, 130),
    font=font_bold,
    badge_bg=(234, 88, 12) # Orange
)

# Arrow to "Order This" button on Card 1
draw_badge_with_pointer(
    draw_flavors,
    box=(230, 560, 330, 605),
    label_text='👉 CLICK "Order This": Auto-fills flavor into order form below!',
    pointer_from=(120, 660),
    font=font_bold,
    badge_bg=(225, 29, 72) # Red
)

# Highlight other flavors (Strawberry, Thai Tea, Green Tea)
draw_badge_with_pointer(
    draw_flavors,
    box=(365, 180, 1205, 620),
    label_text='✨ FULL LINEUP: Strawberry, Thai Tea, Green Tea, Cola, Coco Milk & Coconut Water',
    pointer_from=(450, 130),
    font=font_bold,
    badge_bg=(5, 150, 105) # Emerald
)
im_flavors.save('guide_2_flavors.png')
print('guide_2_flavors.png done')

# -------------------------------------------------------------
# 3. GUIDE 3: 20KM DELIVERY CHECKER (guide_3_delivery.png)
# -------------------------------------------------------------
im_deliv = Image.open('shot_delivery.png').convert('RGB')
draw_deliv = ImageDraw.Draw(im_deliv)

# Landmark chips
draw_badge_with_pointer(
    draw_deliv,
    box=(75, 270, 720, 390),
    label_text='👉 [STEP 1] CLICK ANY BURIRAM LANDMARK (Chang Arena, Clock Tower, etc.)',
    pointer_from=(75, 210),
    font=font_bold,
    badge_bg=(225, 29, 72) # Red
)

# Custom Location / km input
draw_badge_with_pointer(
    draw_deliv,
    box=(75, 410, 720, 485),
    label_text='👉 [STEP 2] OR TYPE YOUR ROAD / DISTANCE IN KM & CLICK "Check Area"',
    pointer_from=(75, 510),
    font=font_bold,
    badge_bg=(234, 88, 12) # Orange
)

# Instant Result Message Box
draw_badge_with_pointer(
    draw_deliv,
    box=(75, 500, 720, 590),
    label_text='⚡ [STEP 3] INSTANT CONFIRMATION: Shows if within 20km with Zero-Melt Guarantee',
    pointer_from=(75, 620),
    font=font_bold,
    badge_bg=(5, 150, 105) # Green
)

# How delivery works card
draw_badge_with_pointer(
    draw_deliv,
    box=(750, 175, 1205, 530),
    label_text='📦 DELIVERY GUIDELINES: Thermal insulated bags & direct dispatch',
    pointer_from=(750, 120),
    font=font_bold,
    badge_bg=(30, 64, 175) # Blue
)
im_deliv.save('guide_3_delivery.png')
print('guide_3_delivery.png done')

# -------------------------------------------------------------
# 4. GUIDE 4: WHERE WE ARE & MAP (guide_4_location.png)
# -------------------------------------------------------------
im_loc = Image.open('shot_location.png').convert('RGB')
draw_loc = ImageDraw.Draw(im_loc)

# Open in Google Maps button
draw_badge_with_pointer(
    draw_loc,
    box=(75, 590, 495, 650),
    label_text='👉 CLICK HERE: Open Google Maps for Turn-by-Turn GPS Directions',
    pointer_from=(75, 680),
    font=font_bold,
    badge_bg=(28, 25, 23) # Dark
)

# Shop details (Buriram, hours, phone)
draw_badge_with_pointer(
    draw_loc,
    box=(75, 180, 495, 560),
    label_text='📍 SHOP DETAILS: Buriram shop & factory, open daily 09:00 - 18:30',
    pointer_from=(75, 130),
    font=font_bold,
    badge_bg=(234, 88, 12) # Orange
)

# 20km Radius Map Preview
draw_badge_with_pointer(
    draw_loc,
    box=(525, 180, 1205, 650),
    label_text='⭕ BURIRAM MAP PREVIEW: Visual 20km delivery boundary circle',
    pointer_from=(600, 130),
    font=font_bold,
    badge_bg=(5, 150, 105) # Green
)
im_loc.save('guide_4_location.png')
print('guide_4_location.png done')

# -------------------------------------------------------------
# 5. GUIDE 5: WHERE TO CONTACT & QUICK ORDER (guide_5_contact.png)
# -------------------------------------------------------------
im_contact = Image.open('shot_contact.png').convert('RGB')
draw_contact = ImageDraw.Draw(im_contact)

# Big Call Hotline Button
draw_badge_with_pointer(
    draw_contact,
    box=(170, 520, 570, 595),
    label_text='👉 [1] CLICK HERE: One-Tap Phone Call to 086-557-8822',
    pointer_from=(170, 620),
    font=font_bold,
    badge_bg=(225, 29, 72) # Red
)

# Copy Phone Number Button
draw_badge_with_pointer(
    draw_contact,
    box=(170, 605, 570, 660),
    label_text='👉 [2] CLICK HERE: Copy Phone Number to clipboard for Line/WhatsApp',
    pointer_from=(170, 690),
    font=font_bold,
    badge_bg=(75, 85, 99) # Slate
)

# Quick Order Form & Submit Button
draw_badge_with_pointer(
    draw_contact,
    box=(610, 230, 1110, 660),
    label_text='👉 [3] FILL & SUBMIT: Choose flavor, Buriram address & prepare order!',
    pointer_from=(610, 180),
    font=font_bold,
    badge_bg=(5, 150, 105) # Green
)
im_contact.save('guide_5_contact.png')
print('guide_5_contact.png done')

print('All 5 annotated guidance images generated successfully!')
