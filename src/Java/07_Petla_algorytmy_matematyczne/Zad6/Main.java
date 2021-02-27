
public class Main
{
	//Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci
	//ich najmniejsza wspolna wielokrotnosc.

	public static int nwd(int a, int b)
	{

		int c;

		while (b != a % b)
		{
			c = b;
			b = a % b;
			a = c;

		   if (b == 0)
		   {
			   break;
		   }
		}

		return a;
	}

	public static int nww(int a, int b)
	{
		return a * b / nwd(a, b);
	}

	public static void test1()
	{
		int a = 14;
		int b = 21;
		int wynik = 42;

		assert nww(a, b) == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}



}