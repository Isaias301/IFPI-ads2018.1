"""	Questão: Lista E 40
	Descrição: Calcule a quantidade de dinheiro gasta por um fumante. 
	Dados de entrada: o número de anos que ele fuma, o nº de cigarros 
	fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).
"""

def main():
	# entrada
	tempo_de_fumante = int(input("A quantos anos você e fumante? "))
	cigaros_fumados_por_dia = int(input("Quantos cigarros você fuma por dia? "))
	preco_da_cateira = float(input("Preço da carteira de cigarro: "))

	# calculos, operacoes, processamento
	dias_de_fumante = tempo_de_fumante * 365
	quantidade_de_carteiras = (cigaros_fumados_por_dia * dias_de_fumante) / 20
	gasto = quantidade_de_carteiras * preco_da_cateira
	# saida
	print("Em %i anos você gastou: R$ %.2f" % (tempo_de_fumante ,gasto))

	
if __name__ == '__main__':
	main()