public class Main
{
	/*
	Suma liczb naturalnych mniejszych od N.
	*/

	public static int sumaV1(int N)
	{

		if (N <= 0)
		{
			return 0;
		}

		return N + sumaV1(N - 1);
	}

	public static void test1()
	{
		int N = 10;
		int wynik = 55;

		assert sumaV1(N) == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}

}