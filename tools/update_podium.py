import os
import re

target_dir = '/Users/ankush/Desktop/Sumil Lucky Draw/refer'
index_file = os.path.join(target_dir, 'index.html')

with open(index_file, 'r') as f:
    content = f.read()

# 1. Update CSS keyframes for glow and add falling celebration CSS
old_css = """/* Granulam Podium Animation */
@keyframes granulamCelebrate {
  0%, 100% { transform: translateY(-50%) scale(1); }
  50% { transform: translateY(-50%) scale(1.08); }
}"""

new_css = """/* Granulam Podium Animation & Glow */
@keyframes granulamCelebrate {
  0%, 100% { transform: scale(1); filter: drop-shadow(0 0 8px rgba(255,215,0,0.5)); }
  50% { transform: scale(1.08); filter: drop-shadow(0 0 25px rgba(255,215,0,0.9)); }
}

/* Localized Falling Celebration */
.podium-wrapper {
  position: absolute; right: 0%; top: 50%; transform: translateY(-50%);
  height: 25vh; width: 20vw; z-index: 3;
  display: flex; justify-content: center; align-items: center;
}
.falling-star {
  position: absolute; top: -20%;
  width: 6px; height: 12px;
  background: #FFD700;
  border-radius: 2px;
  opacity: 0;
  animation: fallDown 2s infinite linear;
  z-index: 4;
}
@keyframes fallDown {
  0% { transform: translateY(0) rotate(0deg); opacity: 1; }
  100% { transform: translateY(30vh) rotate(360deg); opacity: 0; }
}"""

content = content.replace(old_css, new_css)

# 2. Replace the img tag with the wrapper
old_html = """      <!-- GRANULAM PODIUM -->
      <img src="../granulam_podium.png" alt="Granulam Podium" style="position: absolute; right: 0%; top: 50%; height: 22vh; object-fit: contain; z-index: 3; animation: granulamCelebrate 4s infinite ease-in-out;">"""

new_html = """      <!-- GRANULAM PODIUM -->
      <div class="podium-wrapper">
        <!-- Falling celebration particles over the podium -->
        <div class="falling-star" style="left: 20%; animation-delay: 0.1s; background: #FF3B3B;"></div>
        <div class="falling-star" style="left: 50%; animation-delay: 0.8s; background: #FFD700;"></div>
        <div class="falling-star" style="left: 80%; animation-delay: 1.5s; background: #4caf50;"></div>
        <div class="falling-star" style="left: 35%; animation-delay: 0.4s; background: #FF9060;"></div>
        <div class="falling-star" style="left: 65%; animation-delay: 1.1s; background: #FFD966;"></div>
        
        <img src="../granulam_podium.png" alt="Granulam Podium" style="height: 90%; width: 90%; object-fit: contain; animation: granulamCelebrate 4s infinite ease-in-out;">
      </div>"""

content = content.replace(old_html, new_html)

with open(index_file, 'w') as f:
    f.write(content)

print("Added glowing effect and falling celebration.")
