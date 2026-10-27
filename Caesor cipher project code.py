from cryptography.fernet import Fernet
import codecs

# ---------------- Caesar Cipher ---------------- #

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-start+shift)%26+start)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# ---------------- Vigenere Cipher ---------------- #

def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-start+shift)%26+start)
            key_index += 1
        else:
            result += char

    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-start-shift)%26+start)
            key_index += 1
        else:
            result += char

    return result


# ---------------- Atbash Cipher ---------------- #

def atbash(text):
    result = ""

    for c in text:
        if c.isupper():
            result += chr(90 - (ord(c)-65))
        elif c.islower():
            result += chr(122 - (ord(c)-97))
        else:
            result += c

    return result


# ---------------- ROT13 ---------------- #

def rot13(text):
    return codecs.encode(text, 'rot_13')


# ---------------- XOR Cipher ---------------- #

def xor_encrypt(text, key):
    return ''.join(chr(ord(c)^key) for c in text)


def xor_decrypt(text, key):
    return ''.join(chr(ord(c)^key) for c in text)


# ---------------- Fernet Encryption ---------------- #

fernet_key = Fernet.generate_key()
cipher = Fernet(fernet_key)

def fernet_encrypt(text):
    return cipher.encrypt(text.encode()).decode()

def fernet_decrypt(text):
    return cipher.decrypt(text.encode()).decode()


# ---------------- Main Menu ---------------- #

while True:

    print("\n========== Encryption Tool ==========")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. Atbash Cipher")
    print("4. ROT13")
    print("5. XOR Cipher")
    print("6. Fernet (AES Based)")
    print("7. Exit")

    choice = input("\nChoose Algorithm: ")

    if choice == "7":
        break

    text = input("Enter Text: ")

    if choice == "1":
        shift = int(input("Shift: "))
        enc = caesar_encrypt(text, shift)
        print("Encrypted :", enc)
        print("Decrypted :", caesar_decrypt(enc, shift))

    elif choice == "2":
        key = input("Key: ")
        enc = vigenere_encrypt(text, key)
        print("Encrypted :", enc)
        print("Decrypted :", vigenere_decrypt(enc, key))

    elif choice == "3":
        enc = atbash(text)
        print("Encrypted :", enc)
        print("Decrypted :", atbash(enc))

    elif choice == "4":
        enc = rot13(text)
        print("Encrypted :", enc)
        print("Decrypted :", rot13(enc))

    elif choice == "5":
        key = int(input("Numeric Key: "))
        enc = xor_encrypt(text, key)
        print("Encrypted :", enc)
        print("Decrypted :", xor_decrypt(enc, key))

    elif choice == "6":
        enc = fernet_encrypt(text)
        print("Encrypted :", enc)
        print("Decrypted :", fernet_decrypt(enc))

    else:
        print("Invalid Choice")