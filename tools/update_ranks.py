import os
import re

# Lucide SVGs
SVGS = {
    'grand': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/></svg>',
    'mega': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m2 4 3 12h14l3-12-6 7-4-7-4 7-6-7zm3 16h14"/></svg>',
    '3rd': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7.21 15 2.66 7.14a2 2 0 0 1 .13-2.2L4.4 2.8A2 2 0 0 1 6 2h12a2 2 0 0 1 1.6.8l1.6 2.14a2 2 0 0 1 .14 2.2L16.79 15"/><path d="M11 12 5.12 2.2"/><path d="m13 12 5.88-9.8"/><path d="M8 7h8"/><circle cx="12" cy="17" r="5"/><path d="M12 18v-2h-.5"/></svg>',
    '4th': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg>',
    '5th': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
}

def fix_index():
    path = '/Users/ankush/Desktop/Sumil Lucky Draw/index.html'
    with open(path, 'r') as f:
        html = f.read()
    
    # We will replace the innerHTML of .pcard-rank-art and also the small subtext if necessary
    
    # 1. Mega Prize -> Grand Prize
    html = html.replace('<div class="pcard-rank-art">🏆 MEGA PRIZE</div>', f'<div class="pcard-rank-art" style="display:flex; align-items:center; justify-content:center; gap:6px;">{SVGS["grand"]} GRAND PRIZE</div>')
    
    # 2. 1st Prize -> Mega Prize
    html = html.replace('<div class="pcard-rank-art">⭐ 1ST PRIZE</div>', f'<div class="pcard-rank-art" style="display:flex; align-items:center; justify-content:center; gap:6px;">{SVGS["mega"]} MEGA PRIZE</div>')
    
    # 3. 2nd Prize -> 3rd Prize
    html = html.replace('<div class="pcard-rank-art">🥈 2ND PRIZE</div>', f'<div class="pcard-rank-art" style="display:flex; align-items:center; justify-content:center; gap:6px;">{SVGS["3rd"]} 3RD PRIZE</div>')
    
    # 4. 3rd Prize -> 4th Prize
    html = html.replace('<div class="pcard-rank-art">🥉 3RD PRIZE</div>', f'<div class="pcard-rank-art" style="display:flex; align-items:center; justify-content:center; gap:6px;">{SVGS["4th"]} 4TH PRIZE</div>')
    
    # 5. Consolation -> 5th Prize
    html = html.replace('<div class="pcard-rank-art">🏅 CONSOLATION</div>', f'<div class="pcard-rank-art" style="display:flex; align-items:center; justify-content:center; gap:6px;">{SVGS["5th"]} 5TH PRIZE</div>')
    
    with open(path, 'w') as f:
        f.write(html)

def fix_prize():
    path = '/Users/ankush/Desktop/Sumil Lucky Draw/prize.html'
    with open(path, 'r') as f:
        html = f.read()
    
    # Update prizes object
    html = html.replace("rank:'🏆 MEGA PRIZE'", f"rank:'GRAND PRIZE', icon:'{SVGS['grand']}'")
    html = html.replace("rank:'⭐ 1ST PRIZE'", f"rank:'MEGA PRIZE', icon:'{SVGS['mega']}'")
    html = html.replace("rank:'🥈 2ND PRIZE'", f"rank:'3RD PRIZE', icon:'{SVGS['3rd']}'")
    html = html.replace("rank:'🥉 3RD PRIZE'", f"rank:'4TH PRIZE', icon:'{SVGS['4th']}'")
    html = html.replace("rank:'🎁 4TH PRIZE'", f"rank:'5TH PRIZE', icon:'{SVGS['5th']}'") # It was 4TH PRIZE in prize.html earlier ? Wait, let's just regex replace the rank
    
    # Wait, earlier grep showed it was rank:'🎁 4TH PRIZE' for index 4.
    
    # Update the injection logic in prize.html
    html = html.replace(
        "document.getElementById('modal-title').textContent=`🏆 ${prize.rank} — Winners`;",
        "document.getElementById('modal-title').innerHTML = `<span style='display:inline-flex;align-items:center;gap:8px;'>${prize.icon} ${prize.rank} — Winners</span>`;"
    )
    
    with open(path, 'w') as f:
        f.write(html)

if __name__ == '__main__':
    fix_index()
    fix_prize()
    print("Updated ranks and icons successfully!")
