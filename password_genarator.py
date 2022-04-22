import random


def generate_passwords():
    """Password generation"""
    # assigning all possible characters
    all_characters = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_-~,.'
    # in range from 0 to 1001 we are writing generated password into 'password.txt'
    for _ in range(1001):
        # here was used random.sample function to create random password from all characters
        result = ''.join(random.sample(all_characters, random.randint(8, 16)))
        yield result
        with open('passwords.txt', "a") as f:
            f.write(str(result + '\n'))
