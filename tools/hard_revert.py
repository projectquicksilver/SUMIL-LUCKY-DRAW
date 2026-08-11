import os
import re

target_dir = '/Users/ankush/Desktop/Sumil Lucky Draw/refer'
index_file = os.path.join(target_dir, 'index.html')
prize_file = os.path.join(target_dir, 'prize.html')

with open(index_file, 'r') as f:
    index_html = f.read()

# Remove Lucide
index_html = index_html.replace('<script src="https://unpkg.com/lucide@latest"></script>\n', '')
index_html = index_html.replace('<script>lucide.createIcons();</script>\n', '')

# CSS
css_start = index_html.find('/* ── CARDS ROW ── */')
css_end = index_html.find('/* ── RIGHT GROUP ── */')

original_css = """/* ── CARDS ROW ── */
.cards-row {
  display: flex; justify-content: center;
  gap: clamp(5px, 1.2vw, 14px);
  width: 100%; max-width: 1020px;
  margin-top: auto;
  padding-bottom: 10px;
}

/* ── CARD WRAPPER ── */
.pcard-wrap {
  flex: 1; max-width: 192px;
  position: relative; border-radius: 18px;
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
}
/* Shimmer sweep */
.pcard::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(110deg, transparent 30%, rgba(255,200,80,0.14) 50%, transparent 70%);
  transform: translateX(-100%); transition: transform 0s; z-index: 2; pointer-events: none;
}
.pcard-wrap:hover .pcard::after { transform: translateX(100%); transition: transform 0.6s ease; }

/* Spotlight glow at top of card */
.pcard-spotlight {
  position: absolute; top: 0; left: 50%; transform: translateX(-50%);
  width: 80%; height: 48px;
  background: radial-gradient(ellipse at 50% 0%, rgba(255,160,30,0.26) 0%, transparent 75%);
  z-index: 1; pointer-events: none;
  animation: spotFlicker 3.5s ease-in-out infinite;
}
@keyframes spotFlicker { 0%,100%{opacity:0.6;} 50%{opacity:1;} }

/* ── CARD CONTENT ── */
.pcard-body {
  padding: 6px 8px 8px;
  display: flex; flex-direction: column; align-items: center; gap: 3px;
  position: relative; z-index: 3;
}

/* Platform circle with rings */
.pcard-platform {
  position: relative;
  width: clamp(82px,10.5vw,108px); height: clamp(82px,10.5vw,108px);
  display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.pcard-platform::before, .pcard-platform::after {
  content: ''; position: absolute; border-radius: 50%;
  border: 1.5px solid rgba(212,160,23,0.4);
  animation: ringPulse 2.5s ease-in-out infinite;
}
.pcard-platform::before { inset: 0; }
.pcard-platform::after  { inset: 11px; animation-delay: 0.55s; }
.ring3 {
  position: absolute; inset: 22px; border-radius: 50%;
  border: 1px solid rgba(212,160,23,0.22);
  animation: ringPulse 2.5s ease-in-out infinite 1.1s;
}
.pcard-platform-inner {
  position: absolute; inset: 25px; border-radius: 50%;
  background: radial-gradient(circle, rgba(212,160,23,0.24) 0%, rgba(212,160,23,0.06) 60%, transparent 100%);
  animation: innerGlow 2.5s ease-in-out infinite;
}
@keyframes innerGlow { 0%,100%{opacity:0.5;transform:scale(0.93);} 50%{opacity:1;transform:scale(1.07);} }
@keyframes ringPulse  { 0%,100%{opacity:0.3;transform:scale(1);}  50%{opacity:1;transform:scale(1.08);} }

/* Prize image — mix-blend-mode to kill white backgrounds */
.pcard-img {
  width: clamp(68px,8.5vw,100px); height: clamp(68px,8.5vw,100px);
  object-fit: contain;
  mix-blend-mode: lighten;
  filter: drop-shadow(0 4px 12px rgba(0,0,0,0.7));
  animation: floatUp 3.5s ease-in-out infinite;
  position: relative; z-index: 4;
  transition: filter 0.3s ease, transform 0.3s ease;
}
@keyframes floatUp { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-12px);} }
.pcard-wrap:hover .pcard-img {
  filter: drop-shadow(0 8px 22px rgba(212,160,23,0.65)) drop-shadow(0 0 20px rgba(212,160,23,0.4));
  transform: scale(1.12) translateY(-5px);
}

/* ── ANIMATED WORD-ART RANK BADGE ── */
.pcard-rank-art {
  position: relative;
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(11px, 1.5vw, 14px);
  font-weight: 900;
  letter-spacing: 2px;
  text-transform: uppercase;
  text-align: center;
  padding: 4px 14px;
  border-radius: 30px;
  white-space: nowrap;
  overflow: hidden;
  z-index: 1;
}
/* Shimmer sweep inside badge */
.pcard-rank-art::before {
  content: '';
  position: absolute; top: 0; left: -80%; width: 60%; height: 100%;
  background: linear-gradient(110deg, transparent, rgba(255,255,255,0.35), transparent);
  transform: skewX(-18deg);
  animation: badgeSheen 2.8s ease-in-out infinite;
}
@keyframes badgeSheen {
  0%,30% { left: -80%; opacity: 0; }
  32%     { opacity: 1; }
  65%     { left: 130%; opacity: 0; }
  100%    { left: 130%; opacity: 0; }
}

/* Mega */
.mega-card .pcard-rank-art {
  background: linear-gradient(135deg, #C0000A, #FF4500, #C0000A);
  color: #FFE0B0;
  box-shadow: 0 0 14px rgba(255,50,0,0.5), 0 0 28px rgba(255,50,0,0.25), inset 0 1px 0 rgba(255,180,100,0.3);
  border: 1.5px solid rgba(255,100,0,0.5);
  animation: megaGlow 2s ease-in-out infinite;
}
@keyframes megaGlow {
  0%,100% { box-shadow: 0 0 10px rgba(255,50,0,0.4), 0 0 22px rgba(255,50,0,0.2); }
  50%      { box-shadow: 0 0 22px rgba(255,80,0,0.8), 0 0 44px rgba(255,50,0,0.4), 0 0 60px rgba(255,100,0,0.2); }
}

/* 1st */
.rank1-card .pcard-rank-art {
  background: linear-gradient(135deg, #B8860B, #FFD700, #B8860B);
  color: #3B1200;
  box-shadow: 0 0 14px rgba(212,160,23,0.6), 0 0 28px rgba(212,160,23,0.3), inset 0 1px 0 rgba(255,240,150,0.5);
  border: 1.5px solid rgba(255,215,0,0.6);
  animation: goldGlow 2s ease-in-out infinite;
}
@keyframes goldGlow {
  0%,100% { box-shadow: 0 0 10px rgba(212,160,23,0.4), 0 0 22px rgba(212,160,23,0.2); }
  50%      { box-shadow: 0 0 22px rgba(212,160,23,0.9), 0 0 44px rgba(255,200,0,0.5), 0 0 60px rgba(255,160,0,0.2); }
}

/* 2nd */
.rank2-card .pcard-rank-art {
  background: linear-gradient(135deg, #708090, #C0C8D0, #708090);
  color: #1A2030;
  box-shadow: 0 0 12px rgba(176,196,222,0.5), 0 0 24px rgba(176,196,222,0.25), inset 0 1px 0 rgba(230,240,255,0.5);
  border: 1.5px solid rgba(176,196,222,0.6);
  animation: silverGlow 2s ease-in-out infinite;
}
@keyframes silverGlow {
  0%,100% { box-shadow: 0 0 10px rgba(176,196,222,0.4), 0 0 20px rgba(176,196,222,0.2); }
  50%      { box-shadow: 0 0 20px rgba(200,220,240,0.75), 0 0 40px rgba(176,196,222,0.4); }
}

/* 3rd */
.rank3-card .pcard-rank-art {
  background: linear-gradient(135deg, #8B5E3C, #CD8B55, #8B5E3C);
  color: #FFF0D8;
  box-shadow: 0 0 12px rgba(180,120,60,0.5), 0 0 24px rgba(180,120,60,0.25), inset 0 1px 0 rgba(240,200,140,0.4);
  border: 1.5px solid rgba(180,120,60,0.55);
  animation: bronzeGlow 2s ease-in-out infinite;
}
@keyframes bronzeGlow {
  0%,100% { box-shadow: 0 0 10px rgba(180,120,60,0.4), 0 0 20px rgba(180,120,60,0.2); }
  50%      { box-shadow: 0 0 20px rgba(200,140,70,0.7), 0 0 40px rgba(180,120,60,0.35); }
}

/* Consolation */
.rankc-card .pcard-rank-art {
  background: linear-gradient(135deg, #2E6B38, #52A860, #2E6B38);
  color: #DFFFEA;
  box-shadow: 0 0 12px rgba(60,160,80,0.5), 0 0 24px rgba(60,160,80,0.25), inset 0 1px 0 rgba(150,230,160,0.3);
  border: 1.5px solid rgba(60,160,80,0.55);
  animation: greenGlow 2s ease-in-out infinite;
}
@keyframes greenGlow {
  0%,100% { box-shadow: 0 0 10px rgba(60,160,80,0.4), 0 0 20px rgba(60,160,80,0.2); }
  50%      { box-shadow: 0 0 20px rgba(80,180,100,0.7), 0 0 40px rgba(60,160,80,0.35); }
}

/* Prize name + sub */
.pcard-name {
  font-family: 'Barlow Condensed', sans-serif;
  font-size: clamp(12px,1.6vw,15px); font-weight: 900;
  color: #fff; text-align: center; line-height: 1.15;
  text-shadow: 0 1px 10px rgba(255,255,255,0.2);
}
.pcard-sub {
  font-size: clamp(8px,1vw,10px); color: rgba(255,255,255,0.4);
  text-align: center; font-weight: 700; margin-top: 1px;
}
.pcard-qty {
  font-size: clamp(9px,1.2vw,11px); color: #FFD700; font-weight: 800;
  margin-top: 4px; letter-spacing: 0.5px;
}
.pcard-hint {
  font-size: 10px; color: rgba(255,255,255,0.35); text-transform: uppercase;
  margin-top: 6px; font-weight: 700; letter-spacing: 1px;
}
"""
index_html = index_html[:css_start] + original_css + index_html[css_end:]

