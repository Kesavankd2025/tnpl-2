from PIL import Image
from collections import Counter
import sys

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

try:
    img_path = r"C:\Users\DELL\.gemini\antigravity\brain\e088611d-702a-4f29-8d43-198149287cc4\uploaded_image_1768209799995.png"
    img = Image.open(img_path)
    # img = img.resize((100, 100)) # Don't resize, take full quality for thin lines
    pixels = list(img.getdata())

    filtered_pixels = []
    for p in pixels:
        if len(p) == 4 and p[3] < 128: continue # Transparent
        if p[0] > 240 and p[1] > 240 and p[2] > 240: continue # White background
        filtered_pixels.append(p[:3])

    if not filtered_pixels:
        print("No dominant colors found")
        sys.exit()

    counts = Counter(filtered_pixels)
    most_common = counts.most_common(20) # Get more to find the orange
    
    print("Dominant Colors Found:")
    for color, count in most_common:
        print(f"{rgb_to_hex(color)} : {count}")

except Exception as e:
    print(f"Error: {e}")
