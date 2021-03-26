
public class Main
{
	//Napisz funkcje, ktora dla otrzymanej liczby N
	//wypisze N pierwszych wierszy i kolumn 
	//tabliczki mnozenia.

	public static void tabliczkaMnozenia(int n)
	{

		for (int y = 1; y <= n; y++)
		{
			for (int x = 1; x <= n; x++)
			{
				System.out.print(y * x);
				System.out.print(" ");
			}
			System.out.print("\n");
		}
	}

	public static void main(String[] args)
	{

		int a = 5;
		tabliczkaMnozenia(a);

	}



}