# 🖼️ Image Steganography -- Cover & Payload Text

## 📌 Overview

This project implements **image-based steganography** using the **Least
Significant Bit (LSB)** technique. It allows hiding two types of text
inside an image:

-   **Cover Text** -- looks harmless and normal
-   **Payload Text** -- the secret hidden message (CTF flag)

The hidden data can later be **revealed from the image**, making this
tool suitable for **CTF challenges**, **learning steganography**, and
**security demonstrations**.

------------------------------------------------------------------------

## 🎯 Features

-   Add GUI interface
-   Support audio and video steganography
-   Command-line based (Kali Linux)

------------------------------------------------------------------------

## 📁 Project Structure

    Steganography-Project/
    │── main.py
    │── Encrypted.py
    │── Decrypted.py
    │── Reveal.py
    │── README.md

------------------------------------------------------------------------

## 🛠️ Requirements

-   Python 3.x
-   Pillow
-   pyfiglet

Install dependency:

``` bash
pip install pillow
```
```bash
pip install pyfiglet
```
# OR
```bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🚀 Usage

```bash
py main.py     #show help menu
```

### 🔐 Hide Data

``` bash
py main.py hide "cover message" "secret message" pic.png secret.png
```

### 🔓 Reveal Data

``` bash
py main.py reveal secret.png
```

**Example Output**

``` text
Cover Text : Hello my firend! Are you sure?

Payload    : CTF{Mr.robot}
```

------------------------------------------------------------------------

## 🧪 CTF Solver Script (Reveal.py)

``` bash
py Reveal.py
```

This script allows players to extract the hidden message without
installing the full tool.

------------------------------------------------------------------------

## 🧠 How It Works

-   Image converted to RGB
-   Data stored in LSB of red channel
-   Format:

```{=html}
<!-- -->
```
    COVER_TEXT<SEP>PAYLOAD_TEXT<END>

------------------------------------------------------------------------

## 🏴 CTF Difficulty

**Level:** Easy (Beginner)

------------------------------------------------------------------------

## ⚠️ Limitations

-   No encryption
-   Detectable via steganalysis tools
-   Image size limits payload size

------------------------------------------------------------------------

## 🔒 Future Improvements

-   Encrypt payload
-   Password-protected extraction
-   Multi-channel encoding

------------------------------------------------------------------------

## 👨‍💻 Author

**Soth Vandy**\
Cybersecurity & Cryptography Project

------------------------------------------------------------------------

## 📜 License

Educational and CTF use only.
