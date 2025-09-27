import java.util.Scanner;

public class codigoacesso {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); 
		String codigodigitado;

		do {
			System.out.println("Digite um código:");

		codigodigitado = input.nextLine();

		if ("Admin123".equals(codigodigitado)){
			System.out.println("Bem-vindo, Administrador!");
		} else if ("User123".equals(codigodigitado)) {
			System.out.println("Bem-vindo, Usuário! ");
		} else {
			System.out.println("Senha incorreta!");
		}
		} while (!"Admin123".equals(codigodigitado) && !"User123".equals(codigodigitado));
        

}
}