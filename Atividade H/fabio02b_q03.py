"""	Questão: Lista 02 B
	Descrição: Leia uma letra e verifique se a letra digitada é vogal ou consoante.
"""

def main():
	# entrada
	letra = input("Digite uma letra: ")

	if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
		print("Vogal")
	else:
		print("Consoante")	

if __name__ == '__main__':
	main()