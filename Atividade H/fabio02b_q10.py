"""	Questão: Lista 02 B
	Descrição: Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo 
	de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

	Média de Aproveitamento Conceito
	Entre 9.0 e 10.0 		A
	Entre 7.5 e 9.0			B
	Entre 6.0 e 7.5			C
	Entre 4.0 e 6.0			D
	Entre 4.0 e zero		E
	
	O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a 
	mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

def main():
	# entrada
	nota1 = float(input())
	nota2 = float(input())

	media = (nota1+nota2)/2

	if media >= 9 and media <= 10:
		print("Media: {}\nConceito: {}\nSituação: {}".format(media, "A", "APROVADO"))
	elif media >= 7.5 and media <= 9:
		print("Media: {}\nConceito: {}\nSituação: {}".format(media, "B", "APROVADO"))
	elif media >= 6 and media <= 7.5:
		print("Media: {}\nConceito: {}\nSituação: {}".format(media, "C", "APROVADO"))
	elif media >= 4 and media <= 6:
		print("Media: {}\nConceito: {}\nSituação: {}".format(media, "D", "REPROVADO"))
	elif media >= 4 and media <= 0:
		print("Media: {}\nConceito: {}\nSituação: {}".format(media, "E", "REPROVADO"))
		

if __name__ == '__main__':
	main()