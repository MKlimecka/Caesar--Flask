KEY =3
POLISH_CHARACTERS = set("ąćęłńóśźż")
message = "".join([c for c in input("message: ").lower() if c.isalpha()])


def caesar_cipher(message, key=KEY):
    encrypted_message=""
    if contains_polish_characters(message):
        alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwxyzźż"
    else:
        alphabet = "abcdefghijklmnoprstuwxyz"
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + key) % len(alphabet)
            encrypted_message += alphabet[new_index]
    return encrypted_message


def contains_polish_characters(message):
    for char in message:
        if char in POLISH_CHARACTERS:
            return True
        return False
    

def caesar_cipher_decypted(message, key=KEY):
    encrypted_message=""
    if contains_polish_characters(message):
        alphabet = "aąbcćdeęfghijklłmnńoóprsśtuwxyzźż"
    else:
        alphabet = "abcdefghijklmnoprstuwxyz"
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - key) % len(alphabet)
            encrypted_message += alphabet[new_index]
    return encrypted_message
    

print(contains_polish_characters(message)) 
print(caesar_cipher(message))
print(caesar_cipher_decypted(caesar_cipher(message)))

