using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

//Pedir uma nota. Se a nota for menor ou igual a 5, imprimir "Reprovado", senão, se a nota for menor ou igual a 6, imprimir "Recuperação", senão imprimir "Aprovado".

namespace HelloWorld
{
	public class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("Digite o valor da nota: ");
			double nota = Convert.ToDouble(Console.ReadLine());
			
			if (nota <= 5){
			Console.WriteLine("Reprovado");
			}
			else if (nota == 6){
			Console.WriteLine("Recuperação");
			} 
			else {
			 Console.WriteLine("Aprovado");
			}
		}
	}
}