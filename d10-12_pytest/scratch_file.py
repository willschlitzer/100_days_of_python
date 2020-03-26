import random


def hello_you(name="Will"):
    return f"Hello {name}"


def get_random_number(start=1, end=20):
    return random.randint(1, 20)


def fizzbuzz():
    """Running fizzbuzz for 1 to 100"""
    for i in range(1, 100):
        answer = ""
        if i % 3 == 0:
            answer += "Fizz"
        if i % 5 == 0:
            answer += "Buzz"
        print(answer or i)


def fizzbuz_input(n):
    if n % 15 == 0:
        return "Fizz Buzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


if __name__ == "__main__":
    fizzbuzz()
