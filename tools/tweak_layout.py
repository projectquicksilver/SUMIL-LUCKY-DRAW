import os
import re

target_dir = '/Users/ankush/Desktop/Sumil Lucky Draw/refer'
index_file = os.path.join(target_dir, 'index.html')

with open(index_file, 'r') as f:
    content = f.read()

# 1. Update logos and banner
old_header = """    <!-- HEADER LOGOS -->
    <div class="header-logos" style="display:flex; justify-content: space-between; padding: 10px 20px;">
      <div class="logo-left-wrap">
        <img src="../sumil_logo.png" alt="Sumil" class="logo-left" style="height: 60px;">
      </div>
      <img src="../granulam.png" alt="Granulum" class="logo-right" style="height: 60px;">
    </div>

    <!-- TITLE BANNER at the top, 35vh -->
    <img src="../main_banner.png" alt="Main Banner" class="title-banner" style="height: 35vh; width: 100%; object-fit: contain; margin-top: 10px;">"""

new_header = """    <!-- HEADER LOGOS -->
    <div class="header-logos" style="display:flex; justify-content: center; padding: 10px 20px 0;">
      <div class="logo-left-wrap">
        <img src="../sumil_logo.png" alt="Sumil" class="logo-left" style="height: 80px;">
      </div>
    </div>

    <!-- TITLE BANNER at the top -->
    <img src="../main_banner.png" alt="Main Banner" class="title-banner" style="height: 48vh; width: 100%; object-fit: contain; margin-top: 5px;">"""

content = content.replace(old_header, new_header)

# 2. Pull cards up by modifying the divider and cards-row margin
# Let's add negative margin to cards row
content = content.replace(
    '/* ── CARDS ROW ── */\n.cards-row {\n  display: flex; justify-content: center;',
    '/* ── CARDS ROW ── */\n.cards-row {\n  display: flex; justify-content: center;\n  margin-top: -15px;'
)
content = content.replace(
    '<!-- DIVIDER -->\n    <div class="divider">',
    '<!-- DIVIDER -->\n    <div class="divider" style="margin-top:-10px; margin-bottom: 20px; z-index:2; position:relative;">'
)


# 3. Fix broken image names
content = content.replace(
    'src="../prize_pictures/Cash counting 1.png"',
    'src="../prize_pictures/cash counting machine.png"'
)
content = content.replace(
    'src="../prize_pictures/Safe 1.png"',
    'src="../prize_pictures/godrej safe.png"'
)
content = content.replace(
    'src="../prize_pictures/Chair 1.png"',
    'src="../prize_pictures/orthopedic chair cusion.png"'
)

with open(index_file, 'w') as f:
    f.write(content)

print("Layout tweaked successfully.")
