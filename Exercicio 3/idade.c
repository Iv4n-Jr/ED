#include <stdio.h>
int main()
{
	printf("Digite sua idade: ");
	int idade;
	scanf("%d", &idade);
	
	if (idade < 18){
	  printf("\nVocê é menor de idade");
	}
	else {
	  printf("\nVocê é maior de idade");
	}
}