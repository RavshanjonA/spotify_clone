import string
import random

def generate_token(n=30):
    return "".join((random.choice(string.ascii_letters+string.digits) for _ in range(n)))

if __name__ == '__main__':
    print(generate_token(70))