#include <iostream>
using namespace std;

int main() 
{
	double preco;

  	cout << "Digite o valor da compra:\n";
	cin >> preco;

	if (preco >= 100){
		cout << "Frete grátis!";
	} else {
		preco += 15;
		cout << "Valor da compra + frete\n";
		cout << preco;
	}

    return 0;
}