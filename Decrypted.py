from PIL import Image

def decode_image(image_path):
    # Convert ANY image to RGB to read consistent pixels
    img = Image.open(image_path).convert("RGB")
    width, height = img.size

    binary_data = ""

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_data += str(r & 1)

    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        char = chr(int(byte, 2))
        message += char
        if message.endswith("<END>"):
            return message[:-5]   # remove <END>

    return "No hidden message found."
