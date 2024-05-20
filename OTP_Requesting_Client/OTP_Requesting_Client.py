import socket
import RSA_encrypt_decrypt
from bitcoin_address_generator import generate_bitcoin_address

public_key, private_key = RSA_encrypt_decrypt.loadkeys()

public_key_bytes = public_key.save_pkcs1(format='PEM')
private_key_bytes = private_key.save_pkcs1(format='PEM')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12348))

client_socket.sendall(public_key_bytes)

encrypted_otp_data = client_socket.recv(1024)

decrypted_otp = RSA_encrypt_decrypt.decrypt(encrypted_otp_data, private_key)

print("This is the received OTP value:")
print(decrypted_otp)

# Using the decrypted OTP to generate the bitcoin address
address_info = generate_bitcoin_address(decrypted_otp[0:32])
print(address_info)
print(type(address_info))
print(f"Private_key_raw': {address_info['private_key']}")
print(f"Private Key: {address_info['private_key_hex']}")
print(f"WIF: {address_info['WIF']}")
print(f"Public Key: {address_info['public_key']}")
print(f"Compressed Public Key: {address_info['compressed_public_key']}")
print(f"P2PKH Address: {address_info['p2pkh_address']}")
print(f"Compressed P2PKH Address: {address_info['compressed_p2pkh_address']}")
print(f"P2SH Address: {address_info['p2sh_address']}")
print(f"Bech32 Address: {address_info['bech32_address']}\n")
