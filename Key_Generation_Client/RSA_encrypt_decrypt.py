import rsa

def generateKeys():
    (publicKey,privateKey) = rsa.newkeys(1024)
    with open("public_key.pem",'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open("private_key.pem",'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadkeys():
    with open('public_key.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('private_key.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())

    return publicKey,privateKey

def encrypt(message,key):
    return rsa.encrypt(message.encode('ascii'),key)

def decrypt(ciphertext,key):
    try:
        return rsa.decrypt(ciphertext,key).decode('ascii')
    except:
        return False


