"""	Questão: Lista E 46
	Descrição: Uma loja vende seus produtos no sistema entrada mais duas prestações, 
	sendo a entrada maior ou igual a cada uma das duas prestações; estas devem ser iguais, 
	inteiras e as maiores possíveis. Por exemplo, se o valor da mercadoria for R$ 270,00, 
	a entrada e as duas prestações são iguais a R$ 90,00; se o valor da mercadoria 
	for R$ 302,00, a entrada é de R$ 102,00 e as duas prestações são iguais a R$ 100,00.
	Escreva um algoritmo que receba o valor da mercadoria e forneça o valor da entrada e das 
	duas prestações, de acordo com as regras acima.
"""

def main():
	# entrada
	valor_da_mercadoria = float(input("Digite o valor do da mercadoria: "))
	valor_da_entrada = float(input("Digite o valor da entrada: "))
	
	# calculos, operacoes, processamento
	valor_da_mercadoria_menos_entrada = valor_da_mercadoria - valor_da_entrada
	valor_parcelas = valor_da_mercadoria_menos_entrada / 2

	if valor_parcelas <= valor_da_mercadoria_menos_entrada:
		parcelas_valor_final = valor_parcelas
	else: 
		parcelas_valor_final = "Entrada insuficiente"
	
	# saida
	print("Com uma entrada de: R$ %.2f" % valor_da_entrada)
	print("Você pagara duas parcelas de: R$ %.2f" % parcelas_valor_final)

	
if __name__ == '__main__':
	main()