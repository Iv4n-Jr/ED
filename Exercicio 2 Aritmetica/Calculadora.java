import java.util.*;

public class Calculadora_Java {
  
  
    public static void main(String[] args) {
      Scanner input = new Scanner(System.in);
      float a, b, soma, subt, mult, div;
      
      
      System.out.println("Digite um valor: ");
      a = input.nextFloat();
      System.out.println("Digite um valor diferente de 0: ");
      b = input.nextFloat();
      
      soma = a + b;
      subt = a - b;
      mult = a * b;
      div = a / b;
      
      System.out.println("Soma: " + soma);
      System.out.println("Subtração: " + subt);
      System.out.println("Multiplicação: " + mult);
      System.out.println("Divisão: " + div);
      
  }
}