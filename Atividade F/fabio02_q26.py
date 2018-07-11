"""	Questão: Lista E 02
	Descrição: Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.
"""

def main():
	# entrada
	lado1 = input("Digite o primeiro lado: ")
	lado2 = input("Digite o segundo lado: ")
	lado3 = input("Digite o terceiro lado: ")
	
	# calculos, operacoes, processamento
	resultado = verifica_lados(int(lado1), int(lado2), int(lado3)) 

	# saida
	print(resultado)


def verifica_lados(lado1, lado2, lado3):
	if lado1 > lado2 and lado1 > lado3:
		return "Hipotenusa: {}\nCatetos: {} e {}".format(lado1, lado2, lado3)
	elif lado2 > lado1 and lado2 > lado3:
		return "Hipotenusa: {}\nCatetos: {} e {}".format(lado2, lado1, lado3)
	elif lado3 > lado1 and lado3 > lado2:
		return "Hipotenusa: {}\nCatetos: {} e {}".format(lado3, lado1, lado2)

if __name__ == '__main__':
	main()