fila_amigo = ["Olá!", "Te amo!", "Tchau!"]
fila_usuario = []
contador = 0

while contador < len(fila_amigo):  # enquanto houver mensagens do amigo
    print(f"Amigo - {fila_amigo[contador]}")
    
    resposta = input("Digite uma mensagem ou N para sair ou D para deletar a última mensagem: ")
    
    if resposta.upper() == "N":
        print("Encerrando conversa...")
        break

    elif resposta.upper() == "D":
        if fila_usuario:
            fila_usuario.pop()  # deleta a última mensagem enviada
            print("**Última mensagem deletada**")
        else:
            print("**Você não possui mensagens para deletar**")
    
    else:
        fila_usuario.append(resposta)
        print(f"Eu - {fila_usuario[-1]}")

    contador += 1  # só avança para a próxima mensagem do amigo depois da resposta

# Saiu do while:
if contador == len(fila_amigo):
    print("**Amigo não tem mais mensagens. Fim da conversa.**")