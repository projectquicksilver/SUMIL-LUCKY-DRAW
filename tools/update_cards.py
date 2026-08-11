import re
import os

target_dir = '/Users/ankush/Desktop/Sumil Lucky Draw/refer'
index_file = os.path.join(target_dir, 'index.html')
prize_file = os.path.join(target_dir, 'prize.html')

with open(index_file, 'r') as f:
    index_html = f.read()

# 1. Add Lucide CDN
if 'lucide@latest' not in index_html:
    index_html = index_html.replace(
        '<link href="https://fonts.googleapis.com/css2',
        '<script src="https://unpkg.com/lucide@latest"></script>\n<link href="https://fonts.googleapis.com/css2'
    )
if 'lucide.createIcons();' not in index_html:
    index_html = index_html.replace('</body>', '<script>lucide.createIcons();</script>\n</body>')

# 2. Update Card CSS
old_css = """/* ── CARD BODY ── */
.pcard {
  position: relative; z-index: 1; width: 100%; border-radius: 16px; overflow: hidden;
  background: linear-gradient(160deg, rgba(75,79,113,0.55) 0%, rgba(34,40,86,0.75) 60%, rgba(10,13,32,0.88) 100%);
  backdrop-filter: blur(18px);
  border: 1.5px solid rgba(255,215,0,0.45);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.15),
    inset 0 -1px 0 rgba(0,0,0,0.2),
    0 8px 30px rgba(0,0,0,0.6),
    0 0 20px rgba(255,215,0,0.15);
  transition: transform 0.32s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.3s ease;
}
.pcard-wrap:hover .pcard {
  transform: translateY(-10px) scale(1.035);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.3),
    0 24px 58px rgba(0,0,0,0.7),
    0 0 70px rgba(255,215,0,0.45);
}"""

new_css = """/* ── CARD BODY ── */
.pcard {
  position: relative; z-index: 1; width: 100%; border-radius: 16px; overflow: hidden;
  background: linear-gradient(160deg, rgba(34,40,86,0.95) 0%, rgba(10,13,32,0.98) 100%);
  backdrop-filter: blur(18px);
  border: 1px solid rgba(255,215,0,0.55);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.1),
    inset 0 -1px 0 rgba(0,0,0,0.4),
    0 12px 36px rgba(0,0,0,0.7),
    0 0 25px rgba(255,215,0,0.15);
  transition: transform 0.32s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.3s ease;
}
.pcard-wrap:hover .pcard {
  transform: translateY(-10px) scale(1.035);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.3),
    0 24px 60px rgba(0,0,0,0.8),
    0 0 80px rgba(255,215,0,0.5);
}"""
index_html = index_html.replace(old_css, new_css)

# Update rank-art CSS
index_html = index_html.replace("""
  padding: 4px 14px;
  border-radius: 30px;""", """
  padding: 4px 14px;
  border-radius: 30px;
  display: inline-flex;
  align-items: center;
  gap: 6px;""")

index_html = index_html.replace("""
.pcard-qty {
  font-size: clamp(9px,1.2vw,11px); color: #FFD700; font-weight: 800;
  margin-top: 4px; letter-spacing: 0.5px;
}""", """
.pcard-qty {
  display: inline-flex; align-items: center; gap: 4px;
  font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 700;
  color: #FFF; background: rgba(255,255,255,0.08); padding: 3px 10px; border-radius: 12px;
  margin-top: 4px; letter-spacing: 0.5px;
}
.pcard-qty i { width: 12px; height: 12px; color: #FFD700; stroke-width: 2.5; }""")

index_html = index_html.replace("""
.pcard-hint {
  font-size: 10px; color: rgba(255,255,255,0.35); text-transform: uppercase;
  margin-top: 6px; font-weight: 700; letter-spacing: 1px;
}""", """
.pcard-hint {
  display: inline-flex; align-items: center; gap: 4px;
  font-size: 10px; color: #FFD700; opacity: 0.8; text-transform: uppercase;
  margin-top: 6px; font-weight: 700; letter-spacing: 1px;
}
.pcard-hint i { width: 12px; height: 12px; stroke-width: 2.5; }""")

