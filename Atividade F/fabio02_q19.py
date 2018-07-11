"""	Questão: Lista E 02
	Descrição: Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida 
	calcule o índice de massa corpórea (IMC = peso / altura 2 ). Ao final, escreva 
	se a pessoa está com peso normal (IMC abaixo de 25), obeso (IMC entre 25 e 30) 
	ou obesidade mórbida (IMC acima de 30).
"""

def main():
	# entrada
	altura = float(input("Digite sua altura: "))
	peso = float(input("Digite seu peso: "))
	
	# calculos, operacoes, processamento
	resultado = imc(altura, peso)

	# saida
	print(resultado)


def imc(altura, peso):
	imc = (peso/altura)/2
	if imc < 25:
		return "Peso normal"
	elif imc > 25 and imc < 30:
		return "Peso obeso"
	elif imc > 30:
		return "Peso mórbida"
	else:
		return "Dados inválidos"


if __name__ == '__main__':
	main()