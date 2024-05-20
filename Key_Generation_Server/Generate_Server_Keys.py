import rsa

def generate_server_keys():
    public_key, private_key = rsa.newkeys(1024)
    print(public_key)
    print(private_key)
    with open("public_key_Server.pem", 'wb') as p:
        p.write(public_key.save_pkcs1('PEM'))
    with open("private_key_Server.pem", 'wb') as p:
        p.write(private_key.save_pkcs1('PEM'))

generate_server_keys()

