def main():
    nome = input()
    nome_list = nome.split()
    print("{}, {}. {}..".format(nome_list[len(nome_list) - 1], nome_list[0][0].upper(), nome_list[1][0].upper()))


if __name__ == '__main__':
    main()