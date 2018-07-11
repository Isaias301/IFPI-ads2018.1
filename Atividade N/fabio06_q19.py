def main():
    binario = input()
    res = 0
    for i in range(1, len(binario)):
        for j in binario:
            res += (2*int(j))**i
    print(res)


if __name__ == '__main__':
    main()