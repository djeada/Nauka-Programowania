
public class Main
{
	//Napisz funkcje, ktora dla otrzymanej liczby
	//zwroci jej pierwiastek.

	public static final float dokladnosc = 0.0001F;

	public static float pierwiastek(int a)
	{

		float wynik = a;

		while (Math.abs(a - wynik * wynik) > dokladnosc)
		{
			wynik = (wynik + a / wynik) / 2;
		}

		return wynik;

	}

	public static void test1()
	{
		int a = 16;
		int wynik = 4;

		assert Math.abs(pierwiastek(a) - wynik) <= dokladnosc;
	}

	public static void main(String[] args)
	{

		test1();

	}



}