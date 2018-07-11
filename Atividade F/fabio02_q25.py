"""	Questão: Lista E 02
	Descrição: Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. 
	O algoritmo deve escrever uma mensagem de permissão de acesso ou não.
"""

def main():
	# entrada
	password = input("Digite sua senha: ")
	
	# calculos, operacoes, processamento
	resultado = verify_password(password) 

	# saida
	print(resultado)


def verify_password(password):
	right_password = 1234
	if int(password) == right_password:
		return "Bem vindo(a)"
	else:
		return "Senha errada"


if __name__ == '__main__':
	main()