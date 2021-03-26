public class GlobalMembers
{
	//Znajdz takie pary elementow w liscie, ktorych suma jest rowna liczbie.
	//Element nie moze byc w parze sam ze soba.

	public static ArrayList<tangible.Pair<Integer, Integer>> znajdzParyV1(ArrayList<Integer> lista, int suma)
	{

		ArrayList<tangible.Pair<Integer, Integer>> wynik = new ArrayList<tangible.Pair<Integer, Integer>>();

	//C++ TO JAVA CONVERTER WARNING: Unsigned integer types have no direct equivalent in Java:
	//ORIGINAL LINE: for (unsigned int i = 0; i < lista.size(); i++)
		for (int i = 0; i < lista.size(); i++)
		{
	//C++ TO JAVA CONVERTER WARNING: Unsigned integer types have no direct equivalent in Java:
	//ORIGINAL LINE: for (unsigned int j = i + 1; j < lista.size(); j++)
			for (int j = i + 1; j < lista.size(); j++)
			{
				if (lista.get(i) + lista.get(j) == suma)
				{
					wynik.emplace_back(lista.get(i), lista.get(j));
				}
			}
		}

		return new ArrayList<tangible.Pair<Integer, Integer>>(wynik);
	}

	public static void test1()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(0, 4, 5, 6, 2, 9, 2, 3));
		ArrayList<tangible.Pair<Integer, Integer>> wynik = new ArrayList<tangible.Pair<Integer, Integer>>(Arrays.asList({0, 5}, {2, 3}, {2, 3}));
		int suma = 5;

		assert znajdzParyV1(lista, suma) == wynik;
	}

	public static void main(String[] args)
	{

		test1();

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