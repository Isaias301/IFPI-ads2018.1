"""	Questão: Lista E 02
	Descrição: Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a 
	média das duas notas for maior ou igual a 7,0. 

	Caso a média seja inferior a 7,0, o 
	programa deve ler a nota do exame e calcule a média final. 

	Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso 
	contrário deve escreva “Reprovado”.
"""

def main():
	# entrada
	nota1 = float(input("Digite a primeira nota: "))
	nota2 = float(input("Digite a segunda nota: "))

	# calculos, operacoes, processamento
	resultado = resultado_aluno(nota1, nota2)

	# saida
	print(resultado)


def resultado_aluno(nota1, nota2):
	media = (nota1+nota2)/2
	if media < 7.0:
		nota_exame = float(input("Digite a nota do exame: "))
		media_final = (nota_exame + media)/2
		if media_final >= 5.0:
			return "Aprovado"
		else:
			return "Reprovado"
	else:
		return "Aprovado"


if __name__ == '__main__':
	main()