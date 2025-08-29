KEY =3
POLISH_ALPHABET = "aąbcćdeęfghijklłmnńoóprsśtuwxyzźż"
STANDARD_ALPHABET = "abcdefghijklmnoprstuwxyz"


def caesar_cipher(message: str, key=KEY, use_polish: bool=False):
    message = "".join([c for c in message.lower() if c.isalpha()])
    encrypted_message=""
    if use_polish:
        alphabet = POLISH_ALPHABET
    else: 
        alphabet = STANDARD_ALPHABET
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + key) % len(alphabet)
            encrypted_message += alphabet[new_index]
    return encrypted_message


def caesar_cipher_decypted(message: str, key=KEY, use_polish: bool=False):
    message = "".join([c for c in message.lower() if c.isalpha()])
    encrypted_message=""
    if use_polish:
        alphabet = POLISH_ALPHABET
    else: 
        alphabet = STANDARD_ALPHABET
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - key) % len(alphabet)
            encrypted_message += alphabet[new_index]
    return encrypted_message
    