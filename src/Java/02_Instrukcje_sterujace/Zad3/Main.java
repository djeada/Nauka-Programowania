
public class Main
{
	public static void main(String[] args)
	{

		//Dla pobranej liczby, sprawdz czy liczba jest ujemna, dodatnia, czy jest zerem.

		System.out.print("podaj liczbe:");
		System.out.print("\n");

		int a;
		a = Integer.parseInt(System.console().readLine());

		if (a < 0)
		{
			System.out.print("libczba jest ujemna");
			System.out.print("\n");
		}
		else if (a > 0)
		{
			System.out.print("liczba jest dodatnia");
			System.out.print("\n");
		}
		else
		{
			System.out.print("liczba jest zerem");
			System.out.print("\n");
		}

	}


}