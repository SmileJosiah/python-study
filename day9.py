import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(*, code_len=4):
    return ''.join(random.choices(ALL_CHARS, k=code_len))


def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True







if __name__ == '__main__':
    print(generate_code(code_len=16))
    print(is_prime(6))
