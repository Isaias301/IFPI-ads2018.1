def main():
    a = input().split()
    b = input().split()
    print(conjunto_uniao(a, b))


def conjunto_uniao(a, b):
    verto_uniao = a
    tamanho_vetor_b = len(b)
    tamanho_vetor_uniao = len(verto_uniao)
    teste = b

    for i in range(tamanho_vetor_b):
        for j in range(tamanho_vetor_uniao):
            if b[j] == verto_uniao[i]:
                
            # if b[i] != verto_uniao[j]:
            #     verto_uniao.append("=")
            # else:
            #     pass
            #     # verto_uniao.append("!=")
    return teste


# pythonico
# def conjunto_uniao(a, b):
#     verto_uniao = a
#     tamanho_vetor_uniao = len(verto_uniao)
#     for i in range(len(b)):
#         if b[i] not in verto_uniao:
#             verto_uniao.append(b[i])
#     return verto_uniao


# def conjun_intersecao(a, b):
#     pass



if __name__ == '__main__':
    main()
