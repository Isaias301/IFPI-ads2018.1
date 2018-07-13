def main():
    string1, string2 = input().split()
    # a = transforma_string_lista(string1)
    # b = transforma_string_lista(string2)
    print(is_anagram(string1, string2))


# Maneira pythonica
# def is_anagram(string1, string2):
#     return sorted(string1) == sorted(string2)


def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)


def transforma_string_lista(string):
    lista = [None]
    for i in range(len(string)):
        lista.append(ord(string[i]))

    return lista


if __name__ == '__main__':
    main()
