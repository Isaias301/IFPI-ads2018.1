"""	Questão: Lista E 02
	Descrição: Leia 3 (três) números (cada número corresponde a um lado do triângulo), 
	verifique e escreva se os 3 (três) números formam um triângulo (a soma de dois 
	lados não pode ser menor que o terceiro lado). Se formam, verifique se formam um 
	triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno 
	(3 lados diferentes). Não existe lado com tamanho 0 (zero).
"""

def main():
	# entrada
	numero1 = int(input("Digite o primeiro numero: "))
	numero2 = int(input("Digite o segundo numero: "))
	numero3 = int(input("Digite o terceiro numero: "))

	# calculos, operacoes, processamento
	
	if numero1 + numero2 > numero3:
		if numero1 == numero2 == numero3:
			print("Triângulo equilátero")
		elif numero1 == numero2 or numero3 == numero2 or numero1 == numero3:
			print("Triângulo isósceles")
		elif numero1 != numero2 != numero3:
			print("Triângulo escaleno")
		else:
			pass
	else:
		print("Numeros não formam um triangulo")


if __name__ == '__main__':
	main()