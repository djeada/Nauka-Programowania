public class Main
{
	//Znajdz dlugosc najdluzszego ciagu zer w liczbie binarnej.

	public static int najdluzszyCiagZer(int liczba)
	{
		if (liczba == 0)
		{
			return 1;
		}

		int wynik = 0;
		int pom = 0;

		while (liczba != 0)
		{
			int reszta = liczba % 2;
			liczba /= 2;
			if (reszta == 1)
			{
				wynik = Math.max(wynik, pom);
				pom = 0;
			}
			else
			{
				pom++;
			}
		}
		return Math.max(wynik, pom);
	}

	public static void test1()
	{
		int liczba = 111;
		int wynik = 1;

		assert najdluzszyCiagZer(liczba) == wynik;
	}

	public static void test2()
	{
		int liczba = 8219;
		int wynik = 8;

		assert najdluzszyCiagZer(liczba) == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}