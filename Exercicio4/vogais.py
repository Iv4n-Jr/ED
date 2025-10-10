#3) Programa - vogais: Peça ao usuário que digite uma palavra. Para cada letra da palavra, verificar se ela é uma vogal (aeiouAEIOU). Conte quantas vogais existem e imprima o total ao final. Dica: Use um laço de repetição (for) para percorrer as letras, e uma estrutura de decisão (if) para verificar se cada letra é uma vogal..

palavra = input("Digite uma palavra ou mais palavras: ") #O usuário irá fazer um input de uma ou mais palavras
contador = 0

for i in palavra:
	if i in ["a", "e", "i", "o", "u", "ã", "à", "á", "â", "é", "ê", "ó", "õ", "ô", "ò", "í", "ì", "î", "ú", "ù", "û", "A", "Ã", "À", "Á", "Â", "E", "É", "È", "Ê", "I", "Í", "Ì", "Î", "O", "Ò", "Ó", "Ô", "Õ", "U", "Ù", "Ú", "Û"]: #Um conjunto de vogais minúsculas e maiúsculas sendo acentuadas ou não
		contador += 1
		print(f'{contador} - {i}')
	else:
		continue
print(f'\n{contador} vogais!')