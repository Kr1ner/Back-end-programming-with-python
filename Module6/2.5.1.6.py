def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

while True:
    try:
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter a shift value (1-25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Shift value must be between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("Encrypted text:", caesar_cipher_encrypt(text, shift))
