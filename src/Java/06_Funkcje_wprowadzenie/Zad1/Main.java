
public class Main
{
	//Napisz funkcje ktora zwroci
	//a) liczbe 3

	public static int funkcja1()
	{
		return 3;
	}

	//b) napis "Tak"
	public static String funkcja2()
	{
		return "Tak";
	}

	//c) wartosc logiczna prawda
	public static boolean funkcja3()
	{
		return true;
	}

	public static void test1()
	{
		assert funkcja1() == 3;
	}

	public static void test2()
	{
		assert funkcja2().equals("Tak");
	}

	public static void test3()
	{
		assert funkcja3();
	}

	public static void main(String[] args)
	{

		test1();
		test2();
		test3();

	}

}