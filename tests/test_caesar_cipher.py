from caesar_cipher import caesar_cipher, caesar_cipher_decypted

def test_caesar_cipher_encrypt_and_decrypt():
    message = "Ala ma kota."
    key = 3
    encypted_message = caesar_cipher(message, key, use_polish=False)
    decrypted_message = caesar_cipher_decypted(encypted_message, key, use_polish=False)
    assert decrypted_message == "".join([c for c in message.lower() if c.isalpha()])



def test_caesar_cipher_encrypt_and_decrypt_polish_alphbet():
    message = "zażółć gęślą jaźń"
    key = 3
    encypted_message = caesar_cipher(message, key, use_polish=True)
    decrypted_message = caesar_cipher_decypted(encypted_message, key, use_polish=True)
    assert decrypted_message == "".join([c for c in message.lower() if c.isalpha()])

def test_caesar_cipher_encrypt_and_decrypt_non_leters():
    message = "123 kot 456"
    key = 3
    encypted_message = caesar_cipher(message, key, use_polish=True)
    decrypted_message = caesar_cipher_decypted(encypted_message, key, use_polish=True)
    assert decrypted_message == "".join([c for c in message.lower() if c.isalpha()])