
public class Main
{

	//Otrzymujesz liczbe, zamien ja na:
	//a) jej odpowiednik w systemie binarnym.
	public static int naDec(String liczba)
	{
		int dec = 0;
		int n = liczba.length();
		for (int i = 0; i < n; i++)
		{
			dec += Math.pow(2, n - i - 1) * (liczba.charAt(i) - '0');
		}

		return dec;
	}

	//b) jej odpowiednik w systemie dziesiętnym.
	public static String naBin(int liczba)
	{

		String bin;

		while (liczba > 0)
		{
			bin = bin.insert(0, String.valueOf(liczba % 2));
			liczba /= 2;
		}

		return bin;
	}

	public static void test1()
	{
		String liczba = "0011";
		int wynik = 3;

		assert naDec(liczba) == wynik;
	}

	public static void test2()
	{
		String liczba = "1111100";
		int wynik = 124;

		assert naDec(liczba) == wynik;
	}

	public static void test3()
	{
		int liczba = 124;
		String wynik = "1111100";

		assert wynik.equals(naBin(liczba));
	}

	public static void test4()
	{
		int liczba = 3;
		String wynik = "11";

		assert wynik.equals(naBin(liczba));
	}

	public static void main(String[] args)
	{

		test1();
		test2();
		test3();
		test4();

	}

}