public class Main
{
	//Dla otrzymanej listy skladajacej sie z nieparzystej
	//liczby elementow znajdz element bez pary. Przez pary
	//elementow rozumiemy tutaj elementy o rownej wartosci.

	//Zlozonosc czasowa O(n)
	//Zlozonosc pamieciowa O(n)
	public static int elementBezParyV1(ArrayList<Integer> lista)
	{
		ArrayList<Integer> pom = new ArrayList<Integer>();

		for (var liczba : lista)
		{
			var i = find(pom.iterator(), pom.end(), liczba);
			if (i != pom.end())
			{
				pom.erase(i);
			}
			else
			{
				pom.add(liczba);
			}
		}

		return pom.get(0);
	}

	//Zlozonosc czasowa O(n)
	//Zlozonosc pamieciowa O(n)
	public static int elementBezParyV2(ArrayList<Integer> lista)
	{
		int wynik = 0;

		for (var liczba : lista)
		{
			wynik ^= liczba;
		}

		return wynik;
	}

	public static void test1()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 3, 1, 7, 3, 1, 1));
		int wynik = 7;
		assert elementBezParyV1(lista) == wynik;
	}

	public static void test2()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 3, 1, 7, 3, 1, 1));
		int wynik = 7;
		assert elementBezParyV2(lista) == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}
