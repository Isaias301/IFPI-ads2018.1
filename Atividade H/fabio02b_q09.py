"""	Questão: Lista 02 B
	Descrição: Leia um número e exiba o dia correspondente da semana. 
	(1-Domingo, 2- Segunda etc.), se digitar outro valor deve aparecer valor inválido.
"""

def main():
	# entrada
	numero = int(input("Valor da hora: "))
	
	if numero == 1:
		print("Domingo")
	elif numero == 2:
		print("Segunda")
	elif numero == 3:
		print("Terca")
	elif numero == 4:
		print("Quarta")
	elif numero == 5:
		print("Quinta")
	elif numero == 6:
		print("Sexta")
	elif numero == 7:
		print("Sabado")
	else:
		print("Valor inválido")
		


if __name__ == '__main__':
	main()