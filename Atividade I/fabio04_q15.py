def main():
    numero = int(input())
    print(decbinario(numero))
    print(dechexadecimal(numero))

def decbinario(n):
    b = ''
    while n != 0:
        b = b + str(n % 2)
        n = int(n / 2)
    return b[::-1]


def dechexadecimal(n):
    b = ''
    while n != 0:
        b = b + str(n % 16)
        n = int(n / 16)
    return b


if __name__ == '__main__':
    main()
