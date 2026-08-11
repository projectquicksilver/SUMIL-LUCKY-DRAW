import os
from PIL import Image

def optimize_images(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                original_size = os.path.getsize(file_path)
                
                # Only bother if the file is > 500KB
                if original_size > 500 * 1024:
                    try:
                        with Image.open(file_path) as img:
                            # Calculate new dimensions (max width/height 1200)
                            max_dim = 1200
                            if img.width > max_dim or img.height > max_dim:
                                ratio = min(max_dim / img.width, max_dim / img.height)
                                new_size = (int(img.width * ratio), int(img.height * ratio))
                                img = img.resize(new_size, Image.Resampling.LANCZOS)
                            
                            # Save back with optimization
                            img.save(file_path, 'PNG', optimize=True, compress_level=9)
                            
                        new_size = os.path.getsize(file_path)
                        print(f"Optimized {file}: {original_size // 1024}KB -> {new_size // 1024}KB")
                    except Exception as e:
                        print(f"Error optimizing {file}: {e}")

if __name__ == "__main__":
    optimize_images('/Users/ankush/Desktop/Sumil Lucky Draw/assets/images')
    optimize_images('/Users/ankush/Desktop/Sumil Lucky Draw/assets/prizes')
    print("Done!")
