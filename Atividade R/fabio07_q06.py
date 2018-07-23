def main():
    binario = input().split()
    int_binario = tranforma_str_int(binario)
    print(decimal(int_binario))
    # print(hexadecimal(50))


def tranforma_str_int(binario):
    for i in range(len(binario)):
        binario[i] = int(binario[i])
    return binario


def decimal(binario):
    r = 0
    for i in range(len(binario)):
        r += binario[i]*(2**i)
    return r


# def hexadecimal(decimal):
#     cociente = []
#     n = decimal
#     while True:
#         if n%16 != 0:
#             n = n/16
#             print(n)
#         else:
#             return cociente


if __name__ == '__main__':
    main()
