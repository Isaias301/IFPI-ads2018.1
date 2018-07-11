"""	Questão: Lista E 14
	Descrição: Leia 3 notas de um aluno e o peso de cada nota, 
	calcule e escreva a média ponderada.
"""

def main():
	# entrada
	primeira_nota = float(input("Digite a primeira nota: "))
	peso_primeira_nota = float(input("Digite o peso da primeira nota: "))

	segunda_nota = float(input("Digite a segunda nota: "))
	peso_segunda_nota = float(input("Digite o peso da segunda nota: "))

	terceira_nota = float(input("Digite a terceira nota: "))
	peso_terceira_nota = float(input("Digite o peso da terceira nota: "))
	
	
	# calculos, operacoes, processamento
	media_ponderada = ( primeira_nota * peso_primeira_nota + segunda_nota * peso_segunda_nota + terceira_nota * peso_terceira_nota ) / (primeira_nota + segunda_nota + terceira_nota)

	# saida
	print('Média ponderada:  %.2f' % media_ponderada)

	
if __name__ == '__main__':
	main()