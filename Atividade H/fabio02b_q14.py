

def main():
	# entrada

	combustivel = input("Tipo de combustivel: ")
	listros = int(input("Quntos listros: "))

	if combustivel.lower() == "a":
		if listros <= 20 and listros >=1:
			valor = listros - ((3/100)*1.90)
			print("Você pagara R$ %.2f" % (valor))
		elif listros > 20:
			valor = listros - ((5/100)*1.90)
			print("Você pagara R$ %.2f" % (valor))
	elif combustivel.lower() == "g":
		if listros <= 20 and listros >=1:
			valor = listros - ((4/100)*2.50)
			print("Você pagara R$ %.2f" % (valor))
		elif listros > 20:
			valor = listros - ((6/100)*2.50)
			print("Você pagara R$ %.2f" % (valor))


if __name__ == '__main__':
	main()