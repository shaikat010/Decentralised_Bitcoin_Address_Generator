import os

private_key = os.urandom(32)

print(private_key)
print(type(private_key))
print(len(private_key))

print(private_key.hex())

print(int(private_key.hex(),16))

new_byte_value = bytes(str(876).encode('utf-8'))
print(type(new_byte_value))
print(len(new_byte_value))

print(new_byte_value)