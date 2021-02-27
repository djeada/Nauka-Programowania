

public class Main
{
	//Napisz funkcje, ktora dla otrzymanej liczby n,
	//poprosi uzytkownika o podanie n liczb i zwroci
	//ich srednia arytmetyczna

	public static float srednia(int n)
	{

		float suma = 0.0F;
		int x;

		for (int i = 0; i < n; i++)
		{
			System.out.print("Podaj liczbe: ");
			System.out.print("\n");
			x = Integer.parseInt(System.console().readLine());
			suma += x;
		}

		return suma / n;
	}

	public static void main(String[] args)
	{

		System.out.print("Podaj liczbe n: ");
		System.out.print("\n");
		int n;
		n = Integer.parseInt(System.console().readLine());

		float wynik = srednia(n);

		System.out.print("Srednia z podanych liczb to ");
		System.out.print(wynik);
		System.out.print("\n");

	}

}