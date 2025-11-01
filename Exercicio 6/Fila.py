fila = []
opcao = 0

while opcao != 4:
    numerador = 1
    print("")
    print("--- MENU ---")
    print("1. Adicionar pessoa à fila")
    print("2. Atender pessoa")
    print("3. Mostrar fila")
    print("4. Sair")
    opcao = int(input("Digite uma das opções: "))

    if opcao == 1:
        nome = input("Digite o nome da pessoa:")
        fila.append(nome)
        print(f'{nome} Adicionado à fila')
        
    elif opcao == 2:
        if len(fila) > 0:
            print(f"{fila[0]} Atendido(a)!")
            fila.pop(0)
        else:
            print("Sem pessoas para atender!")
    
    elif opcao == 3:
        if len(fila) > 0:
            for nome in fila:
                print(f"{numerador} - {nome}")
                numerador = numerador + 1
        else:
            print("Sem pessoas para listar!")