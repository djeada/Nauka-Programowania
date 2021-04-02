import java.util.*;

public class Main
{
	//Policz z ilu zer i jedynek sklada sie otrzymana liczba.

	public static int policzUstawioneBity(int liczba)
	{
		int suma = 0;

		while (liczba > 0)
		{
			if ((liczba & 1) != 0)
			{
				suma++;
			}
			liczba >>= 1;
		}

		return suma;
	}

	public static void przygotujTablice(ArrayList<Integer> tablica)
	{

		tablica.clear();

		for (int i = 0; i < 256; i++)
		{
			tablica.add(policzUstawioneBity(i));
		}
	}

	public static int liczbaBitow(int liczba)
	{
		return (int)log2(liczba) + 1;
	}

	public static int zera(int liczba, ArrayList<Integer> tablica)
	{
		return liczbaBitow(liczba) - tablica.get(liczba & 0xff) + tablica.get((liczba >> 8) & 0xff) + tablica.get((liczba >> 16) & 0xff) + tablica.get((liczba >> 24) & 0xff);
	}

	public static int jedynki(int liczba, ArrayList<Integer> tablica)
	{

		return tablica.get(liczba & 0xff) + tablica.get((liczba >> 8) & 0xff) + tablica.get((liczba >> 16) & 0xff) + tablica.get((liczba >> 24) & 0xff);
	}

	public static void test1(ArrayList<Integer> tablica)
	{
		int liczba = 10;
		int wynik = 2;

		assert jedynki(liczba, tablica) == wynik;
	}

	public static void test2(ArrayList<Integer> tablica)
	{
		int liczba = 7;
		int wynik = 3;

		assert jedynki(liczba, tablica) == wynik;
	}

	public static void test3(ArrayList<Integer> tablica)
	{
		int liczba = 10;
		int wynik = 2;

		assert zera(liczba, tablica) == wynik;
	}

	public static void test4(ArrayList<Integer> tablica)
	{
		int liczba = 7;
		int wynik = 0;

		assert zera(liczba, tablica) == wynik;
	}

	public static void main(String[] args)
	{

		ArrayList<Integer> tablica = new ArrayList<Integer>();
		przygotujTablice(tablica);

		test1(tablica);
		test2(tablica);
		test3(tablica);
		test4(tablica);

	}

}