public class Main
{
	// Przy uzyciu operatorow bitowych:
	//a) Zamien wielkie litery na male.
	public static String wielkieNaMale(String slowo)
	{
		String wynik = "";

		for (int litera : slowo)
		{
			wynik += (char)(litera | (int)' ');
		}

		return wynik;
	}

	//b) Zamien male litery na wielkie.
	public static String maleNaWielkie(String slowo)
	{
		String wynik = "";

		for (int litera : slowo)
		{
			wynik += (char)(litera & (int)'_');
		}

		return wynik;
	}

	//c) Zamien male litery na wielkie i wielkie na male.
	public static String odwrocWielkoscLiter(String slowo)
	{

		String wynik = "";

		for (int litera : slowo)
		{

			if (litera >= 'a' && litera <= 'z')
			{
				wynik += (char)(litera ^ (int)' ');
			}

			else if (litera >= 'A' && litera <= 'Z')
			{
				wynik += (char)(litera ^ (int)' ');
			}

			else
			{
				wynik += (char)litera;
			}
		}

		return wynik;
	}

	public static void test1()
	{
		String slowo = "KURCZAKU";
		String wynik = "kurczaku";

		assert wynik.equals(wielkieNaMale(slowo));
	}

	public static void test2()
	{
		String slowo = "piesek";
		String wynik = "PIESEK";

		assert wynik.equals(maleNaWielkie(slowo));
	}

	public static void test3()
	{
		String slowo = "wszedl Kotek na PloteK i mrUga";
		String wynik = "WSZEDL kOTEK NA pLOTEk I MRuGA";

		assert wynik.equals(odwrocWielkoscLiter(slowo));
	}

	public static void main(String[] args)
	{

		test1();
		test2();
		test3();

	}

}