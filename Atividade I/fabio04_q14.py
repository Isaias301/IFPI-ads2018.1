def main():
    cont_dilma = 0
    cont_serra = 0
    cont_ciro = 0
    cont_indeciso = 0
    cont_outros = 0
    cont_nulo = 0
    while True:
        print("45 - Serra\n13 - Dilma\nCiro Gomes - 23\nIndeciso - 99\n98 - Outros\n0 - Nulo/Branco")
        opniao = int(input())
        if opniao == -1:
            break
        if opniao == 45:
            cont_serra += 1
        elif opniao == 13:
            cont_dilma += 1
        elif opniao == 23:
            cont_ciro += 1
        elif opniao == 99:
            cont_indeciso += 1
        elif opniao == 98:
            cont_outros += 1
        elif opniao == 0:
            cont_nulo += 1
    total_intrevistados = cont_dilma + cont_serra + cont_ciro + cont_indeciso + cont_outros + cont_nulo
    print("Total de intrevistados: {}".format(total_intrevistados))

    por_serra = (total_intrevistados / cont_serra) - 1
    print("Porcentagem Serra: %2.f %%" % por_serra)

    por_dilma = (total_intrevistados / cont_dilma) - 1
    print("Porcentagem Dilma: %2.f %%" % por_dilma)

    por_ciro = (total_intrevistados / cont_ciro) - 1
    print("Porcentagem Ciro Gomes: %2.f %%" % por_ciro)

    por_indecisos = (total_intrevistados / cont_indeciso) - 1
    print("Porcentagem Indecisos: %2.f %%" % por_indecisos)

    por_outro = (total_intrevistados / cont_outros) - 1
    print("Porcentagem Outros: %2.f %%" % por_outro)

    por_nulos = (total_intrevistados / cont_nulo) - 1
    print("Porcentagem Outros: %2.f %%" % por_nulos)


if __name__ == '__main__':
    main()
