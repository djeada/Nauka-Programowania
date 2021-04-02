public class Main
{
	/*
	N-ty wyraz ciagu danego 
	wzorem rekurencyjnym.	
	1) a(1) = 1
	2) a(n) = 1 + a(n-1)*2
	*/

	public static int ciagV1(int n)
	{

		if (n == 1)
		{
			return 1;
		}

		return 1 + ciagV1(n - 1) * 2;
	}

	public static void test1()
	{
		int n = 5;
		int wynik = 31;

		assert ciagV1(n) == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}

}