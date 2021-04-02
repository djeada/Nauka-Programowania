public class Main
{
	//Znajdz min/maks dwoch liczb bez uzycia instrukcji warunkowej.

	public static int znak(int n)
	{

		return (n >> 31) & 0x01;
	}

	// a >= b : znakA = 1, znakB = 0;
	// a < b : znakA = 0, znakB = 1;
	public static int maks(int a, int b)
	{
		int znakB = znak(a - b);
		int znakA = znakB ^ 1;
		return znakA * a + znakB * b;
	}

	public static int min(int a, int b)
	{
		int znakB = znak(a - b);
		int znakA = znakB ^ 1;
		return znakB * a + znakA * b;
	}

	public static void test1()
	{
		int a = 10;
		int b = 8;
		int wynik = a;

		assert maks(a, b) == wynik;
	}

	public static void test2()
	{
		int a = 10;
		int b = 8;
		int wynik = b;

		assert min(a, b) == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}