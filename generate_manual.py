import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

def create_manual():
    doc = docx.Document()

    # 1-inch margins
    for section in doc.sections:
        section.top_margin = Inches(0.85)
        section.bottom_margin = Inches(0.85)
        section.left_margin = Inches(0.85)
        section.right_margin = Inches(0.85)

    # Color definitions
    COLOR_PRIMARY = RGBColor(234, 88, 12)     # Brand Orange #EA580C
    COLOR_DARK = RGBColor(28, 25, 23)         # Dark Stone #1C1917
    COLOR_MUTED = RGBColor(100, 95, 90)       # Muted Stone
    COLOR_EMERALD = RGBColor(5, 150, 105)     # Emerald Green #059669
    COLOR_RED = RGBColor(225, 29, 72)         # Crimson Red #E11D48
    HEX_ORANGE_LIGHT = "FFF7ED"
    HEX_GRAY_LIGHT = "F8F4EE"
    HEX_EMERALD_LIGHT = "ECFDF5"

    def set_cell_background(cell, hex_color):
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
        cell._tc.get_or_add_tcPr().append(shading)

    def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = OxmlElement('w:tcMar')
        for margin, value in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
            node = OxmlElement(f'w:{margin}')
            node.set(qn('w:w'), str(value))
            node.set(qn('w:type'), 'dxa')
            tcMar.append(node)
        tcPr.append(tcMar)

    def add_figure_image(image_path, caption_text):
        if os.path.exists(image_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(2)
            run = p_img.add_run()
            run.add_picture(image_path, width=Inches(6.4))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(12)
            r_cap = p_cap.add_run(f"📸 {caption_text}")
            r_cap.font.name = "Calibri"
            r_cap.font.size = Pt(9)
            r_cap.font.italic = True
            r_cap.font.color.rgb = COLOR_MUTED

    # --- COVER / HEADER ---
    p_badge = doc.add_paragraph()
    p_badge.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_badge.paragraph_format.space_after = Pt(2)
    r_badge = p_badge.add_run("OFFICIAL WEBSITE USER & VISUAL GUIDANCE MANUAL")
    r_badge.font.name = "Arial"
    r_badge.font.size = Pt(10)
    r_badge.font.bold = True
    r_badge.font.color.rgb = COLOR_PRIMARY

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("Ms.Porn Slushie\n(ร้านมิสพร สเลอปี้ บุรีรัมย์)")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(24)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_DARK

    p_subtitle = doc.add_paragraph()
    p_subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_subtitle.paragraph_format.space_after = Pt(14)
    r_sub = p_subtitle.add_run("Visual Step-by-Step Guide with Click Pointers & Content Management\nLocal Factory & Drink Shop • Buriram, Thailand")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_MUTED

    # Key Summary Box
    table_meta = doc.add_table(rows=1, cols=1)
    table_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_meta = table_meta.rows[0].cells[0]
    cell_meta.width = Inches(6.5)
    set_cell_background(cell_meta, HEX_ORANGE_LIGHT)
    set_cell_margins(cell_meta, top=140, bottom=140, left=200, right=200)

    p_meta = cell_meta.paragraphs[0]
    r_meta_title = p_meta.add_run("📌 QUICK FACTS & CORE REQUIREMENTS\n")
    r_meta_title.font.bold = True
    r_meta_title.font.size = Pt(10.5)
    r_meta_title.font.color.rgb = COLOR_PRIMARY

    bullets = [
        "Shop Name: Ms.Porn Slushie (ร้านมิสพร สเลอปี้ - โรงงานผลิตและหน้าร้าน)",
        "Location: Buriram Province, Thailand (Daily 09:00 AM – 06:30 PM)",
        "Main Produce: Signature Fresh Orange Slushie (สเลอปี้ส้มสายน้ำผึ้งแท้ 100%)",
        "Full Flavors: Strawberry, Thai Tea, Green Tea, Cola, Coco Milk, Coconut Water",
        "Delivery Coverage: Within 20 km radius across Buriram (Thermal zero-melt packing)",
        "Customer Hotline: 086-557-8822 (One-tap calling & copy button ready)",
        "Local Live URL: http://localhost:8000"
    ]
    for b in bullets:
        r_b = p_meta.add_run(f"• {b}\n")
        r_b.font.size = Pt(9.5)
        r_b.font.color.rgb = COLOR_DARK

    doc.add_paragraph()

    # --- SECTION 1: OVERVIEW & ACCESS ---
    h1 = doc.add_heading(level=1)
    r = h1.add_run("1. Website Overview & How to Run")
    r.font.color.rgb = COLOR_PRIMARY
    r.font.bold = True

    p = doc.add_paragraph()
    p.add_run(
        "The Ms.Porn Slushie website is an interactive single-page application crafted specifically to answer "
        "the three most important questions customers have: "
    )
    p.add_run("Where are we located? Where can we deliver? Where to contact? ").bold = True
    p.add_run(
        "It features a clean, cozy, and refreshing visual aesthetic with warm vanilla backgrounds, fresh orange accents, "
        "and clear bilingual (English & Thai) labeling for Buriram residents and visitors alike."
    )

    p_run = doc.add_paragraph()
    p_run.add_run("How to View the Live Website:\n").bold = True
    p_run.add_run("1. Live Local URL: Open Chrome, Edge, or Safari and go to ")
    r_link = p_run.add_run("http://localhost:8000\n")
    r_link.bold = True
    r_link.font.color.rgb = COLOR_PRIMARY
    p_run.add_run("2. Double-Click Open: You can also double-click ")
    p_run.add_run("index.html").bold = True
    p_run.add_run(" in the project folder to view it directly.\n")
    p_run.add_run("3. Free Online Publishing: Drag the project folder into Netlify (app.netlify.com/drop) to publish a live public web link in seconds!")

    # --- SECTION 2: HERO & NAVIGATION WITH VISUAL ARROWS ---
    h2 = doc.add_heading(level=1)
    r = h2.add_run("2. Hero Section & Navigation Guide (Where to Click)")
    r.font.color.rgb = COLOR_PRIMARY
    r.font.bold = True

    p = doc.add_paragraph()
    p.add_run(
        "The top of the website greets visitors with your brand story, highlighting that Ms.Porn Slushie is a local Buriram factory craft. "
        "Look at the visual guide below with the numbered arrows pointing to each interactive control:"
    )

    # Embed Figure 1
    add_figure_image("guide_1_hero.png", "Figure 1: Hero Section Click Guide — Header navigation, phone hotline, and 20km delivery check buttons.")

    p_guide1 = doc.add_paragraph()
    p_guide1.add_run("Click Controls on this Screen:\n").bold = True
    
    ctrls1 = [
        ("Arrow [1] - Top Header Actions:", "Located in the sticky navbar. Clicking the phone number (086-557-8822) opens the phone dialer immediately. Clicking 'Order Delivery' jumps down smoothly to the 20km delivery checker."),
        ("Arrow [2] - 'Check 20km Delivery Area' CTA:", "The primary orange button in the hero banner. Clicking this takes the customer directly to the Buriram interactive distance tool."),
        ("Arrow [3] - 'Call: 086-557-8822' CTA:", "A secondary high-visibility button allowing mobile and desktop users to dial the shop with one click."),
        ("Arrow [4] - Signature Orange Slushie Showcase:", "Spotlights your #1 Main Produce with frost badges, taste profile notes, and direct order link.")
    ]
    for title, desc in ctrls1:
        p_item = doc.add_paragraph()
        r_t = p_item.add_run(f"👉 {title} ")
        r_t.bold = True
        r_t.font.color.rgb = COLOR_PRIMARY
        r_d = p_item.add_run(desc)
        r_d.font.size = Pt(9.5)

    # --- SECTION 3: FLAVORS MENU WITH VISUAL ARROWS ---
    h3 = doc.add_heading(level=1)
    r = h3.add_run("3. Fresh Slushie Menu & Flavor Ordering")
    r.font.color.rgb = COLOR_PRIMARY
    r.font.bold = True

    p = doc.add_paragraph()
    p.add_run(
        "The menu presents all 7 flavors crafted at your factory, each with taste notes, Thai subtitles, "
        "and an interactive 'Order This' shortcut button:"
    )

    # Embed Figure 2
    add_figure_image("guide_2_flavors.png", "Figure 2: Menu Showcase Guide — Highlighting Main Produce and interactive 'Order This' buttons.")

    flavors_list = [
        ("🍊 Orange Slushie (สเลอปี้ส้มสด):", "Main signature produce made with 100% real citrus squeeze. Golden badge highlighted."),
        ("🍓 Strawberry Slushie (สเลอปี้สตรอว์เบอร์รี):", "Fruity, sweet, and fragrant red berry slushie."),
        ("🧋 Thai Tea Slushie (ชาไทยสเลอปี้):", "Deep brewed authentic Thai tea with creamy milk freeze."),
        ("🍵 Green Tea Slushie (ชาเขียวมัทฉะเกล็ดหิมะ):", "Soothing, aromatic matcha with crisp micro-crystals."),
        ("🥤 Cola Slushie (โคล่าสเลอปี้):", "Nostalgic fizzy cola micro-freeze."),
        ("🍫 Coco Milk (โกโก้นมสเลอปี้):", "Rich velvety chocolate cocoa blend."),
        ("🥥 Coconut Water (น้ำมะพร้าวสดเกล็ดหิมะ):", "100% pure young coconut water, ultra-hydrating.")
    ]
    for fname, fdesc in flavors_list:
        p_f = doc.add_paragraph()
        r_fn = p_f.add_run(f"• {fname} ")
        r_fn.bold = True
        r_fd = p_f.add_run(fdesc)
        r_fd.font.size = Pt(9.5)

    p_order_btn = doc.add_paragraph()
    r_ob = p_order_btn.add_run("💡 How the 'Order This' Button Works: ")
    r_ob.bold = True
    r_ob.font.color.rgb = COLOR_EMERALD
    p_order_btn.add_run(
        "When a customer clicks the 'Order This' button on any flavor card (pointed by Arrow [2]), "
        "the page automatically scrolls down to the Order Form, selects that flavor in the dropdown menu, "
        "and places the cursor in the Buriram Address input field ready for typing!"
    )

    # --- SECTION 4: 20KM DELIVERY AREA CHECKER ---
    h4 = doc.add_heading(level=1)
    r = h4.add_run("4. 'Where Can We Deliver' (20km Delivery Zone)")
    r.font.color.rgb = COLOR_PRIMARY
    r.font.bold = True

    p = doc.add_paragraph()
    p.add_run(
        "One of your primary requirements is making sure customers know where you deliver. "
        "We built an interactive 20km delivery radius checker that lets customers test their address immediately:"
    )

    # Embed Figure 3
    add_figure_image("guide_3_delivery.png", "Figure 3: Delivery Checker Guide — Landmark buttons, custom distance input, and confirmation badge.")

    steps_deliv = [
        ("Step 1 (Red Arrow): Click Any Buriram Landmark Chip", "Customers can tap common destinations such as Chang Arena (4.8 km), Buriram Clock Tower (2.5 km), Buriram Rajabhat University (3.2 km), Khao Kradong (8.5 km), Buriram Hospital (2.0 km), or Huai Chorakhe Mak (14.5 km)."),
        ("Step 2 (Orange Arrow): Or Type Custom Road / Kilometers", "If their location isn't a landmark, they can type their subdistrict or estimated km (e.g. 'Isan subdistrict', '8 km') and click 'Check Area'."),
        ("Step 3 (Green Arrow): Instant Delivery Eligibility Status", "The system displays a green badge confirming they are within the 20km radius, details the thermal zero-melt packaging guarantee, and displays the direct hotline.")
    ]
    for s_title, s_desc in steps_deliv:
        p_s = doc.add_paragraph()
        r_st = p_s.add_run(f"✅ {s_title}\n")
        r_st.bold = True
        r_st.font.size = Pt(10)
        r_st.font.color.rgb = COLOR_EMERALD
        r_sd = p_s.add_run(s_desc)
        r_sd.font.size = Pt(9.5)

    # --- SECTION 5: WHERE WE ARE (BURIRAM SHOP & FACTORY) ---
    h5 = doc.add_heading(level=1)
    r = h5.add_run("5. 'Where We Are' (Visit Buriram Shop & Map)")
    r.font.color.rgb = COLOR_PRIMARY
    r.font.bold = True

    p = doc.add_paragraph()
    p.add_run(
        "Customers looking to visit the shop and micro-factory in person can find complete physical details and directions:"
    )

    # Embed Figure 4
    add_figure_image("guide_4_location.png", "Figure 4: Location & Map Guide — Shop hours, address, parking, and Google Maps GPS navigation.")

    loc_details = [
        ("Physical Shop Location:", "Buriram Province, Thailand (อำเภอเมืองบุรีรัมย์ จ.บุรีรัมย์)."),
        ("Operating Hours:", "Monday – Sunday, 09:00 AM – 06:30 PM (Open daily with fresh morning batches)."),
        ("Open in Google Maps Button (Dark Arrow):", "One click opens Google Maps navigation with driving directions for motorbikes and cars."),
        ("Parking & Pickup Convenience:", "Dedicated frontage parking allows customers to quickly stop and grab takeout cups without parking hassles.")
    ]
    for l_title, l_desc in loc_details:
        p_l = doc.add_paragraph()
        r_lt = p_l.add_run(f"📍 {l_title} ")
        r_lt.bold = True
        r_ld = p_l.add_run(l_desc)
        r_ld.font.size = Pt(9.5)

    # --- SECTION 6: WHERE TO CONTACT & QUICK ORDER ---
    h6 = doc.add_heading(level=1)
    r = h6.add_run("6. 'Where to Contact' & Quick Order Guide")
    r.font.color.rgb = COLOR_PRIMARY
    r.font.bold = True

    p = doc.add_paragraph()
    p.add_run(
        "The contact section provides frictionless ways for customers to reach you immediately by phone, copy your number for messaging apps, or fill out a pre-order form:"
    )

    # Embed Figure 5
    add_figure_image("guide_5_contact.png", "Figure 5: Contact Guide — One-tap phone calling, number copy tool, and quick order submission.")

    contact_steps = [
        ("Arrow [1] - Big Call 086-557-8822 Button:", "Tapping this button triggers a direct phone call. Best for immediate delivery dispatch and urgent orders."),
        ("Arrow [2] - Copy Phone Number Button:", "Copies '0865578822' directly to the user's clipboard and flashes 'Copied: 086-557-8822!'. Perfect for customers pasting into Line search or WhatsApp."),
        ("Arrow [3] - Quick Order Submission Form:", "Customers enter their name, phone number, choose their slushie flavor (Orange, Strawberry, etc.), and their Buriram address. Clicking submit prepares an order summary and offers an instant confirmation dial.")
    ]
    for c_title, c_desc in contact_steps:
        p_c = doc.add_paragraph()
        r_ct = p_c.add_run(f"📞 {c_title}\n")
        r_ct.bold = True
        r_ct.font.size = Pt(10)
        r_ct.font.color.rgb = COLOR_PRIMARY
        r_cd = p_c.add_run(c_desc)
        r_cd.font.size = Pt(9.5)

    # --- SECTION 7: OWNER'S EDITING & CUSTOMIZATION GUIDE ---
    h7 = doc.add_heading(level=1)
    r = h7.add_run("7. How to Update Content (Owner's Cheatsheet)")
    r.font.color.rgb = COLOR_PRIMARY
    r.font.bold = True

    p = doc.add_paragraph()
    p.add_run(
        "You can easily edit and customize any text or flavor on the website. Here is a quick reference table showing which file and line to edit:"
    )

    table_edit = doc.add_table(rows=6, cols=3)
    table_edit.alignment = WD_TABLE_ALIGNMENT.CENTER

    headers = [("Item to Change", Inches(1.8)), ("File to Edit", Inches(1.2)), ("What to Look For & Replace", Inches(3.5))]
    for col_idx, (head_text, col_w) in enumerate(headers):
        cell = table_edit.rows[0].cells[col_idx]
        cell.width = col_w
        set_cell_background(cell, HEX_ORANGE_LIGHT)
        set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
        p_cell = cell.paragraphs[0]
        r_head = p_cell.add_run(head_text)
        r_head.bold = True
        r_head.font.size = Pt(9.5)
        r_head.font.color.rgb = COLOR_PRIMARY

    edit_rows = [
        ("Phone Number", "index.html & script.js", "Search for '086-557-8822' and '0865578822'. Replace with your new phone number."),
        ("Opening Hours", "index.html", "Search for '09:00 AM – 06:30 PM' and update your daily working hours."),
        ("Specific Street Address", "index.html", "Search for 'Buriram Province, Thailand' and insert your exact street name, subdistrict, or house number."),
        ("Delivery Distance", "index.html & script.js", "In index.html search '20km'. In script.js search 'if (distanceKm <= 20)' to adjust threshold."),
        ("New Drink Flavors", "index.html", "Duplicate any '<div class=\"flavor-card\">' block, change emoji, flavor name, and description.")
    ]

    for row_idx, (item, fname, desc) in enumerate(edit_rows, start=1):
        row = table_edit.rows[row_idx]
        for c_idx, val in enumerate([item, fname, desc]):
            cell = row.cells[c_idx]
            cell.width = headers[c_idx][1]
            if row_idx % 2 == 1:
                set_cell_background(cell, HEX_GRAY_LIGHT)
            set_cell_margins(cell, top=90, bottom=90, left=140, right=140)
            p_val = cell.paragraphs[0]
            r_val = p_val.add_run(val)
            r_val.font.size = Pt(9)
            if c_idx == 0:
                r_val.bold = True

    doc.add_paragraph()

    # --- DOCUMENT FOOTER ---
    p_foot = doc.add_paragraph()
    p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_foot = p_foot.add_run("— End of Visual Guidance Manual —\nPrepared for Ms.Porn Slushie • Buriram, Thailand • 2026")
    r_foot.font.size = Pt(9)
    r_foot.font.italic = True
    r_foot.font.color.rgb = COLOR_MUTED

    output_path = r"c:\Users\student\Downloads\web sandbox1\Ms_Porn_Slushie_Website_User_Manual.docx"
    doc.save(output_path)
    print(f"Updated manual with annotated images successfully saved at: {output_path}")

if __name__ == "__main__":
    create_manual()
