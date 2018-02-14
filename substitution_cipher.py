alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,./;\'[]-=<>?:\"{}_+\| "
key = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*()<>?:\"{}_+,./;\'[]-=|\ "

def encrypt(message):
    
    result = ''

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]


    return result



def decrypt(message):
    result = ''

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]


    return result
    

secret_message = "Encryption is fun"
encrypted_message = encrypt(secret_message)
decrypted_message = decrypt(encrypted_message)

print(decrypted_message)
print(encrypted_message)
