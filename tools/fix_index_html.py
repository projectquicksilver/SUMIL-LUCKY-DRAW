import os
import re

target_dir = '/Users/ankush/Desktop/Sumil Lucky Draw/refer'
index_file = os.path.join(target_dir, 'index.html')

with open(index_file, 'r') as f:
    content = f.read()

# The point where the file broke is after `.pcard-hint { ... }`
# Find `.pcard-hint {` and its closing brace `}`
hint_pos = content.find('.pcard-hint {')
if hint_pos != -1:
    end_brace = content.find('}', hint_pos)
    
    missing_middle = """
/* ── BOTTOM STRIP ── */
.bottom-strip {
  width: 100%; margin-top: 8px;
}
.bottom-strip img { width: 100%; object-fit: contain; display: block; }

/* Custom glowing backdrop for Sumil logo */
.logo-left-wrap {
  position: relative;
  display: inline-block;
}
.logo-left-wrap::before {
  content: '';
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 140%; height: 140%;
  background: radial-gradient(circle, rgba(255,255,255,0.85) 0%, rgba(255,215,0,0.5) 40%, transparent 70%);
  z-index: -1;
  border-radius: 50%;
  filter: blur(8px);
}
</style>
</head>
<body>

<section class="hero">
  <div class="hero-bg"></div>
  <div class="rays"></div>
  <div class="fx" id="fx"></div>

  <div class="content">

    <!-- TOP GROUP: logos + banner + strip + main image + divider -->
    <div class="top-group">

    <!-- HEADER LOGOS -->
    <div class="header-logos" style="display:flex; justify-content: space-between; padding: 10px 20px;">
      <div class="logo-left-wrap">
        <img src="../sumil_logo.png" alt="Sumil" class="logo-left" style="height: 60px;">
      </div>
      <img src="../granulam.png" alt="Granulum" class="logo-right" style="height: 60px;">
    </div>

    <!-- TITLE BANNER at the top, 35vh -->
    <img src="../main_banner.png" alt="Main Banner" class="title-banner" style="height: 35vh; width: 100%; object-fit: contain; margin-top: 10px;">

    <!-- DIVIDER -->
    <div class="divider">
      <div class="div-line"></div>
      <span class="div-txt">✦ Click a Prize to Enter ✦</span>
      <div class="div-line"></div>
    </div>

    </div><!-- end .top-group -->

"""
    
    # We replace from the end brace of .pcard-hint to <!-- PRIZE CARDS ROW ...
    cards_row_pos = content.find('<!-- PRIZE CARDS ROW')
    if cards_row_pos != -1:
        content = content[:end_brace+1] + "\n" + missing_middle + content[cards_row_pos:]

# Now fix the bottom missing tags
bottom_missing = """
  </div><!-- end .content -->
</section>

<script src="audio.js"></script>
<script>
(function(){
  const layer = document.getElementById('fx');
  const colors = ['#D4A017','#FFD966','#FF6B00','#FF3B3B','#FFF5DC','#B87333','#FF9060'];
  for(let i = 0; i < 65; i++){
    const el = document.createElement('div'); el.className = 'cf';
    const c = colors[i % colors.length], w = 4 + Math.random()*10, h = w*(Math.random()>.4?2.5:1);
    el.style.cssText = `left:${Math.random()*100}%;width:${w}px;height:${h}px;background:${c};border-radius:${Math.random()>.5?'50%':'3px'};animation-delay:${Math.random()*12}s;animation-duration:${7+Math.random()*9}s;`;
    layer.appendChild(el);
  }
  for(let i = 0; i < 24; i++){
    const s = document.createElement('div'); s.className = 'sp';
    const sz = 3 + Math.random()*10;
    s.style.cssText = `left:${Math.random()*100}%;top:${Math.random()*95}%;width:${sz}px;height:${sz}px;animation-delay:${Math.random()*4}s;animation-duration:${1.5+Math.random()*3}s;`;
    layer.appendChild(s);
  }
  for(let i = 0; i < 7; i++){
    const o = document.createElement('div'); o.className = 'orb';
    const sz = 60 + Math.random()*180;
    o.style.cssText = `left:${Math.random()*100}%;top:${Math.random()*100}%;width:${sz}px;height:${sz}px;animation-delay:${Math.random()*5}s;animation-duration:${5+Math.random()*6}s;`;
    layer.appendChild(o);
  }
})();
</script>
</body>
</html>
"""

# Find where it prematurely ended
end_cards_row = content.find('    </div><!-- end .cards-row -->')
if end_cards_row != -1:
    content = content[:end_cards_row + len('    </div><!-- end .cards-row -->')] + "\n" + bottom_missing

with open(index_file, 'w') as f:
    f.write(content)

print("index.html structure restored successfully.")
