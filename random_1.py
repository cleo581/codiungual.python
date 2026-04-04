import random
import string

characters = string.ascii_letters + string.digits
length = 8

password = []

for i in range(length):
    password.append(random.choice(characters))

random.shuffle(password)

password = "".join(password)

print("Generated password:", password)