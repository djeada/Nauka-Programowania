
public class Main
{
	//Napisz funkcje, ktora dla otrzymanych dwoch liczb 
	//przy pomocy petli obliczy ile wynosi a podniesione do b.

	public static double potega(int a, int b)
	{
		int wynik = 1;
		for (int i = 0; i < Math.abs(b); i++)
		{
			wynik *= a;
		}

		if (b < 0)
		{
			return 1 / wynik;
		}

		return wynik;
	}

	public static void test1()
	{
		int a = 2;
		int b = 3;
		double wynik = 8.00;

		assert Math.abs(potega(a, b) - wynik) < 0.01;
	}

	public static void test2()
	{
		int a = 10;
		int b = -5;
		double wynik = 0.00001;

		assert Math.abs(potega(a, b) - wynik) < 0.01;
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}