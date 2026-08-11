import os

target_dir = '/Users/ankush/Desktop/Sumil Lucky Draw/refer'
index_file = os.path.join(target_dir, 'index.html')

with open(index_file, 'r') as f:
    content = f.read()

css_start = content.find('/* ── CARDS ROW ── */')
css_end = content.find('/* ── RIGHT GROUP ── */')

if css_start != -1 and css_end != -1:
    new_css = """/* ── CARDS ROW ── */
.cards-row {
  display: flex; justify-content: center;
  gap: clamp(5px, 1.2vw, 14px);
  width: 100%; max-width: 1050px;
  margin-top: auto;
  padding-bottom: 20px;
}

/* ── CARD WRAPPER ── */
.pcard-wrap {
  flex: 1; max-width: 200px;
  position: relative; border-radius: 16px;
  cursor: pointer; text-decoration: none; display: block;
}

/* Spinning gold border on hover */
.pcard-wrap::before {
  content: ''; position: absolute; inset: -2px; border-radius: 19px;
  background: conic-gradient(from 0deg, #FFD700 0%, #FFF4CC 25%, #FFD700 50%, #B8860B 75%, #FFD700 100%);
  opacity: 0; transition: opacity 0.35s ease; z-index: 0;
  animation: borderSpin 2.5s linear infinite;
}
.pcard-wrap:hover::before { opacity: 1; box-shadow: 0 0 30px rgba(255,215,0,0.5); }
@keyframes borderSpin {
  0%   { background: conic-gradient(from 0deg,   #FFD700,#FFF4CC,#FFD700,#B8860B,#FFD700); }
  25%  { background: conic-gradient(from 90deg,  #FFD700,#FFF4CC,#FFD700,#B8860B,#FFD700); }
  50%  { background: conic-gradient(from 180deg, #FFD700,#FFF4CC,#FFD700,#B8860B,#FFD700); }
  75%  { background: conic-gradient(from 270deg, #FFD700,#FFF4CC,#FFD700,#B8860B,#FFD700); }
  100% { background: conic-gradient(from 360deg, #FFD700,#FFF4CC,#FFD700,#B8860B,#FFD700); }
}

.pcard-wrap::after {
  content: ''; position: absolute; inset: -16px; border-radius: 28px;
  background: radial-gradient(circle, rgba(212,160,23,0.2) 0%, transparent 70%);
  opacity: 0; transition: opacity 0.35s ease; z-index: -1;
  animation: auraBreath 3s ease-in-out infinite;
}
.pcard-wrap:hover::after { opacity: 1; }
@keyframes auraBreath { 0%,100%{transform:scale(0.95);} 50%{transform:scale(1.06);} }


/* ── CARD BODY ── */
.pcard {
  position: relative; z-index: 1; width: 100%; border-radius: 16px; overflow: hidden;
  background: #111111; /* Dark grey/black from image */
  border: 1px solid rgba(255,255,255,0.08);
  height: 100%;
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.05),
    inset 0 -1px 0 rgba(0,0,0,0.4),
    0 8px 30px rgba(0,0,0,0.8),
    0 0 15px rgba(0,0,0,0.5);
  transition: transform 0.32s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.3s ease;
}
.pcard-wrap:hover .pcard {
  transform: translateY(-10px) scale(1.035);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.1),
    0 24px 60px rgba(0,0,0,0.9),
    0 0 60px rgba(255,215,0,0.3);
}

/* Shimmer sweep */
.pcard::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(110deg, transparent 30%, rgba(255,200,80,0.08) 50%, transparent 70%);
  transform: translateX(-100%); transition: transform 0s; z-index: 2; pointer-events: none;
}
.pcard-wrap:hover .pcard::after { transform: translateX(100%); transition: transform 0.6s ease; }

/* Spotlight glow at top of card */
.pcard-spotlight {
  position: absolute; top: 0; left: 50%; transform: translateX(-50%);
  width: 80%; height: 48px;
  background: radial-gradient(ellipse at 50% 0%, rgba(255,160,30,0.2) 0%, transparent 75%);
  z-index: 1; pointer-events: none;
  animation: spotFlicker 3.5s ease-in-out infinite;
}
@keyframes spotFlicker { 0%,100%{opacity:0.6;} 50%{opacity:1;} }

/* ── CARD CONTENT ── */
.pcard-body {
  padding: 10px 8px 12px;
  display: flex; flex-direction: column; align-items: center; gap: 4px;
  position: relative; z-index: 3;
  height: 100%;
}

/* Platform circle with rings */
.pcard-platform {
  position: relative;
  width: clamp(82px,10.5vw,108px); height: clamp(82px,10.5vw,108px);
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  margin-top: 10px;
}
.pcard-platform::before, .pcard-platform::after {
  content: ''; position: absolute; border-radius: 50%;
  border: 1.5px solid rgba(255,255,255,0.15); /* Subtler rings matching dark theme */
  animation: ringPulse 2.5s ease-in-out infinite;
}
.pcard-platform::before { inset: 0; }
.pcard-platform::after  { inset: 11px; animation-delay: 0.55s; }
.ring3 {
  position: absolute; inset: 22px; border-radius: 50%;
  border: 1px solid rgba(255,255,255,0.08);
  animation: ringPulse 2.5s ease-in-out infinite 1.1s;
}
.pcard-platform-inner {
  position: absolute; inset: 25px; border-radius: 50%;
  background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, transparent 80%);
  animation: innerGlow 2.5s ease-in-out infinite;
}
@keyframes innerGlow { 0%,100%{opacity:0.5;transform:scale(0.93);} 50%{opacity:1;transform:scale(1.07);} }
@keyframes ringPulse  { 0%,100%{opacity:0.3;transform:scale(1);}  50%{opacity:1;transform:scale(1.08);} }

/* Prize image */
.pcard-img {
  width: clamp(68px,8.5vw,100px); height: clamp(68px,8.5vw,100px);
  object-fit: contain;
  mix-blend-mode: lighten;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,0.9));
  animation: floatUp 3.5s ease-in-out infinite;
  position: relative; z-index: 4;
  transition: filter 0.3s ease, transform 0.3s ease;
}
@keyframes floatUp { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-12px);} }
.pcard-wrap:hover .pcard-img {
  filter: drop-shadow(0 8px 22px rgba(212,160,23,0.65)) drop-shadow(0 0 20px rgba(212,160,23,0.4));
  transform: scale(1.12) translateY(-5px);
}

/* ── ANIMATED WORD-ART RANK BADGE (Styled like the image) ── */
.pcard-rank-art {
  font-family: 'Inter', sans-serif;
  font-size: 10px; font-weight: 800;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  padding: 4px 14px;
  border-radius: 20px;
  display: inline-flex; align-items: center; gap: 6px;
  position: relative; z-index: 1;
}

/* Mega/Grand (Gold) */
.mega-card .pcard-rank-art {
  background: #FFA800; /* Flat gold from image */
  color: #000;
  box-shadow: 0 4px 10px rgba(0,0,0,0.5);
}
/* Others (Dark Grey) */
.rank-other .pcard-rank-art {
  background: rgba(255,255,255,0.12); /* Semi-transparent grey */
  color: #FFF;
  border: 1px solid rgba(255,255,255,0.05);
}

/* Prize name */
.pcard-name {
  font-family: 'Inter', sans-serif;
  font-size: clamp(12px,1.6vw,14px); font-weight: 800;
  color: #fff; text-align: center; line-height: 1.2;
  margin-top: auto;
}
.pcard-sub { display: none; } /* Hidden as per clean image look */

/* Quantity Badge */
.pcard-qty {
  display: inline-flex; align-items: center; gap: 4px;
  font-family: 'Inter', sans-serif; font-size: 10px; font-weight: 800;
  background: #FFA800; color: #000; padding: 4px 12px; border-radius: 12px;
  margin-top: 6px; letter-spacing: 0.5px;
  text-transform: uppercase;
}
.pcard-qty i { width: 12px; height: 12px; color: #000; stroke-width: 2.5; }

/* Hint Badge */
.pcard-hint {
  display: inline-flex; align-items: center; gap: 4px;
  font-size: 9px; color: #FFA800; opacity: 0.7; text-transform: uppercase;
  margin-top: 6px; font-weight: 700; letter-spacing: 1px;
}
.pcard-hint i { width: 10px; height: 10px; stroke-width: 2.5; }
"""
    content = content[:css_start] + new_css + content[css_end:]

