# This is the key generation server

import socket
import rsa
import Generate_Server_Keys
import RSA_encrypt_decrypt
import Response_Phrase_Generation

public_key,private_key = RSA_encrypt_decrypt.loadkeys()

public_key_bytes = public_key.save_pkcs1(format="PEM")
private_key_bytes = private_key.save_pkcs1(format="PEM")

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(5)

while True:
    print("Waiting for Connection.......")
    connection,client_address = server_socket.accept()
    print(f'Connected to {client_address}')
    print("Connected Successfully ..... !!!!")

    connection.sendall(public_key_bytes)

    received_encrypted_data = connection.recv(4096)
    print("This is the encrypted response phrase from the Key Generation Client: ")
    print(received_encrypted_data)

    decrypted_secret_phrase = RSA_encrypt_decrypt.decrypt(received_encrypted_data,private_key)

    print("This is the decrypted response phrase from the Key Generation Client:")
    print(decrypted_secret_phrase)

    response_secret_otp = Response_Phrase_Generation.generate_int_from_random(decrypted_secret_phrase)

    with open("key_store.txt",'a') as file:
        file.write(str(response_secret_otp ) + "\n")

    print("The OTP has been added to the key_store.....")

    connection.close()


