def main():
	numero = int(input())

	while True:
		numero = numero / 2
		if numero < 1:
			print(numero)
			break


		
if __name__ == '__main__':
	main()