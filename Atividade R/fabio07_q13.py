def main():
    vetor = [[1,2,3], [4,5,6], [7,8,9]]
    print(determinante(vetor))

def determinante(vetor):
    # soma dos eleentos da diagonal primaria
    diag_primaria = 0
    for i in range(len(vetor)):
        for j in range(len(vetor[i])):
            if i == j:
                diag_primaria += vetor[i][j]
    diag_secundaria = 0
    # soma dos eleentos da diagonal secundaria
    for i in range(len(vetor)):
        for j in range(len(vetor[i])):
            if i == len(vetor)-1-j:
                diag_secundaria += vetor[i][j]
    return diag_primaria + diag_secundaria



if __name__ == '__main__':
    main()
