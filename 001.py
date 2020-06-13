import hashlib
class Hash:
    @staticmethod
    def md5(arg):
        text = arg
        textUtf8 = text.encode("utf-8")
        hash = hashlib.md5(textUtf8)
        hexa = hash.hexdigest()
        print(hexa)

    @staticmethod
    def sha1(arg):
        text = arg
        textUtf8 = text.encode("utf-8")
        hash = hashlib.sha1(textUtf8)
        hexa = hash.hexdigest()
        print(hexa)

    @staticmethod
    def sha256(arg):
        text = arg
        textUtf8 = text.encode("utf-8")
        hash = hashlib.sha256(textUtf8)
        hexa = hash.hexdigest()
        print(hexa)

    @staticmethod
    def sha512(arg):
        text = arg
        textUtf8 = text.encode("utf-8")
        hash = hashlib.sha512(textUtf8)
        hexa = hash.hexdigest()
        print(hexa)


Hash.md5('secret')
Hash.sha1('secret')
Hash.sha256('secret')
Hash.sha512('secret')
