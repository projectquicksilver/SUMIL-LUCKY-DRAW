from PIL import Image
from collections import Counter
import sys

def get_dominant_colors(image_path, num_colors=10):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        
        # Resize to speed up processing
        img.thumbnail((200, 200))
        
        pixels = list(img.getdata())
        
        # Filter out near-white and near-black colors to find the actual pack color
        def is_valid_color(r, g, b):
            brightness = sum([r, g, b]) / 3
            # Ignore very dark (black/dark grey) and very bright (white/light grey)
            if brightness < 30 or brightness > 220:
                return False
            # Ignore mostly grey colors
            if max(r,g,b) - min(r,g,b) < 20:
                return False
            return True
            
        valid_pixels = [(r,g,b) for r,g,b in pixels if is_valid_color(r,g,b)]
        
        counts = Counter(valid_pixels)
        for (r, g, b), count in counts.most_common(num_colors):
            print(f"Hex: #{r:02x}{g:02x}{b:02x} - RGB: ({r}, {g}, {b}) - Count: {count}")
    except Exception as e:
        print(f"Error: {e}")

get_dominant_colors('/Users/ankush/Desktop/Sumil Lucky Draw/granulam.png')
