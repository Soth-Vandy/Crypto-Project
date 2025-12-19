import sys
from Encrypted import encode_image
from Decrypted import decode_image
import pyfiglet
def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print('  Encrypt: py main.py hide "cover message "secret message" pic.png secret.png')
        print("  Decrypt: py main.py reveal secret.png")
        return

    command = sys.argv[1].lower()

    if command == "hide":
        if len(sys.argv) != 6:
            print('Usage: py main.py hide "cover message "secret message" pic.png secret.png')
            return
        cover_text = sys.argv[2]
        payload_text = sys.argv[3]
        image_path = sys.argv[4]
        output_path = sys.argv[5]
        encode_image(image_path, cover_text, payload_text, output_path)

    elif command == "reveal":
        if len(sys.argv) != 3:
            print('Usage: py main.py reveal image.png')
            return
        image_path = sys.argv[2]
        decode_image(image_path)

    else:
        print("Unknown command. Use 'hide' or 'reveal'.")

def Banner():
    banner = pyfiglet.figlet_format("Image-Stega")
    print(banner)
    print("                 hide secret message in image                    ")
    print("---------------------------------------------------------------\n")


        

if __name__ == "__main__":
    Banner()
    main()
