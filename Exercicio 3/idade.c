#include <stdio.h>
int main()
{
	printf("Digite sua idade: ");
	int idade;
	scanf("%d", &idade);
	
	if (idade < 18){
	  printf("\nVoc� � menor de idade");
	}
	else {
	  printf("\nVoc� � maior de idade");
	}
}