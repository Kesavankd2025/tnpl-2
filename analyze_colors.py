from PIL import Image
from collections import Counter
import sys

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

try:
    img_path = r"C:\Users\DELL\.gemini\antigravity\brain\e088611d-702a-4f29-8d43-198149287cc4\uploaded_image_1768209799995.png"
    img = Image.open(img_path)
    img = img.resize((100, 100))
    pixels = list(img.getdata())

    filtered_pixels = []
    for p in pixels:
        # Check for transparency
        if len(p) == 4 and p[3] < 50:
            continue
        # Check for near-white
        if p[0] > 240 and p[1] > 240 and p[2] > 240:
            continue
        filtered_pixels.append(p[:3])

    if not filtered_pixels:
        print("No dominant colors found (image might be blank or fully transparent)")
        sys.exit()

    counts = Counter(filtered_pixels)
    most_common = counts.most_common(5)
    
    print("Dominant Colors Found:")
    for color, count in most_common:
        print(f"{rgb_to_hex(color)}")

except Exception as e:
    print(f"Error: {e}")
