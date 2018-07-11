

def main():
	
	# entrada
	tipo_carne = input("Tipo de carne: ")
	kg_carne = int(input("Quantos Kg: "))
	tipo_pagamento = int(input("Tipo de pagamento: 1 - Avista | 2 - Cartão de credito | 3 - Cartão Tabajara: "))

	if tipo_carne.lower() == "file":
		if kg_carne <= 5:
			if tipo_pagamento == 3: 
				valor_da_compra = kg_carne*4.90
				desconto = (5/100)*valor_da_compra
				valor_total = valor_da_compra - desconto
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
			else:
				valor_da_compra = kg_carne*4.90
				desconto = 0
				valor_total = valor_da_compra - desconto
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
		elif kg_carne > 5:
			if tipo_pagamento == 3: 
				valor_da_compra = kg_carne*5.80
				desconto = (5/100)*valor_da_compra
				valor_total = valor_da_compra - desconto
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
			else:
				valor_da_compra = kg_carne*5.80	
				desconto = 0
				valor_total = valor_da_compra
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
	elif tipo_carne.lower() == "alcatra":
		if kg_carne <= 5:
			if tipo_pagamento == 3: 
				valor_da_compra = kg_carne*5.90
				desconto = (5/100)*valor_da_compra
				valor_total = valor_da_compra - desconto
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
			else:
				valor_da_compra = kg_carne*5.90
				desconto = 0
				valor_total = valor_da_compra - desconto
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
		elif kg_carne > 5:
			if tipo_pagamento == 3: 
				valor_da_compra = kg_carne*6.80
				desconto = (5/100)*valor_da_compra
				valor_total = valor_da_compra - desconto
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
			else:
				valor_da_compra = kg_carne*6.80	
				desconto = 0
				valor_total = valor_da_compra
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
	elif tipo_carne.lower() == "picanha":
		if kg_carne <= 5:
			if tipo_pagamento == 3: 
				valor_da_compra = kg_carne*6.90
				desconto = (5/100)*valor_da_compra
				valor_total = valor_da_compra - desconto
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
			else:
				valor_da_compra = kg_carne*6.90
				desconto = 0
				valor_total = valor_da_compra - desconto
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
		elif kg_carne > 5:
			if tipo_pagamento == 3: 
				valor_da_compra = kg_carne*7.80
				desconto = (5/100)*valor_da_compra
				valor_total = valor_da_compra - desconto
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)
			else:
				valor_da_compra = kg_carne*7.80	
				desconto = 0
				valor_total = valor_da_compra
				cupom(tipo_carne, valor_da_compra, kg_carne, "Cartão Tabajara", desconto, valor_total)		

def cupom(carne, valor_total, quantidade, tipo_pagamento, desconto, valor_a_pagar):
	print("Tipo de carne: %s\nQuantidade: %i\nPreço total: %.2f\nTipo de pagamento: %s\nValor do desconto: %.2f\nValor a pagar: %.2f" % (carne, quantidade, valor_total, tipo_pagamento, desconto, valor_a_pagar))


if __name__ == '__main__':
	main()