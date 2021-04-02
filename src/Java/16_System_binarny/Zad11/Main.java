public class Main
{
	//Czy liczba jest palindromem?

	public static final int liczbaBitow = 8;

	public static boolean czyPalindromV1(int liczba)
	{

		std::bitset<liczbaBitow> bity = liczba;

		for (int i = 0; i < liczbaBitow / 2 - 1; i++)
		{
			if ((bity[i] ^ bity[liczbaBitow - 1 - i]) != 0)
			{
				return false;
			}
		}

		return true;
	}

	public static void test1()
	{
		int liczba = 231;
		assert czyPalindromV1(liczba);
	}

	public static void test2()
	{
		int liczba = 17;
		assert!czyPalindromV1(liczba);
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}