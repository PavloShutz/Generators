import random


def define_number():
    """function yield a number till it wouldn't be equal to a generated number"""
    generated_number = random.randint(1, 101)
    while True:
        guess = random.randint(1, 101)
        if guess == generated_number:
            yield guess
            break
        yield guess
