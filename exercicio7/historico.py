import random

opcao = 0
pilha = []
sites = ["YouTube", "Reddit", "Discord", "Google", "WhatsApp", "Duolingo", "Instagram", "Twitter"]

#loop para escolha de opções
while opcao != 5:
	numerador = 1
	print(
		"========HISTÓRICO========\n",
		"1️⃣ Entrar em um site\n",
		"2️⃣ Remover último site acessado\n",
		"3️⃣ Ver último site acessado\n",
		"4️⃣ Mostrar histórico\n",
		"5️⃣ Sair\n"	
	)
	opcao = int(input("Digite uma das opções: "))

	if opcao == 1:
		site_entrado = random.choice(sites)
		pilha.append(site_entrado)
		print(f"Você entrou e saiu do {site_entrado}!")
	
	if opcao == 2:
		if len(pilha) > 0: 
			print(f"{pilha[-1]}, removido do histórico!")
			pilha.pop()
		else: #Caso o histórico esteja vázio
			print("O histórico está vázio!")
	
	if opcao == 3:
		if len(pilha) > 0:
			print(f"{pilha[-1]} Foi o último site acessado!")
		else: #Caso o histórico esteja vázio
			print("O histórico está vázio!")

	
	if opcao == 4:
		if len(pilha) > 0:
			for item in reversed(pilha):
				print(f"{numerador} - {item}")
				numerador += 1
		else: #Caso o histórico esteja vázio
			print("O histórico está vázio!")

	if opcao == 5:
		print("Até mais!")