opcao = 0
pilha = []

#loop para escolha de opções
while opcao != 5:
	numerador = 1
	print(
		"========MENU SANDUÍCHE========\n",
		"1️⃣ Adicionar ingrediente\n",
		"2️⃣ Remover ingrediente (do topo)\n",
		"3️⃣ Ver último ingrediente adicionado\n",
		"4️⃣ Mostrar sanduíche\n",
		"5️⃣ Finalizar pedido\n"	
	)
	opcao = int(input("Digite uma das opções: "))

	if opcao == 1:
		adicao = input("Diga gostaria de adicionar: ")
		if adicao.strip() == "": #Caso o usuário digite nada
			print("Você adicionou nada!")
		else:	
			pilha.append(adicao)
	
	if opcao == 2:
		if len(pilha) > 0: 
			print(f"{pilha[-1]} removido!")
			pilha.pop()
		else: #Caso a pilha estiver vazia
			print("Pilha vazia")
	
	if opcao == 3:
		if len(pilha) > 0:
			print(f"{pilha[-1]} Foi o último elemento adicionado!")
		else: #Caso não tenha itens para ver
			print("Sem itens para ver")

	
	if opcao == 4:
		if len(pilha) > 0:
			for item in reversed(pilha):
				print(f"{numerador} - {item}")
				numerador += 1
		else:#Caso não tenha itens para ver
			print("Sem itens para ver")

	if opcao == 5:
		if len(pilha) > 0:
			print("Seu pedido foi realizado!")
			for item in reversed(pilha):
				print(f"{numerador} - {item}")
				numerador += 1
		else: #Caso o Usuario tenha pedido nada
			print("Você realizou nenhum pedido!")