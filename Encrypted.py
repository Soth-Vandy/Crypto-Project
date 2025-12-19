from PIL import Image

def encode_image(image_path, cover_text, payload_text, output_path):
    """
    Encode cover_text and payload_text into an image using LSB method.
    """
    img = Image.open(image_path).convert("RGB")
    encoded = img.copy()
    width, height = img.size

    secret_data = cover_text + "<SEP>" + payload_text + "<END>"
    binary = ''.join(format(ord(c), "08b") for c in secret_data)

    index = 0
    for y in range(height):
        for x in range(width):
            if index < len(binary):
                r, g, b = img.getpixel((x, y))
                r = (r & ~1) | int(binary[index])
                encoded.putpixel((x, y), (r, g, b))
                index += 1
            else:
                encoded.save(output_path)
                print(f"[+] Data successfully embedded into {output_path}\n")
                return

    print("[-] Image too small to hold data\n")
