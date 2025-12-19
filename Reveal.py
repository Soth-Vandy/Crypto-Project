from PIL import Image

img = Image.open(r"Input Path Image").convert("RGB")
bits = ""

for y in range(img.height):
    for x in range(img.width):
        r, g, b = img.getpixel((x,y))
        bits += str(r & 1)

msg = ""
for i in range(0, len(bits), 8):
    msg += chr(int(bits[i:i+8], 2))
    if "<END>" in msg:
        print(msg)
        break
