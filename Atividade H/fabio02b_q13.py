"""	Questão: Lista 02 B
	Descrição: Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

	a) "Telefonou para a vítima ?"
	b) "Esteve no local do crime ?"
	c) "Mora perto da vítima ?"
	d) "Devia para a vítima ?"
	e) "Já trabalhou com a vítima ?"

	O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. 
	Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
	entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
	como "Inocente".
"""

def main():
	# entrada

	p1 = input("Telefonou para a vítima ?")
	p2 = input("Esteve no local do crime ?")
	p3 = input("Mora perto da vítima ?")
	p4 = input("Devia para a vítima ?")
	p5 = input("Já trabalhou com a vítima ?")

	respostas = (p1.lower(), p2.lower(), p3.lower(), p4.lower(), p5.lower())
	
	if respostas.count("sim") == 2:
		print("Suspeita")
	elif respostas.count("sim") >= 3 and respostas.count("sim") <= 4:
		print("Cúmplice")
	elif respostas.count("sim") == 5:
		print("Assassino")
	else:
		print("Inocente")

if __name__ == '__main__':
	main()