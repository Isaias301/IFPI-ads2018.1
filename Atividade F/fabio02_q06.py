"""	Questão: Lista E 02
	Descrição: Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo)
	verifique e escreva se os 3 (três) números formam um triângulo (a soma dos ângulos 
	internos é igual a 180o). Se formam, verifique se formam um triângulo acutângulo 
	(3 ângulos < 90o), retângulo (1 ângulo = 90o) ou obtusângulo (1 ângulo > 90o). 
	Não existe ângulo com tamanho 0o (zero grau).
"""

def main():
	# entrada
	numero1 = int(input("Digite o primeiro numero: "))
	numero2 = int(input("Digite o segundo numero: "))
	numero3 = int(input("Digite o terceiro numero: "))

	# calculos, operacoes, processamento
	if numero1 + numero2 + numero3 == 180:
		if numero1 == 90 or numero2 == 90 or numero3 == 90:
			print("Triângulo retângulo")
		elif numero1 > 90 or numero2 > 90 or numero3 > 90:
			print("Triângulo obtusângulo")
		elif numero1 < 90 and numero2 < 90 and numero3 < 90:
			print("Triângulo acutângulo")
		else:
			pass
	else:
		print("Numeros não somam 180°")


if __name__ == '__main__':
	main()