html_start = content.find('<!-- PRIZE CARDS ROW -->')
html_end = content.find('</section>')

if html_start != -1 and html_end != -1:
    new_html = """<!-- PRIZE CARDS ROW -->
    <div class="cards-row">

      <!-- GRAND PRIZE -->
      <a class="pcard-wrap mega-card" href="prize.html?prize=0">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-rank-art"><i data-lucide="crown" style="width:14px;height:14px;stroke-width:2.5;"></i> GRAND PRIZE</div>
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Harley Davidson.png" alt="Harley Davidson" class="pcard-img" style="animation-delay:0s">
            </div>
            <div class="pcard-name">HARLEY-DAVIDSON<br>X440</div>
            <span class="pcard-qty"><i data-lucide="gift"></i> 1 Winner</span>
            <div class="pcard-hint"><i data-lucide="mouse-pointer-click"></i> View &amp; Spin</div>
          </div>
        </div>
      </a>

      <!-- MEGA PRIZE -->
      <a class="pcard-wrap rank-other" href="prize.html?prize=1">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-rank-art"><i data-lucide="star" style="width:12px;height:12px;stroke-width:2.5;"></i> MEGA PRIZE</div>
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Bullet 1.png" alt="Royal Enfield Bike" class="pcard-img" style="animation-delay:0.5s">
            </div>
            <div class="pcard-name">ROYAL ENFIELD BIKE</div>
            <span class="pcard-qty"><i data-lucide="gift"></i> 2 Winners</span>
            <div class="pcard-hint"><i data-lucide="mouse-pointer-click"></i> View &amp; Spin</div>
          </div>
        </div>
      </a>

      <!-- 3RD PRIZE -->
      <a class="pcard-wrap rank-other" href="prize.html?prize=2">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-rank-art"><i data-lucide="medal" style="width:12px;height:12px;stroke-width:2.5;"></i> 3RD PRIZE</div>
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Cash counting 1.png" alt="Cash Counting Machine" class="pcard-img" style="animation-delay:0.2s">
            </div>
            <div class="pcard-name">CASH COUNTING<br>MACHINE</div>
            <span class="pcard-qty"><i data-lucide="gift"></i> 50 Winners</span>
            <div class="pcard-hint"><i data-lucide="mouse-pointer-click"></i> View &amp; Spin</div>
          </div>
        </div>
      </a>

      <!-- 4TH PRIZE -->
      <a class="pcard-wrap rank-other" href="prize.html?prize=3">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-rank-art"><i data-lucide="award" style="width:12px;height:12px;stroke-width:2.5;"></i> 4TH PRIZE</div>
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Safe 1.png" alt="Godrej Safe" class="pcard-img" style="animation-delay:0.7s">
            </div>
            <div class="pcard-name">GODREJ SAFE</div>
            <span class="pcard-qty"><i data-lucide="gift"></i> 100 Winners</span>
            <div class="pcard-hint"><i data-lucide="mouse-pointer-click"></i> View &amp; Spin</div>
          </div>
        </div>
      </a>

      <!-- 5TH PRIZE -->
      <a class="pcard-wrap rank-other" href="prize.html?prize=4">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-rank-art"><i data-lucide="award" style="width:12px;height:12px;stroke-width:2.5;"></i> 5TH PRIZE</div>
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Chair 1.png" alt="Orthopedic Chair" class="pcard-img" style="animation-delay:0.4s">
            </div>
            <div class="pcard-name">ORTHOPEDIC CHAIR<br>BACK SUPPORT</div>
            <span class="pcard-qty"><i data-lucide="gift"></i> 200 Winners</span>
            <div class="pcard-hint"><i data-lucide="mouse-pointer-click"></i> View &amp; Spin</div>
          </div>
        </div>
      </a>

    </div><!-- end .cards-row -->
    </div><!-- end .hero -->
  </div>
"""
    content = content[:html_start] + new_html + content[html_end:]

with open(index_file, 'w') as f:
    f.write(content)

print("Restored original card layout and applied dark/gold color styling.")
