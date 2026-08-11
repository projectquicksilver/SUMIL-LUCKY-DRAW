import os

target_dir = '/Users/ankush/Desktop/Sumil Lucky Draw/refer'
index_file = os.path.join(target_dir, 'index.html')

with open(index_file, 'r') as f:
    content = f.read()

# 1. Add CSS keyframes before </style>
keyframes_css = """
/* Granulam Podium Animation */
@keyframes granulamCelebrate {
  0% { transform: translateY(-50%) rotate(0deg) scale(1); filter: drop-shadow(0 0 10px rgba(255,215,0,0.3)); }
  25% { transform: translateY(-55%) rotate(5deg) scale(1.05); filter: drop-shadow(0 0 20px rgba(255,215,0,0.6)); }
  50% { transform: translateY(-50%) rotate(0deg) scale(1.1); filter: drop-shadow(0 0 30px rgba(255,215,0,0.8)); }
  75% { transform: translateY(-45%) rotate(-5deg) scale(1.05); filter: drop-shadow(0 0 20px rgba(255,215,0,0.6)); }
  100% { transform: translateY(-50%) rotate(0deg) scale(1); filter: drop-shadow(0 0 10px rgba(255,215,0,0.3)); }
}
"""

if "granulamCelebrate" not in content:
    content = content.replace("</style>", keyframes_css + "\n</style>")

# 2. Update the HTML to wrap title-banner and add the new image
old_banner_html = """    <!-- TITLE BANNER at the top -->
    <img src="../main_banner.png" alt="Main Banner" class="title-banner" style="height: 48vh; width: 100%; object-fit: contain; margin-top: 5px;">"""

new_banner_html = """    <!-- BANNER CONTAINER -->
    <div style="position: relative; width: 100%; display: flex; justify-content: center; align-items: center; margin-top: 5px;">
      
      <!-- TITLE BANNER -->
      <img src="../main_banner.png" alt="Main Banner" class="title-banner" style="height: 48vh; width: 100%; max-width: 1200px; object-fit: contain; z-index: 2;">
      
      <!-- GRANULAM PODIUM -->
      <img src="../granulam_podium.png" alt="Granulam Podium" style="position: absolute; right: 5%; top: 50%; height: 38vh; object-fit: contain; z-index: 3; animation: granulamCelebrate 8s infinite ease-in-out;">
      
    </div>"""

content = content.replace(old_banner_html, new_banner_html)

with open(index_file, 'w') as f:
    f.write(content)

print("Added Granulam Podium and animations successfully.")
