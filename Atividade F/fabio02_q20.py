"""	Questão: Lista E 02
	Descrição: Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante 
	(primeiro, segundo, terceiro ou quarto) em que o ângulo se localiza.
"""

def main():
	# entrada
	angulo = int(input("Digite o ângulo: "))
	
	
	# calculos, operacoes, processamento
	resultado = indentificar_quadrante(angulo)

	# saida
	print(resultado)


def indentificar_quadrante(angulo):
	if angulo > 0 and angulo < 90:
		return "Primeiro quadrante"
	elif angulo > 90 and angulo < 180:
		return "Segundo quadrante"
	elif angulo > 180 and angulo < 270:
		return "Terceiro quadrante"
	elif angulo > 270 and angulo < 360:
		return "Quarto quadrante"
	else:
		return "Angulo invalido"

if __name__ == '__main__':
	main()