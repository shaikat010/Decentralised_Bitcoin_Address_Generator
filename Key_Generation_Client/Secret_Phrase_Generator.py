import hashlib

def generate_int_from_random(random_value):
    random_bytes = str(random_value).encode('utf-8')
    hash_object = hashlib.sha256()
    hash_object.update(random_bytes)

    hash_hex = hash_object.hexdigest()

    generated_int = int(hash_hex,16)

    return generated_int



