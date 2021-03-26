public class GlobalMembers
{
	//Otrzymujesz liste liczb, wykonaj nastepujace polecenia:

	//a)Zwieksz o 1 wszystkie elementy stojace na parzystych indeksach.
	public static void zwieksz(ArrayList<Integer> lista)
	{
		for (int i = 0; i < lista.size(); i++)
		{
			if (i % 2 == 0)
			{
				lista.get(i)++;
			}
		}
	}

	//b)Wyzeruj wszystkie wielokrotnosci liczby 3.
	public static void wyzeruj(ArrayList<Integer> lista)
	{

		for (var liczba : lista)
		{
			if (liczba % 3 == 0)
			{
				liczba = 0;
			}
		}
	}

	//c)Podnies do kwadratu wszystkie elementy mniejsze niz 10.
	public static void kwadrat(ArrayList<Integer> lista)
	{

		for (var liczba : lista)
		{
			if (liczba < 10)
			{
				liczba = Math.pow(liczba, 2);
			}
		}
	}

	//d)Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.
	public static int czyPierwsza(int n)
	{

		if ((!(n % 2) && n != 2) || n < 1)
		{
			return false;
		}

		for (int i = 3; i <= Math.sqrt((double)n); i += 2)
		{
			if ((n % i) == 0)
			{
				return false;
			}
		}

		return true;
	}

	public static void suma(ArrayList<Integer> lista)
	{
		int suma = accumulate(lista.iterator(), lista.end(), 0);

		for (int i = 0; i < lista.size(); i++)
		{
			if (czyPierwsza(i) != 0)
			{
				lista.set(i, suma);
			}
		}
	}

	//e)Zamien kazdy element na iloczyn wszystkich elementow list poza nim samym.

	public static void zamien(tangible.RefObject<ArrayList<Integer>> lista)
	{

		ArrayList<Integer> iloczyny = new ArrayList<Integer>();

		for (int i = 0; i < lista.argValue.size(); i++)
		{
			int iloczyn = 1;

			for (int j = 0; j < lista.argValue.size(); j++)
			{
				if (j == i)
				{
					continue;
				}

				iloczyn *= lista.argValue.get(j);
			}

			iloczyny.add(iloczyn);
		}

		lista.argValue = iloczyny;
	}

	public static void test1()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(4, 5, -6, 4, 10, -11, 3));
		zwieksz(lista);
		assert lista == wynik;
	}

	public static void test2()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(0, 5, -7, 4, 0, -11, 2));
		wyzeruj(lista);
		assert lista == wynik;
	}

	public static void test3()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(3, 5, 5, 5, 9, 5, 2));
		suma(lista);
		assert lista == wynik;
	}

	public static void test4()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(27720, 16632, -11880, 20790, 9240, -7560, 41580));
	tangible.RefObject<java.util.ArrayList<Integer>> tempRef_lista = new tangible.RefObject<java.util.ArrayList<Integer>>(lista);
		zamien(tempRef_lista);
		lista = tempRef_lista.argValue;
		assert lista == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();
		test3();
		test4();

	}

}

public final class RefObject<T>
{
	public T argValue;
	public RefObject(T refArg)
	{
		argValue = refArg;
	}
}