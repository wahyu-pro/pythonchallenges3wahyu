from simplecrypt import encrypt, decrypt
class Cipher:
    @staticmethod
    def encrypt(arg1, arg2):
        password =  arg2
        message = arg1
        ciphertext = encrypt(password, message)
        return ciphertext
    
    @staticmethod
    def decrypt(arg1, message):
        chip = decrypt(arg1, message)
        return chip


message = Cipher.encrypt('p4$$w0rd', 'Ini tulisan rahasia')
print(message)
decryptedMessage = Cipher.decrypt('p4$$w0rd', message)
print(decryptedMessage)
