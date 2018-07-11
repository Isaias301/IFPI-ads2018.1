def main():
    texto = input()
    old = input("old: ")
    new = input("New: ")
    print(set_replace(texto, old, new))


def set_replace(texto, old, new):
    return texto.replace(old, new)


if __name__ == '__main__':
    main()