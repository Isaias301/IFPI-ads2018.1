def main():
    a = input().split()
    b = input().split()
    print(junta_vetores(a, b))


# função para juntar os vetores
def junta_vetores(a, b):
    # junta os vetores
    c = a+b
    return c
    # poderia ser simplesmente assim: return a+b ou return c = a+b


if __name__ == '__main__':
    main()
