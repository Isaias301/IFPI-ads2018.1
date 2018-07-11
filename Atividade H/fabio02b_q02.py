"""	Questão: Lista 02 B
	Descrição: Leia uma letra, 
	verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.
"""

def main():
	# entrada
	letra = input("Digite uma letra: ")

	if letra.upper() == "M":
		print("Masculino")
	elif letra.upper() == "F":
		print("Feminino")
	else:
		print("Sexo Inválido")
	

if __name__ == '__main__':
	main()