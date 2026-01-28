from PIL import Image
from collections import Counter
import sys

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

try:
    img_path = r"C:\Users\DELL\.gemini\antigravity\brain\e088611d-702a-4f29-8d43-198149287cc4\uploaded_image_1768209799995.png"
    img = Image.open(img_path)
    pixels = list(img.getdata())

    orange_pixels = []
    for p in pixels:
        if len(p) == 4 and p[3] < 128: continue 
        r, g, b = p[:3]
        # Look for orange-ish: High Red, Medium Green, Low Blue
        if r > 150 and g > 100 and b < 100:
            orange_pixels.append(p[:3])

    if not orange_pixels:
        print("No orange colors found")
    else:
        counts = Counter(orange_pixels)
        most_common = counts.most_common(5)
        print("Dominant Orange Colors Found:")
        for color, count in most_common:
            print(f"{rgb_to_hex(color)} : {count}")

except Exception as e:
    print(f"Error: {e}")
