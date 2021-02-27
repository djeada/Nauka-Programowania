
public class Main
{
	public static void main(String[] args)
	{

		//Dla dwoch pobranych liczb, wypisz najpierw wieksza potem mniejsza.

		System.out.print("podaj dwie liczby:");
		System.out.print("\n");

		int a;
		int b;

		a = Integer.parseInt(System.console().readLine());
		b = Integer.parseInt(System.console().readLine());

		if (a > b)
		{
			System.out.print(a + "\n");
			System.out.print(b + "\n");
			System.out.print("pierwsza liczba jest wieksza od drugiej\n");

		}

		else
		{
			System.out.print(b + "\n");
			System.out.print(a + "\n");
			System.out.print("pierwsza liczba nie jest wieksza od drugiej\n");

		}

	}


}