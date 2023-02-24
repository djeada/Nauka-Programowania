public class Main
{
	//Napisz funkcje, ktora przy pomocy petli obliczy silnie
	//z otrzymanej liczby.

	public static int silnia(int a)
	{

		int wynik = 1;

		while (a > 0)
		{
			wynik *= a;
			a--;
		}

		return wynik;
	}

	public static void test1()
	{
		int a = 4;
		int wynik = 24;
		assert silnia(a) == wynik;
	}

	public static void test2()
	{
		int a = -5;
		int wynik = 1;
		assert silnia(a) == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}
