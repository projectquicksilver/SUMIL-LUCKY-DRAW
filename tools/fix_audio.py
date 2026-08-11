import os
import re

filepath = '/Users/ankush/Desktop/Sumil Lucky Draw/js/audio.js'
with open(filepath, 'r') as f:
    content = f.read()

# 1. Update BGM Candidates
old_bgm = """  var BGM_CANDIDATES = [
    'https://raw.githubusercontent.com/projectquicksilver/Shriram_Bioseed-Lucky-Draw/main/assets/audio/bg_music.mp3',
    'assets/audio/bg_music.mp3',
    'https://raw.githubusercontent.com/projectquicksilver/Shriram_Bioseed-Lucky-Draw_playground/main/assets/audio/bg_music.mp3'
  ];"""
new_bgm = """  var BGM_CANDIDATES = [
    'assets/audio/bg_music.mp3'
  ];"""
content = content.replace(old_bgm, new_bgm)

# 2. Update APPLAUSE Candidates
old_app = """  var APPLAUSE_CANDIDATES = [
    'https://raw.githubusercontent.com/projectquicksilver/Shriram_Bioseed-Lucky-Draw/main/assets/audio/applause.mp3',
    'assets/audio/applause.mp3',
    'https://raw.githubusercontent.com/projectquicksilver/Shriram_Bioseed-Lucky-Draw_playground/main/assets/audio/applause.mp3'
  ];"""
new_app = """  var APPLAUSE_CANDIDATES = [
    'assets/audio/applause.mp3'
  ];"""
content = content.replace(old_app, new_app)

# 3. Update the UI widget
ui_pattern = re.compile(r"var css = document\.createElement\('style'\);.*?<span class=\"ld-ico\" style=\"margin-top:-4px;\">🔉</span>';", re.DOTALL)

new_ui = """var css = document.createElement('style');
  css.textContent =
    '#ld-audio-ctl{position:fixed;right:20px;bottom:20px;z-index:900;display:flex;flex-direction:row;align-items:center;gap:12px;' +
      'padding:10px 16px;border-radius:30px;' +
      'background:linear-gradient(160deg,rgba(34,40,86,.88),rgba(17,24,56,.94));' +
      'border:1.5px solid rgba(255,215,0,.45);backdrop-filter:blur(14px);' +
      'box-shadow:0 6px 24px rgba(0,0,0,.6),0 0 18px rgba(255,215,0,.18),inset 0 1px 0 rgba(255,255,255,.15);}' +
    '#ld-play{width:36px;height:36px;border-radius:50%;border:none;cursor:pointer;flex-shrink:0;' +
      'background:linear-gradient(135deg,#FFD700,#FFF4CC);display:flex;align-items:center;justify-content:center;' +
      'box-shadow:0 3px 12px rgba(255,215,0,.5);transition:transform .2s,box-shadow .2s;}' +
    '#ld-play:hover{transform:scale(1.1);box-shadow:0 4px 18px rgba(255,215,0,.8);}' +
    '#ld-play svg{width:16px;height:16px;fill:#020A1A;}' +
    '#ld-vol{-webkit-appearance:none;appearance:none;width:80px;height:6px;border-radius:4px;outline:none;cursor:pointer;' +
      'background:linear-gradient(90deg,#FFD700 var(--p,60%),rgba(255,215,0,.2) var(--p,60%));}' +
    '#ld-vol::-webkit-slider-thumb{-webkit-appearance:none;width:15px;height:15px;border-radius:50%;' +
      'background:radial-gradient(circle at 35% 35%,#FFF3C0,#FFD700 45%,#B8860B);' +
      'box-shadow:0 0 8px rgba(255,210,0,.8);cursor:pointer;}' +
    '#ld-vol::-moz-range-thumb{width:15px;height:15px;border:none;border-radius:50%;' +
      'background:radial-gradient(circle at 35% 35%,#FFF3C0,#FFD700 45%,#B8860B);box-shadow:0 0 8px rgba(255,210,0,.8);cursor:pointer;}' +
    '#ld-audio-ctl .ld-ico{display:flex;align-items:center;justify-content:center;width:18px;height:18px;}' +
    '#ld-audio-ctl .ld-ico svg{width:18px;height:18px;fill:rgba(255,215,0,0.9);filter:drop-shadow(0 0 4px rgba(255,215,0,0.5));}' +
    '@media (max-width:560px){#ld-audio-ctl{right:8px;bottom:8px;padding:8px 12px;}#ld-vol{width:60px;}}';
  document.head.appendChild(css);

  var SVG_PLAY  = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>';
  var SVG_PAUSE = '<svg viewBox="0 0 24 24"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>';
  var SVG_VOL_DOWN = '<svg viewBox="0 0 24 24"><path d="M18.5 12c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM5 9v6h4l5 5V4L9 9H5z"/></svg>';
  var SVG_VOL_UP = '<svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3c0-1.77-1.02-3.29-2.5-4.03v8.05c1.48-.73 2.5-2.25 2.5-4.02zM14 3.23v2.06c2.89.86 5 3.54 5 6.71s-2.11 5.85-5 6.71v2.06c4.01-.91 7-4.49 7-8.77s-2.99-7.86-7-8.77z"/></svg>';

  var wrap = document.createElement('div');
  wrap.id = 'ld-audio-ctl';
  wrap.innerHTML =
    '<button id="ld-play" title="Play / pause music"></button>' +
    '<div class="ld-ico" title="Volume Down">' + SVG_VOL_DOWN + '</div>' +
    '<input id="ld-vol" type="range" min="0" max="100" step="1" title="Volume">' +
    '<div class="ld-ico" title="Volume Up">' + SVG_VOL_UP + '</div>';"""

content = ui_pattern.sub(new_ui, content)

with open(filepath, 'w') as f:
    f.write(content)
print("Updated js/audio.js successfully.")
