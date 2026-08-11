import os

files_to_update = ['index.html', 'prize.html', 'js/audio.js']

replacements = {
    '../main_banner.png': 'assets/images/main_banner.png',
    '../sumil_logo.png': 'assets/images/sumil_logo.png',
    '../granulam.png': 'assets/images/granulam.png',
    '../granulam_podium.png': 'assets/images/granulam_podium.png',
    '../Spin_this_wheel.gif': 'assets/images/Spin_this_wheel.gif',
    '../Spin_this_wheel_transparent.gif': 'assets/images/Spin_this_wheel_transparent.gif',
    '../prize_pictures/': 'assets/prizes/',
    '../qualifier_data/': 'assets/data/',
    'bg_music.mp3': 'assets/audio/bg_music.mp3',
    'applause.mp3': 'assets/audio/applause.mp3',
    'src="audio.js"': 'src="js/audio.js"'
}

for file_path in files_to_update:
    full_path = os.path.join('/Users/ankush/Desktop/Sumil Lucky Draw', file_path)
    if not os.path.exists(full_path):
        continue
    
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Paths updated successfully.")
