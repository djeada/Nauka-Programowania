import java.util.*;



package <missing>;

public class GlobalMembers
{
	//Otrzymujesz liczbe naturalna. Zbuduj slownik skladajacy sie
	//z kluczy bedacych kolejnymi liczbami naturalnymi mniejszymi
	//od otrzymanej liczby oraz wartosci bedacych kwadratami swoich kluczy.

	public static HashMap<Integer, Integer> budujSlownik(int liczba)
	{
		HashMap<Integer, Integer> slownik = new HashMap<Integer, Integer>();

		for (int i = 1; i < liczba; i++)
		{
			slownik.put(i, Math.pow(i, 2));
		}

		return new HashMap<Integer, Integer>(slownik);
	}

	public static void test1()
	{
		int liczba = 5;
		HashMap<Integer, Integer> wynik = new HashMap<Integer, Integer>(Map.ofEntries(Map.entry(1, 1), Map.entry(2, 4), Map.entry(3, 9), Map.entry(4, 16)));

		assert budujSlownik(liczba) == wynik;
	}

	public static void test2()
	{
		int liczba = -1;
		HashMap<Integer, Integer> wynik = new HashMap<Integer, Integer>();

		assert budujSlownik(liczba) == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}