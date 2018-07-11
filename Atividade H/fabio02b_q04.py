"""	Questão: Lista 02 B
	Descrição: Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
	"Aprovado", se a média alcançada for maior ou igual a sete;
	"Reprovado", se a média for menor do que sete;
	"Aprovado com Distinção", se a média for igual a dez.
"""

def main():
	# entrada
	n1 = float(input("Digite a 1º nota: "))
	n2 = float(input("Digite a 2º nota: "))

	# processamento
	media = (n1+n2)/2
	if media < 9:
		if media >= 7:
			print("Aprovado")
	else:
		if media < 7:
			print("Reprovado")
		if media == 10:
			print("Aprovado com Distinção")

if __name__ == '__main__':
	main()