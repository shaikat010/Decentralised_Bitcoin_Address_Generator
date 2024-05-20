import socket
import random
import rsa
import RSA_encrypt_decrypt

all_keys = []

with open("key_store.txt", 'r') as file:
    for line in file:
        # Removes the newline and appends the line to the list
        cleaned_line = line.strip()
        all_keys.append(cleaned_line)

print(all_keys)


def choose_key(key_list):
    size = len(key_list)
    index = random.randint(0, size)
    return key_list[index]


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12348))
server_socket.listen(5)

while True:
    print("Waiting for the connection from the OTP Requesting Client....")
    connection,client_address = server_socket.accept()
    print("Connected to",client_address)

    public_key_bytes_received = connection.recv(1024)

    print(public_key_bytes_received)

    received_public_key = rsa.PublicKey.load_pkcs1(public_key_bytes_received)

    print("Sending the OTP to the Requesting Client...............................")

    OTP = choose_key(all_keys)

    encrypted_OTP_data = RSA_encrypt_decrypt.encrypt(OTP,received_public_key)

    print("This is the encrypted OTP data: ")
    print(encrypted_OTP_data)

    connection.send(encrypted_OTP_data)

    connection.close()