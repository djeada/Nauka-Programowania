
public class Main
{
	public static void main(String[] args)
	{

		//Dla pobranej liczby, powinna zostac wyswietlona suma 
		//wszystkich liczb naturalnych mniejszych od pobranej liczby.

		System.out.print("Podaj liczbe: ");
		System.out.print("\n");
		int n;
		n = Integer.parseInt(System.console().readLine());

		int suma = 0;

		for (int i = 1; i < n; i++)
		{
			suma += i;
		}

		System.out.print(suma);
		System.out.print("\n");

	}

}