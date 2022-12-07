import time
from main import rabin_karp_search


def main():
    with open("resources/text1.txt") as file:
        text1 = file.readline()
    with open("resources/text2.txt") as file:
        text2 = file.readline()
    with open("resources/text3.txt") as file:
        text3 = file.readline()

    start_time = time.perf_counter()
    res = rabin_karp_search(text1, 'raw')
    print(f'Best case took {(time.perf_counter() - start_time) * 10 ** 3} ms')
    print(res)
    start_time = time.perf_counter()
    res = rabin_karp_search(text2, 'hi')
    print(f'Average case took {(time.perf_counter() - start_time) * 10 ** 3} ms')
    print(res)
    start_time = time.perf_counter()
    res = rabin_karp_search(text3, 'adb')
    print(f'Worst case took {(time.perf_counter() - start_time) * 10 ** 3} ms')
    print(res)


if __name__ == '__main__':
    main()
