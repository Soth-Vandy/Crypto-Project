from PIL import Image

def encode_image(image_path, message, output_path):
    # Convert ANY image to standard RGB
    img = Image.open(image_path).convert("RGB")
    encoded = img.copy()
    width, height = img.size
    index = 0

    # Add end marker so we know where message stops
    message += "<END>"
    binary_message = ''.join(format(ord(ch), "08b") for ch in message)

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                r, g, b = img.getpixel((col, row))
                
                # set LSB of red channel
                r = (r & ~1) | int(binary_message[index])
                encoded.putpixel((col, row), (r, g, b))

                index += 1
            else:
                encoded.save(output_path)
                print("Message hidden successfully in:", output_path)
                return

    print("Message too large for this image.")
