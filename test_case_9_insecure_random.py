# Insecure Random Number Example
import random

def generate_password():
    return ''.join(random.choice('abcdef123456') for _ in range(8))

print(generate_password())
