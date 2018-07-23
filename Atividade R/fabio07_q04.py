def main():
    a = input().split()
    b = input().split()

    print(conjunto_uniao(a, b))
    # print(conjun_intersecao(a, b))


def conjunto_uniao(a, b):
    if a < b:
        a = b
        b = a

    unitario = a
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                unitario += [b[j]]
                del a[i]
    return sorted(unitario)


def conjun_intersecao(a, b):
    r = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                r = r + [a[i]]
    return r


# pythonico
# def conjunto_uniao(a, b):
#     if a < b:
#         a = b
#         b = a
#
#     unitario = a
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i] == b[j]:
#                 unitario.append(b[j])
#                 del(a[i])
#     return unitario


# pythonico
# def conjunto_uniao(a, b):
#     verto_uniao = a
#     tamanho_vetor_uniao = len(verto_uniao)
#     for i in range(len(b)):
#         if b[i] not in verto_uniao:
#             verto_uniao.append(b[i])
#     return verto_uniao


if __name__ == '__main__':
    main()
