import random


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

print('This is the chosen key from the key list')
print(choose_key(all_keys))