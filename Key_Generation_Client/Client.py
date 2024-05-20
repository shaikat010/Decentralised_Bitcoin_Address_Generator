import rsa
import socket
import RSA_encrypt_decrypt
from Secret_Phrase_Generator import generate_int_from_random

server_ip = '127.0.0.1'
server_port = 12345

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((server_ip,server_port))

public_key_bytes_received = sock.recv(4096)

# byte --> normal
received_public_key = rsa.PublicKey.load_pkcs1(public_key_bytes_received)

print('Received Public Key: ', received_public_key)
print(type(received_public_key))

with open('public_key_Server.pem','wb') as p:
    p.write(received_public_key.save_pkcs1('PEM'))

seed = input("Enter a value: ")
secret_phrase = str(generate_int_from_random(seed))
# print(secret_phrase)

print("This is the secret phrase: " + str(secret_phrase))

encrypted_data = RSA_encrypt_decrypt.encrypt(secret_phrase,received_public_key)
print("This is the secret phrase encrypted data: " + str(encrypted_data))

sock.sendall(encrypted_data)

# Closes the socket
sock.close()

