

def main():
	# entrada

	kg_morango = int(input("kg_morango: "))
	kg_maca = int(input("kg_macasss: "))

	if kg_morango <= 5:
		morango = kg_morango*2.50
	elif kg_morango > 5:
		morango = kg_morango*2.20

	if kg_maca <= 5:
		maca = kg_maca*1.80
	elif kg_maca > 5:
		maca = kg_maca*1.50

	valor_compra = maca + morango

	if kg_morango + kg_maca > 8 or valor_compra > 25:
		valor_final = valor_compra - (10/100)*valor_compra
		print("Valor a ser pago: %.2f" % valor_final)
	else:
		print("Valor a ser pago: %.2f" % valor_compra)


if __name__ == '__main__':
	main()