from Encrypted import encode_image
from Decrypted import decode_image
import pyfiglet

def show_banner():
    banner = pyfiglet.figlet_format("Image-Stega")
    print(banner)
    print("                 hide secret message in image                    ")
    print("---------------------------------------------------------------\n")

def main():
    show_banner()
    print("1. Encrypt (hide message in image)")
    print("2. Decrypt (extract message from image)")
    choice = input("Choose option (1/2): ")

    if choice == "1":
        img = input("Enter input image path: ")
        msg = input("Enter secret message: ")
        out = input("Enter output image path (example: encoded.png): ")
        encode_image(img, msg, out)

    elif choice == "2":
        img = input("Enter image path to decrypt: ")
        message = decode_image(img)
        print("Hidden message:", message)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
