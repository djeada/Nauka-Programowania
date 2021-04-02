public class Main
{

public static void oblicz(int n, RefObject<Integer> wynikA, RefObject<Integer> wynikB)
{
	oblicz(n, wynikA, wynikB, "AB");
}
	/*
	Gracz A oraz gracz B graja w kapsle.
	Na poczatku gry otrzymuja pewna liczbe kapsli.
	W kazdej turze grac moze z puli kapsli zabrac 1, 2 badz 4 kapsle.
	Gracz, ktory zabral ostatni kapsel wygyrwa.
	Gre rozpoczyna gracz A.
	Znajdz liczbe mozliwych kombinacji wybrania liczby kapsli w danej turze
	prowadzaca do zwyciestwa kazdego z graczy.
	*/

	public static void oblicz(int n, RefObject<Integer> wynikA, RefObject<Integer> wynikB, String s)
	{

		if (n <= 0)
		{
			return;
		}

		if (n == 1 || n == 2 || n == 4)
		{

			if (s.charAt(0) == 'A')
			{
				wynikA.argValue++;
			}

			else
			{
				wynikB.argValue++;
			}

			return;
		}

		else
		{
			var temp = s.charAt(0);
			s = StringFunctions.changeCharacter(s, 0, s.charAt(1));
			s = StringFunctions.changeCharacter(s, 1, temp);

			oblicz(n - 1, wynikA, wynikB, s);
			oblicz(n - 2, wynikA, wynikB, s);
			oblicz(n - 4, wynikA, wynikB, s);
		}
	}

	public static void test1()
	{
		int wynikA = 0;
		int wynikB = 0;

	RefObject<Integer> tempRef_wynikA = new RefObject<Integer>(wynikA);
	RefObject<Integer> tempRef_wynikB = new RefObject<Integer>(wynikB);
		oblicz(1, tempRef_wynikA, tempRef_wynikB);
		wynikB = tempRef_wynikB.argValue;
		wynikA = tempRef_wynikA.argValue;
		assert wynikA == 1;
		assert wynikB == 0;
	}

	public static void test2()
	{
		int wynikA = 0;
		int wynikB = 0;
	RefObject<Integer> tempRef_wynikA = new RefObject<Integer>(wynikA);
	RefObject<Integer> tempRef_wynikB = new RefObject<Integer>(wynikB);
		oblicz(3, tempRef_wynikA, tempRef_wynikB);
		wynikB = tempRef_wynikB.argValue;
		wynikA = tempRef_wynikA.argValue;
		assert wynikA == 0;
		assert wynikB == 2;
	}

	public static void test3()
	{
		int wynikA = 0;
		int wynikB = 0;
	RefObject<Integer> tempRef_wynikA = new RefObject<Integer>(wynikA);
	RefObject<Integer> tempRef_wynikB = new RefObject<Integer>(wynikB);
		oblicz(10, tempRef_wynikA, tempRef_wynikB);
		wynikB = tempRef_wynikB.argValue;
		wynikA = tempRef_wynikA.argValue;
		assert wynikA == 33;
		assert wynikB == 27;
	}

	public static void main(String[] args)
	{

		test1();
		test2();
		test3();

	}

}
