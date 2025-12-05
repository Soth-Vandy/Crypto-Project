# Steganography Project

A Python-based steganography tool that allows you to hide secret messages inside images and extract them later. This project includes scripts to encrypt (embed) and decrypt (extract) text from image files using basic image manipulation techniques.

---

## 📁 Project Structure
```
Steganography-Project/
├── main.py                 
├── Encrypted.py            # Handles embedding text into images
├── Decrypted.py            # Handles extracting text from images
├── Encrypted-Images/       # Output folder for encoded images
   └── encod.png            # result image encoded

---

## 🚀 Features
- Make GUI for user easy to use
- Base on AES encryption for secret message

---

## 🛠️ Requirements
Make sure you have **Python 3.10+** installed.

Install required dependencies:
```bash
pip install pillow
```

---

## ▶️ Usage

### **1. Encode a Message**
Run the encryption script to hide a message inside an image:
```bash
python Encrypted.py
```
Follow the prompts to select:
- Input image
- Output filename
- Message to hide

---

### **2. Decode a Message**
Run the decryption script to extract the hidden message:
```bash
python Decrypted.py
```
Choose the encoded image, and the program will reveal the hidden text.

---

## 📌 main.py
The `main.py` file acts as a controller that ties together the encryption and decryption components. You can modify it to add a GUI, enhance automation, or integrate advanced steganography techniques.

---

## 📜 License
This project is open-source. You may modify or distribute it as needed.

---

## 🤝 Contributing
Feel free to submit issues or pull requests to improve functionality.

---

## 📧 Contact
contact me at:
```
Sothvandy8399@gmail.com
```