# Replace HTML elements
# Mega
index_html = index_html.replace('🏆 MEGA PRIZE', '<i data-lucide="crown" style="width:16px;height:16px;stroke-width:2.5;"></i> MEGA PRIZE')
index_html = index_html.replace('⭐ 1ST PRIZE', '<i data-lucide="star" style="width:14px;height:14px;stroke-width:2.5;"></i> 1ST PRIZE')
index_html = index_html.replace('🥈 2ND PRIZE', '<i data-lucide="medal" style="width:14px;height:14px;stroke-width:2.5;"></i> 2ND PRIZE')
index_html = index_html.replace('🥉 3RD PRIZE', '<i data-lucide="award" style="width:14px;height:14px;stroke-width:2.5;"></i> 3RD PRIZE')
index_html = index_html.replace('🏅 CONSOLATION', '<i data-lucide="gift" style="width:14px;height:14px;stroke-width:2.5;"></i> CONSOLATION')

index_html = re.sub(r'🎁 (× \d+ Winners?)', r'<i data-lucide="gift"></i> \1', index_html)
index_html = re.sub(r'🎯 View &amp; Spin', r'<i data-lucide="mouse-pointer-click"></i> View &amp; Spin', index_html)


with open(index_file, 'w') as f:
    f.write(index_html)


# Also do prize.html
with open(prize_file, 'r') as f:
    prize_html = f.read()

if 'lucide@latest' not in prize_html:
    prize_html = prize_html.replace(
        '<link href="https://fonts.googleapis.com/css2',
        '<script src="https://unpkg.com/lucide@latest"></script>\n<link href="https://fonts.googleapis.com/css2'
    )
if 'lucide.createIcons();' not in prize_html:
    prize_html = prize_html.replace('</body>', '<script>lucide.createIcons();</script>\n</body>')

# Replace emojis in text content
prize_html = prize_html.replace('🏆 &nbsp;REVEAL WINNERS!', '<i data-lucide="trophy" style="width:18px;height:18px;stroke-width:2.5;margin-right:8px;vertical-align:middle;"></i> REVEAL WINNERS!')
prize_html = prize_html.replace('🏆 Lucky Draw Winners', '<i data-lucide="trophy" style="width:24px;height:24px;stroke-width:2.5;vertical-align:middle;"></i> Lucky Draw Winners')
prize_html = prize_html.replace('<div class="winner-trophy">🏆</div>', '<div class="winner-trophy"><i data-lucide="award" style="width:40px;height:40px;stroke-width:2;color:#FFD700;"></i></div>')
prize_html = prize_html.replace('🏆 ${prize.rank}', '<i data-lucide="award" style="width:24px;height:24px;stroke-width:2.5;vertical-align:middle;"></i> ${prize.rank.replace(\'<i data-lucide="crown" style="width:16px;height:16px;stroke-width:2.5;"></i> \', \'\').replace(\'<i data-lucide="star" style="width:14px;height:14px;stroke-width:2.5;"></i> \', \'\').replace(\'<i data-lucide="medal" style="width:14px;height:14px;stroke-width:2.5;"></i> \', \'\').replace(\'<i data-lucide="award" style="width:14px;height:14px;stroke-width:2.5;"></i> \', \'\').replace(\'<i data-lucide="gift" style="width:14px;height:14px;stroke-width:2.5;"></i> \', \'\')}')

# Replace emojis in wheel configs with simpler unicode characters
prize_html = prize_html.replace("icon:'🏆'", "icon:'✦'")
prize_html = prize_html.replace("icon:'⭐'", "icon:'★'")
prize_html = prize_html.replace("icon:'🎁'", "icon:'❖'")

# Update prize configs
prize_html = prize_html.replace("'🏆 MEGA PRIZE'", "'MEGA PRIZE'")
prize_html = prize_html.replace("'⭐ 1ST PRIZE'", "'1ST PRIZE'")
prize_html = prize_html.replace("'🥈 2ND PRIZE'", "'2ND PRIZE'")
prize_html = prize_html.replace("'🥉 3RD PRIZE'", "'3RD PRIZE'")
prize_html = prize_html.replace("'🏅 CONSOLATION'", "'CONSOLATION'")


with open(prize_file, 'w') as f:
    f.write(prize_html)

print("Updated both files.")
