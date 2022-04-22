from random import randint


def generate_random_of_ten_thousand():
    for _ in range(10000):
        random_number = randint(0, 10001)
        yield random_number ** 2


nums = generate_random_of_ten_thousand()
first = open('1st', 'a')
second = open('2nd', 'a')
third = open('3nd', 'a')

for i in nums:
    if i % 3 == 0:
        first.write(f"{i}\n")
    elif i % 5 == 0:
        second.write(f"{i}\n")
    elif i % 2 == 0:
        third.write(f"{i}\n")

first.close()
second.close()
third.close()
