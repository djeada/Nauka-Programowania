public class Main
{
	//Konwersja miedzy dowolnymi systemami liczbowymi.
	public static int naDec(String liczba, int podstawa)
	{
		int wartoscDec = 0;

		for (int i = liczba.length() - 1; i >= 0; i--)
		{

			if (liczba.charAt(i) >= 'A' && liczba.charAt(i) < 'Z')
			{
				wartoscDec += (liczba.charAt(i) - 'A' + 10) * Math.pow(podstawa, (liczba.length() - 1 - i));
			}

			else
			{
				wartoscDec += (liczba.charAt(i) - '0') * Math.pow(podstawa, (liczba.length() - 1 - i));
			}
		}

		return wartoscDec;
	}

	public static void zmianaPodstawy(RefObject<String> liczba, int podstawa, int nowaPodstawa)
	{

		if (podstawa > (10 + 'Z' - 'A'))
		{
			return;
		}

		int wartoscDec = naDec(liczba.argValue, podstawa);
		liczba.argValue = "";
		podstawa = nowaPodstawa;

		while (wartoscDec > 0)
		{
			int reszta = wartoscDec % podstawa;
			wartoscDec /= podstawa;

			char nowyZnak = '0' + reszta;

			if (nowyZnak > '9')
			{
				nowyZnak = 'A' + (nowyZnak - '9') - 1;
			}

			liczba.argValue += nowyZnak;
		}

		reverse(liczba.argValue.iterator(), liczba.argValue.end());
	}

	public static void test1()
	{
		String liczba = "4301";
		String wynik = "1003031";
	RefObject<String> tempRef_liczba = new RefObject<String>(liczba);
		zmianaPodstawy(tempRef_liczba, 10, 4);
		liczba = tempRef_liczba.argValue;

		assert liczba.equals(wynik);
	}

	public static void main(String[] args)
	{

		test1();
	}

}