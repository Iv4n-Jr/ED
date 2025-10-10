using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Loop
{
    class Program
    {

       

        static void Main(string[] args)
        {
            
            double gasto;
            double valor;
            int rep;
            Console.WriteLine("Quantas despesas você quer registrar:");
             rep = Convert.ToInt32(Console.ReadLine());

            for (int i = 0; i<= rep;  i++) {
                Console.WriteLine("Digite o valor a ser gasto");
                gasto = Convert.ToInt32(Console.ReadLine());
                valor =+ gasto;
                Console.WriteLine("O valor total é " + valor);
            }
            
            Console.ReadKey();



        }
    }
}
