#include <stdio.h>
#include <string.h>

int main() {
    // Define a senha correta
    const char senhaCorreta[] = "1234";
    char senhaDigitada[100];

    // Loop enquanto a senha estiver incorreta
    do {
        printf("Digite a senha: ");
        scanf("%s", senhaDigitada);

        if (strcmp(senhaDigitada, senhaCorreta) != 0) {
            printf("❌ Senha incorreta!\n");
        }

    } while (strcmp(senhaDigitada, senhaCorreta) != 0);

    // Senha correta foi digitada
    printf("✅ Senha correta!\n");

    return 0;
}
