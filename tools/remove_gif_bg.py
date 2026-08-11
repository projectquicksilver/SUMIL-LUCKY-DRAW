from PIL import Image

def remove_bg(gif_path, out_path):
    img = Image.open(gif_path)
    frames = []
    
    # Try to find the background color from the first pixel
    bg_color = None
    
    try:
        while True:
            frame = img.copy().convert("RGBA")
            if bg_color is None:
                # get color of top left pixel
                bg_color = frame.getpixel((0, 0))
            
            # Make the background color transparent
            newData = []
            for item in frame.getdata():
                # If the pixel is close to the background color, make it transparent
                # Simple exact match (with some tolerance for compression artifacts)
                if abs(item[0] - bg_color[0]) < 15 and abs(item[1] - bg_color[1]) < 15 and abs(item[2] - bg_color[2]) < 15:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)
            
            frame.putdata(newData)
            frames.append(frame)
            img.seek(img.tell() + 1)
    except EOFError:
        pass

    # Save as new gif
    frames[0].save(out_path, save_all=True, append_images=frames[1:], loop=0, duration=img.info.get('duration', 100), disposal=2)

remove_bg('/Users/ankush/Desktop/Sumil Lucky Draw/Spin_this_wheel.gif', '/Users/ankush/Desktop/Sumil Lucky Draw/Spin_this_wheel_transparent.gif')
print("GIF processed!")
