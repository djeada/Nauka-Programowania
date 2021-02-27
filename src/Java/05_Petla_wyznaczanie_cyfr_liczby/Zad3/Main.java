
public class Main
{
	public static void main(String[] args)
	{

		//Dla pobranej liczby, wyswietl liczbe Pi tyle razy 
		//ile wynosi pobrana liczba, z dokladnoscia do tylu 
		//miejsc po przecinku ile wynosi pobrana liczba.

		System.out.print("Podaj liczbe");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());

		int suma = 0;

		while (a > 0)
		{
			suma += (a % 10);
			a = a / 10;
		}

		System.out.print("Suma cyfr podanej liczby wynosi " + suma + "\n");

	}

}