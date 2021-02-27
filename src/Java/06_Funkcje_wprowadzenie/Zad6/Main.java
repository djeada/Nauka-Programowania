
public class Main
{
	//Napisz funkcje, ktora dla otrzymanej liczby zwroci sume cyfr tej liczby.

	public static int sumaCyfr(int a)
	{
		int suma = 0;

		while (a > 0)
		{
			suma += (a % 10);
			a /= 10;
		}

		return suma;
	}

	public static void main(String[] args)
	{
		System.out.print("Podaj liczbe: ");
		System.out.print("\n");
		int a;
		a = Integer.parseInt(System.console().readLine());

		System.out.print("Suma cyfr liczby to: ");
		System.out.print(sumaCyfr(a));
		System.out.print("\n");

	}

}