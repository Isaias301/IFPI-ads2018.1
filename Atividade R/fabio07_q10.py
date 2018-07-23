def main():
    valor = int(input("Digite o valor: "))
    print(fibonaci(valor))


def fibonaci(valor):
    fibonaci=[0,1]
    p=0
    s=1
    for i in range(valor-2):
        t=s+p
        fibonaci += [t]
        p=s
        s=t
    return fibonaci


if __name__ == '__main__':
    main()
