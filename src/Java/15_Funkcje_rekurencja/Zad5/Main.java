public class Main
{
	//Liczba Fibonacciego.

	public static int fibonnaciV1(int n)
	{

		if (n == 0 || n == 1)
		{
			return n;
		}

		return fibonnaciV1(n - 1) + fibonnaciV1(n - 2);
	}

	
	public static int[] fibonnaciV2_pom = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

	public static int fibonnaciV2(int n)
	{

		if (fibonnaciV2_pom[n] != 0)
		{
			return fibonnaciV2_pom[n];
		}

		if (n == 0 || n == 1)
		{
			fibonnaciV2_pom[n] = n;
			return fibonnaciV2_pom[n];
		}

		fibonnaciV2_pom[n] = fibonnaciV2(n - 1) + fibonnaciV2(n - 2);

		return fibonnaciV2_pom[n];
	}

	public static void test1()
	{
		int n = 7;
		int wynik = 13;

		assert fibonnaciV1(n) == wynik;
		assert fibonnaciV2(n) == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}

}