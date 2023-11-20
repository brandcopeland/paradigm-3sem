import random

def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    # Пример использования:
    random_numbers = list(gen_random(5, 1, 3))
    print(random_numbers)