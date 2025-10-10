#include <iostream>

using namespace std;

int main() {
    int numero;

    cout << "Digite um número inteiro positivo: ";
    cin >> numero;

    // Verifica se o número é positivo
    if (numero < 0) {
        cout << "Por favor, digite um número inteiro **positivo**." << endl;
        return 1; // Encerra o programa com código de erro
    }

    // Laço de contagem regressiva
    while (numero >= 0) {
        cout << numero << endl;
        numero--; // Decrementa o número
    }

    cout << "Contagem regressiva finalizada!" << endl;

    return 0;
}
