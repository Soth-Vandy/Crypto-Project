from PIL import Image

def decode_image(image_path):
    """
    Decode hidden data from an image using LSB method.
    """
    img = Image.open(image_path).convert("RGB")
    binary_data = ""
    width, height = img.size

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            binary_data += str(r & 1)

    # Convert binary to text
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded_text = ""
    for byte in all_bytes:
        decoded_text += chr(int(byte, 2))
        if decoded_text.endswith("<END>"):
            break

    if "<SEP>" in decoded_text:
        cover_text, payload_text = decoded_text.split("<SEP>")
        payload_text = payload_text.replace("<END>", "")
        cover_text = cover_text
    else:
        cover_text, payload_text = decoded_text, ""

    print(f"Cover Text : {cover_text}")
    print(f"Payload    : {payload_text}")
    return cover_text, payload_text
