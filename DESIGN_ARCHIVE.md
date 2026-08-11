# Design History Archive

This document serves as a reference for the previous design states ("Original" and "Pro") that were used prior to consolidating the application onto the single "Blue Laser Stage" design. 

If you ever wish to revert to or reuse these designs in the future, you can copy the relevant CSS snippets below and replace the current `.stage` background elements in `index.html` and `prize.html`.

---

## 1. The "Original" Design (Radial Gradient & Lasers)

This was the first design, featuring a deep blue radial gradient background with spinning criss-cross laser rays.

### Background CSS:
```css
/* ── BACKGROUND ── */
.hero-bg {
  position: absolute; inset: 0; z-index: 0;
  background: radial-gradient(ellipse 100% 80% at 50% 20%, #4B4F71 0%, #222856 35%, #111838 70%, #0A0D20 100%);
}
.hero-bg::before { display: none; }
.hero-bg::after {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(ellipse 100% 100% at 50% 50%, transparent 40%, rgba(0,0,0,0.55) 100%);
}

/* ── SPOTLIGHTS & RAYS ── */
.rays { position: absolute; inset: 0; z-index: 1; overflow: hidden; pointer-events: none; }
.rays::before {
  content: ''; position: absolute; top: 0; left: 50%; width: 280%; height: 280%;
  transform: translate(-50%, -30%);
  background: conic-gradient(from 0deg, transparent 0deg, rgba(255,215,0,0.15) 3deg, transparent 6deg, transparent 20deg, rgba(255,215,0,0.10) 23deg, transparent 26deg, transparent 40deg, rgba(255,215,0,0.15) 43deg, transparent 46deg, transparent 60deg, rgba(255,215,0,0.10) 63deg, transparent 66deg, transparent 80deg, rgba(255,215,0,0.15) 83deg, transparent 86deg, transparent 100deg, rgba(255,215,0,0.10) 103deg, transparent 106deg, transparent 120deg, rgba(255,215,0,0.15) 123deg, transparent 126deg, transparent 140deg, rgba(255,215,0,0.10) 143deg, transparent 146deg, transparent 160deg, rgba(255,215,0,0.15) 163deg, transparent 166deg, transparent 180deg, rgba(255,215,0,0.10) 183deg, transparent 186deg, transparent 200deg, rgba(255,215,0,0.15) 203deg, transparent 206deg, transparent 220deg, rgba(255,215,0,0.10) 223deg, transparent 226deg, transparent 240deg, rgba(255,215,0,0.15) 243deg, transparent 246deg, transparent 260deg, rgba(255,215,0,0.10) 263deg, transparent 266deg, transparent 280deg, rgba(255,215,0,0.15) 283deg, transparent 286deg, transparent 300deg, rgba(255,215,0,0.10) 303deg, transparent 306deg, transparent 320deg, rgba(255,215,0,0.15) 323deg, transparent 326deg, transparent 340deg, rgba(255,215,0,0.10) 343deg, transparent 346deg, transparent 360deg);
  animation: spinRays 80s linear infinite;
}
@keyframes spinRays { to { transform: translate(-50%, -30%) rotate(360deg); } }
```

### HTML Structure:
```html
<div class="hero-bg"></div>
<div class="rays"></div>
```

---

## 2. The "Pro" Design (Vibrant Image Background)

This was the premium, high-resolution aesthetic design utilizing the `vibrant_bg.png` asset.

### Background CSS:
```css
/* ── BACKGROUND ── */
.hero-bg {
  position: absolute; inset: 0; z-index: 0;
  background-image: url('assets/images/vibrant_bg.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.hero-bg::before, .hero-bg::after { display: none; }
.rays { display: none; }
```

### HTML Structure:
```html
<div class="hero-bg"></div>
```

---

## 3. The 3-Way UI Toggle Switch

If you ever wish to re-implement the multi-state architecture where users can toggle between different designs dynamically, you can inject this UI component into the `<body>` of your HTML files.

### Toggle CSS:
```css
/* ── 3-WAY DESIGN TOGGLE ── */
.design-toggle {
  position: fixed; top: 20px; right: 20px; z-index: 1000; display: flex;
  background: rgba(0, 0, 0, 0.5); border-radius: 30px; border: 1px solid rgba(255, 215, 0, 0.3);
  backdrop-filter: blur(5px); padding: 4px; overflow: hidden;
}
.design-toggle button {
  background: transparent; border: none; color: rgba(255, 255, 255, 0.5);
  padding: 6px 14px; font-family: 'Barlow Condensed', sans-serif; font-weight: 700;
  letter-spacing: 1px; cursor: pointer; border-radius: 26px; transition: all 0.3s ease;
  font-size: 14px;
}
.design-toggle button:hover { color: #fff; }
.design-toggle button.active {
  background: rgba(255, 215, 0, 0.3); color: #fff; box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
}
```

### Toggle HTML & JS Logic:
```html
<div class="design-toggle">
  <button onclick="switchTheme('original')" class="active">ORIGINAL</button>
  <button onclick="switchTheme('stage')">STAGE</button>
  <button onclick="switchTheme('pro')">PRO</button>
</div>
<script>
function switchTheme(theme) {
  const isPrize = window.location.pathname.includes('prize');
  const p = new URLSearchParams(window.location.search).get('prize') || 0;
  let target = '';
  
  if (theme === 'original') target = isPrize ? 'prize.html' : 'index.html';
  if (theme === 'stage') target = isPrize ? 'prize-stage.html' : 'index-stage.html';
  if (theme === 'pro') target = isPrize ? 'prize-pro.html' : 'index-pro.html';
  
  if (isPrize) target += '?prize=' + p;
  window.location.href = target;
}
</script>
```

*(To use the toggle, you must duplicate `index.html` and `prize.html` into corresponding files like `index-pro.html` and `index-stage.html`, adjusting the active button class and background CSS in each.)*
