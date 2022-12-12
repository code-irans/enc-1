import sys
import base64

extra_character = chr(9611)

def secret_code(secret):
    secret_code = 0

    for c in secret:
        secret_code += ord(c)
    
    return secret_code 

def encrypt(plain_text, secret):
    cipher_text = ""
    base64_cipher_text = ""

    for c in plain_text:
        ascii_code = ord(c)
        cipher_text += extra_character + str(int(ascii_code * 2 * 12 / 2 * secret_code(secret))) 

    cipher_text = cipher_text[1:].encode()

    base64_cipher_text = base64.b64encode(cipher_text).decode()

    return base64_cipher_text

def decrypt(cipher_text, secret):
    plain_text = ""
    cipher_text = base64.b64decode(cipher_text.encode()).decode()

    for c in cipher_text.split(extra_character):
        ascii_code = int(int(c) / secret_code(secret) * 2 / 12 / 2)
        plain_text += chr(ascii_code)

    return plain_text

def main(argv, argc):
    if argc == 1:
        sys.exit()

    if argv[1] == "-e": 
        cipher_text = encrypt(argv[2], argv[3])
        print(cipher_text)

    elif argv[1] == "-d":
        plain_text = decrypt(argv[2], argv[3])
        print(plain_text)

if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
