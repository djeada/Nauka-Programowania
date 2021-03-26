public class GlobalMembers
{
	//Dla otrzymanej listy oraz liczby X, znajdz indeksy pierwszej
	//pary elementów listy, ktorych suma jest rowna liczbie X.
	//Jesli w liscie nie ma takiej pary, zwroc pare (-1, -1)

	public static tangible.Pair<Integer, Integer> sumaDwochV1(ArrayList<Integer> lista, int liczba)
	{
		int n = lista.size();

		for (int i = 0; i < n; i++)
		{
			for (int j = i + 1; j < n; j++)
			{
				if (lista.get(j) + lista.get(i) == liczba)
				{
					return tangible.<Integer, Integer>Pair(i, j);
				}
			}
		}

		return tangible.<Integer, Integer>Pair(-1, -1);
	}

	public static void test1()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 3, 4, 5, 2));
		int liczba = 5;
		tangible.Pair<Integer, Integer> wynik = new tangible.Pair<Integer, Integer>(0, 2);
		assert sumaDwochV1(lista, liczba) == wynik;
	}

	public static void test2()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(2, -6, 10, 21, 8));
		int liczba = 7;
		tangible.Pair<Integer, Integer> wynik = new tangible.Pair<Integer, Integer>(-1, -1);
		assert sumaDwochV1(lista, liczba) == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}

public final class Pair<T1, T2>
{
	public T1 first;
	public T2 second;

	public Pair()
	{
		first = null;
		second = null;
	}

	public Pair(T1 firstValue, T2 secondValue)
	{
		first = firstValue;
		second = secondValue;
	}

	public Pair(Pair<T1, T2> pairToCopy)
	{
		first = pairToCopy.first;
		second = pairToCopy.second;
	}
}