# HTML
html_start = index_html.find('<!-- PRIZE CARDS ROW')
html_end = index_html.find('</section>')

original_html = """<!-- PRIZE CARDS ROW — no badge images, animated word-art ranks -->
    <div class="cards-row">

      <!-- MEGA PRIZE -->
      <a class="pcard-wrap mega-card" href="prize.html?prize=0">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Harley Davidson.png"
                   alt="Harley Davidson" class="pcard-img" style="animation-delay:0s">
            </div>
            <div class="pcard-rank-art">🏆 MEGA PRIZE</div>
            <div class="pcard-name">HARLEY-DAVIDSON<br>X440 BIKE</div>
            <div class="pcard-sub">Harley-Davidson X440</div>
            <span class="pcard-qty">🎁 × 1 Winner</span>
            <div class="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </a>

      <!-- 1ST PRIZE -->
      <a class="pcard-wrap rank1-card" href="prize.html?prize=1">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Bullet 1.png"
                   alt="Royal Enfield Bike" class="pcard-img" style="animation-delay:0.5s">
            </div>
            <div class="pcard-rank-art">⭐ 1ST PRIZE</div>
            <div class="pcard-name">ROYAL ENFIELD<br>BIKES</div>
            <div class="pcard-sub">Royal Enfield Bike</div>
            <span class="pcard-qty">🎁 × 2 Winners</span>
            <div class="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </a>

      <!-- 2ND PRIZE -->
      <a class="pcard-wrap rank2-card" href="prize.html?prize=2">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Cash counting 1.png"
                   alt="Cash Counting Machine" class="pcard-img" style="animation-delay:0.2s">
            </div>
            <div class="pcard-rank-art">🥈 2ND PRIZE</div>
            <div class="pcard-name">CASH COUNTING<br>MACHINE</div>
            <div class="pcard-sub">Heavy Duty</div>
            <span class="pcard-qty">🎁 × 50 Winners</span>
            <div class="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </a>

      <!-- 3RD PRIZE -->
      <a class="pcard-wrap rank3-card" href="prize.html?prize=3">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Safe 1.png"
                   alt="Godrej Safe" class="pcard-img" style="animation-delay:0.7s">
            </div>
            <div class="pcard-rank-art">🥉 3RD PRIZE</div>
            <div class="pcard-name">GODREJ<br>SAFE</div>
            <div class="pcard-sub">Digital Locker</div>
            <span class="pcard-qty">🎁 × 100 Winners</span>
            <div class="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </a>

      <!-- 4TH PRIZE -->
      <a class="pcard-wrap rankc-card" href="prize.html?prize=4">
        <div class="pcard">
          <div class="pcard-spotlight"></div>
          <div class="pcard-body">
            <div class="pcard-platform">
              <div class="ring3"></div><div class="pcard-platform-inner"></div>
              <img src="../prize_pictures/Chair 1.png"
                   alt="Orthopedic Chair" class="pcard-img" style="animation-delay:0.4s">
            </div>
            <div class="pcard-rank-art">🏅 CONSOLATION</div>
            <div class="pcard-name">ORTHOPEDIC CHAIR<br>BACK SUPPORT</div>
            <div class="pcard-sub">Ergonomic</div>
            <span class="pcard-qty">🎁 × 200 Winners</span>
            <div class="pcard-hint">🎯 View &amp; Spin</div>
          </div>
        </div>
      </a>

    </div><!-- end .cards-row -->
    </div><!-- end .hero -->
  </div>
"""
index_html = index_html[:html_start] + original_html + index_html[html_end:]

