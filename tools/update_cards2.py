import re
import os

target_dir = '/Users/ankush/Desktop/Sumil Lucky Draw/refer'
index_file = os.path.join(target_dir, 'index.html')

with open(index_file, 'r') as f:
    content = f.read()

# 1. CSS Overhaul
old_css_start = content.find('/* ── CARDS ROW ── */')
old_css_end = content.find('/* ── RIGHT GROUP ── */')

if old_css_start != -1 and old_css_end != -1:
    new_css = """/* ── CARDS ROW ── */
.cards-row {
  display: flex; justify-content: center;
  gap: 12px;
  width: 100%; max-width: 1050px;
  margin-top: auto;
  padding-bottom: 20px;
}

/* ── CARD WRAPPER ── */
.pcard-wrap {
  flex: 1; max-width: 200px;
  position: relative; border-radius: 8px;
  cursor: pointer; text-decoration: none; display: block;
}
.pcard-wrap::after {
  content: ''; position: absolute; inset: -10px; border-radius: 12px;
  background: radial-gradient(circle, rgba(255,215,0,0.15) 0%, transparent 70%);
  opacity: 0; transition: opacity 0.3s ease; z-index: -1;
}
.pcard-wrap:hover::after { opacity: 1; }

/* ── CARD BODY ── */
.pcard {
  position: relative; z-index: 1; width: 100%; border-radius: 8px; overflow: hidden;
  background: #15151A; /* Dark almost black/grey */
  border: 1px solid rgba(255,255,255,0.08);
  height: 100%;
  display: flex; flex-direction: column;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.pcard-wrap:hover .pcard {
  transform: translateY(-8px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.8), 0 0 20px rgba(255,184,0,0.2);
  border-color: rgba(255,184,0,0.3);
}

.pcard-body {
  padding: 16px 12px 20px;
  display: flex; flex-direction: column; align-items: center;
  height: 100%;
}

/* Top Badge */
.pcard-rank-badge {
  font-family: 'Inter', sans-serif;
  font-size: 10px; font-weight: 800;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  padding: 5px 16px;
  border-radius: 20px;
  margin-bottom: 25px;
}
.rank-grand {
  background: #FFA800;
  color: #000;
}
.rank-other {
  background: rgba(255,255,255,0.12);
  color: #FFF;
}

/* Image Wrap */
.pcard-img-wrap {
  position: relative;
  width: 100%;
  display: flex; align-items: center; justify-content: center;
  height: 90px;
  margin-bottom: 20px;
}
.pcard-img-glow {
  position: absolute;
  width: 80px; height: 80px;
  background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, transparent 60%);
  border-radius: 50%;
  z-index: 0;
}
.pcard-img {
  max-width: 85%; max-height: 85%;
  object-fit: contain;
  position: relative; z-index: 1;
  transition: transform 0.3s ease;
}
.pcard-wrap:hover .pcard-img {
  transform: scale(1.1);
}

/* Prize Name */
.pcard-name {
  font-family: 'Inter', sans-serif;
  font-size: 13px; font-weight: 800;
  color: #FFF; text-align: center; line-height: 1.3;
  margin-top: auto; margin-bottom: 15px;
}

/* Quantity Badge */
.pcard-qty-badge {
  font-family: 'Inter', sans-serif;
  font-size: 10px; font-weight: 800;
  background: #FFA800; color: #000;
  padding: 4px 14px; border-radius: 12px;
  text-transform: uppercase;
}

"""
    content = content[:old_css_start] + new_css + content[old_css_end:]

# 2. HTML Overhaul
html_start = content.find('<!-- PRIZE CARDS ROW')
html_end = content.find('</section>')

if html_start != -1 and html_end != -1:
    new_html = """<!-- PRIZE CARDS ROW -->
    <div class="cards-row">

      <!-- GRAND PRIZE -->
      <a class="pcard-wrap mega-card" href="prize.html?prize=0">
        <div class="pcard">
          <div class="pcard-body">
            <div class="pcard-rank-badge rank-grand">GRAND PRIZE</div>
            <div class="pcard-img-wrap">
               <div class="pcard-img-glow"></div>
               <img src="../prize_pictures/Harley Davidson.png" alt="Harley Davidson" class="pcard-img">
            </div>
            <div class="pcard-name">HARLEY-DAVIDSON<br>X440</div>
            <div class="pcard-qty-badge">1 WINNER</div>
          </div>
        </div>
      </a>

      <!-- MEGA PRIZE -->
      <a class="pcard-wrap rank1-card" href="prize.html?prize=1">
        <div class="pcard">
          <div class="pcard-body">
            <div class="pcard-rank-badge rank-other">MEGA PRIZE</div>
            <div class="pcard-img-wrap">
               <div class="pcard-img-glow"></div>
               <img src="../prize_pictures/Bullet 1.png" alt="Royal Enfield Bike" class="pcard-img">
            </div>
            <div class="pcard-name">ROYAL ENFIELD BIKE</div>
            <div class="pcard-qty-badge">2 WINNERS</div>
          </div>
        </div>
      </a>

      <!-- 3RD PRIZE -->
      <a class="pcard-wrap rank2-card" href="prize.html?prize=2">
        <div class="pcard">
          <div class="pcard-body">
            <div class="pcard-rank-badge rank-other">3RD PRIZE</div>
            <div class="pcard-img-wrap">
               <div class="pcard-img-glow"></div>
               <img src="../prize_pictures/Cash counting 1.png" alt="Cash Counting Machine" class="pcard-img">
            </div>
            <div class="pcard-name">CASH COUNTING<br>MACHINE</div>
            <div class="pcard-qty-badge">50 WINNERS</div>
          </div>
        </div>
      </a>

      <!-- 4TH PRIZE -->
      <a class="pcard-wrap rank3-card" href="prize.html?prize=3">
        <div class="pcard">
          <div class="pcard-body">
            <div class="pcard-rank-badge rank-other">4TH PRIZE</div>
            <div class="pcard-img-wrap">
               <div class="pcard-img-glow"></div>
               <img src="../prize_pictures/Safe 1.png" alt="Godrej Safe" class="pcard-img">
            </div>
            <div class="pcard-name">GODREJ SAFE</div>
            <div class="pcard-qty-badge">100 WINNERS</div>
          </div>
        </div>
      </a>

      <!-- 5TH PRIZE -->
      <a class="pcard-wrap rankc-card" href="prize.html?prize=4">
        <div class="pcard">
          <div class="pcard-body">
            <div class="pcard-rank-badge rank-other">5TH PRIZE</div>
            <div class="pcard-img-wrap">
               <div class="pcard-img-glow"></div>
               <img src="../prize_pictures/Chair 1.png" alt="Orthopedic Chair" class="pcard-img">
            </div>
            <div class="pcard-name">ORTHOPEDIC CHAIR<br>BACK SUPPORT</div>
            <div class="pcard-qty-badge">200 WINNERS</div>
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

print("Updated index.html layout to match reference image.")
