cor = 0

while cor != "azul" and cor != "vermelho" and cor != "amarelo":
	cor = input("Diga uma cor primária: ")

	if cor != "azul" and cor != "vermelho" and cor != "amarelo":
		print("Essa cor não faz parte das cores primárias!")

	else:
		if cor == "vermelho":
			print("VERMELHO: calor, energia, perigo")
		elif cor == "amarelo":
			print("alegria, riqueza, luz")
		else:
			print("AZUL: calma, inteligência, frio")