with open(index_file, 'w') as f:
    f.write(index_html)


# Revert prize.html
with open(prize_file, 'r') as f:
    prize_html = f.read()

# Remove Lucide
prize_html = prize_html.replace('<script src="https://unpkg.com/lucide@latest"></script>\n', '')
prize_html = prize_html.replace('<script>lucide.createIcons();</script>\n', '')

# Emojis in text
prize_html = prize_html.replace('<i data-lucide="trophy" style="width:18px;height:18px;stroke-width:2.5;margin-right:8px;vertical-align:middle;"></i> REVEAL WINNERS!', '🏆 &nbsp;REVEAL WINNERS!')
prize_html = prize_html.replace('<i data-lucide="trophy" style="width:24px;height:24px;stroke-width:2.5;vertical-align:middle;"></i> Lucky Draw Winners', '🏆 Lucky Draw Winners')
prize_html = prize_html.replace('<div class="winner-trophy"><i data-lucide="award" style="width:40px;height:40px;stroke-width:2;color:#FFD700;"></i></div>', '<div class="winner-trophy">🏆</div>')

# Need regex for dynamic title since it got mangled
prize_html = re.sub(
    r'<i data-lucide="award".*?</i> \$\{prize\.rank.*?\}',
    r'🏆 ${prize.rank}',
    prize_html
)

# Wheel icons
prize_html = prize_html.replace("icon:'✦'", "icon:'🏆'")
prize_html = prize_html.replace("icon:'★'", "icon:'⭐'")
prize_html = prize_html.replace("icon:'❖'", "icon:'🎁'")

# Prize names
prize_html = prize_html.replace("'MEGA PRIZE'", "'🏆 MEGA PRIZE'")
prize_html = prize_html.replace("'1ST PRIZE'", "'⭐ 1ST PRIZE'")
prize_html = prize_html.replace("'2ND PRIZE'", "'🥈 2ND PRIZE'")
prize_html = prize_html.replace("'3RD PRIZE'", "'🥉 3RD PRIZE'")
prize_html = prize_html.replace("'CONSOLATION'", "'🏅 CONSOLATION'")

with open(prize_file, 'w') as f:
    f.write(prize_html)

print("Hard revert completed successfully.")
