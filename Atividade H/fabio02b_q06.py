"""	Questão: Lista 02 B
	Descrição: Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino 
	ou N para Noturno e escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" 
	ou "Valor Inválido!", conforme o caso.
"""


def main():
	# entrada
	letra = input("Você estuda em que turno: ")

	if letra.lower() == "m":
		print("Bom Dia!")
	if letra.lower() == "v":
		print("Boa Tarde!")
	if letra.lower() == "n":
		print("Boa Noite!")
	else:
		print("Valor Inválido!")	

if __name__ == '__main__':
	main()