"""	Questão: Lista E 13
	Descrição: Leia um valor em real(R$), calcule e escreva 70% deste valor.
"""

def main():
	# entrada
	valor_em_real = float(input("Digite um valor em R$: "))
	
	
	# calculos, operacoes, processamento
	porcentagem = ( 70 / 100 ) * valor_em_real

	# saida
	print('Resultado:  %.2f' % porcentagem)

	
if __name__ == '__main__':
	main()