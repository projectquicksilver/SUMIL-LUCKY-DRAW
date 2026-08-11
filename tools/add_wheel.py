import os
import re

target_dir = '/Users/ankush/Desktop/Sumil Lucky Draw/refer'
index_file = os.path.join(target_dir, 'index.html')

with open(index_file, 'r') as f:
    content = f.read()

# We want to add the spinning wheel on the left side of the banner container.
# Currently the container has:
old_banner_html = """      <!-- TITLE BANNER -->
      <img src="../main_banner.png" alt="Main Banner" class="title-banner" style="height: 48vh; width: 100%; max-width: 1200px; object-fit: contain; z-index: 2;">"""

new_banner_html = """      <!-- SPINNING WHEEL (LEFT) -->
      <div class="podium-wrapper" style="right: auto; left: 0%;">
        <!-- Falling celebration particles over the wheel -->
        <div class="falling-star" style="left: 20%; animation-delay: 0.2s; background: #FF3B3B;"></div>
        <div class="falling-star" style="left: 50%; animation-delay: 0.9s; background: #FFD700;"></div>
        <div class="falling-star" style="left: 80%; animation-delay: 1.6s; background: #4caf50;"></div>
        <div class="falling-star" style="left: 35%; animation-delay: 0.5s; background: #FF9060;"></div>
        <div class="falling-star" style="left: 65%; animation-delay: 1.2s; background: #FFD966;"></div>
        
        <img src="../spining_wheel.png" alt="Spinning Wheel" style="height: 90%; width: 90%; object-fit: contain; animation: granulamCelebrate 4s infinite ease-in-out;">
      </div>

      <!-- TITLE BANNER -->
      <img src="../main_banner.png" alt="Main Banner" class="title-banner" style="height: 48vh; width: 100%; max-width: 1200px; object-fit: contain; z-index: 2;">"""

content = content.replace(old_banner_html, new_banner_html)

with open(index_file, 'w') as f:
    f.write(content)

print("Added spinning wheel successfully.")
