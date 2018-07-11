def main():
    data = input().split("/")
    mes = int(data[1]) - 1
    meses = ['janeiro', 'fevereiro', 'marco']
    for i in range(len(meses)):
        if mes == i:
            print("{} de {} de {}".format(data[0], meses[i], data[2]))


if __name__ == '__main__':
    main()