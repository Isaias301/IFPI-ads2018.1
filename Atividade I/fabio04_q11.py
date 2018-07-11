def main():
    media_final = 0
    tot_aluno_aprovado = 0
    tot_aluno_reprovado = 0
    tot_aluno = 0
    while True:
        matricula = int(input("Matricula: "))
        if matricula == 0:
            break
        else:
            nota1 = float(input("Nota 1: "))
            nota2 = float(input("Nota 2: "))
            nota3 = float(input("Nota 3: "))
            media_final = (2 * nota1) + (3 * nota2) + (5 * nota3) / 10
            tot_aluno += 1
            if media_final >= 7:
                print("Aprovado")
                tot_aluno_reprovado += 1
            elif media_final < 7:
                print("Aluno reprovado")
                tot_aluno_reprovado += 1
            media_final = 0
    print("Quantidade de alunos: {}".format(tot_aluno))


if __name__ == '__main__':
    main()