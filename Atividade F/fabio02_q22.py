"""	Questão: Lista E 02
	Descrição: Leia a hora do início de um jogo e a hora de fim do jogo 
	(cada hora é composta por 2 variáveis inteiras hora e minuto). Calcule e escreva a duração 
	do jogo (horas e minutos), sabendo-se que o tempo máximo de duração do jogo é de 24 horas 
	e que ele pode iniciar-se em um dia e terminar no dia seguinte.
"""

def main():
	# entrada
	inicio_jogo = float(input("Digite o horario de inicio do jogo: "))
	termino_jogo = float(input("Digite o horario de termino do jogo: "))

	
	# calculos, operacoes, processamento
	if inicio_jogo < termino_jogo:
		tempo_jogo = termino_jogo - inicio_jogo
		hora = (tempo_jogo * 60)/60
		minuto = (tempo_jogo * 60)%60
	else:
		tempo_jogo = 24 - inicio_jogo + termino_jogo
		hora = (tempo_jogo * 60)/60
		minuto = (tempo_jogo * 60)%60

	# saida
	print("O jogo teve duraçao de: %i h %i min" % (hora, minuto))



if __name__ == '__main__':
	main()