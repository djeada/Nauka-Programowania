import java.util.*;

public class Main
{
	//Otrzymujesz liste 2d. Obroc otrzymana liste o 90 stopni.
	//Tzn. zamien miejscami ostatnia kolumne, z ostatnim wierszem,
	//przedostatnią kolumnę z przedostatnim wierszem itd.

	public static void obroc(ArrayList<ArrayList<Integer>> macierz)
	{

		int N = macierz.size();

		for (int i = 0; i < N / 2; i++)
		{
			int first = i + 1;
			int last = N - 1 - i;

			for (int j = first; j < last; j++)
			{
				int pom = macierz.get(i).get(j);
				macierz.get(i).set(j, macierz.get(N - 1 - j).get(i));
				macierz.get(N - 1 - j).set(i, macierz.get(N - 1 - i).get(N - 1 - j));
				macierz.get(N - 1 - i).set(N - 1 - j, macierz.get(j).get(N - 1 - i));
				macierz.get(j).set(N - 1 - i, pom);
			}

			int pom = macierz.get(i).get(i);
			macierz.get(i).set(i, macierz.get(N - 1 - i).get(i));
			macierz.get(N - 1 - i).set(i, macierz.get(N - 1 - i).get(N - 1 - i));
			macierz.get(N - 1 - i).set(N - 1 - i, macierz.get(i).get(N - 1 - i));
			macierz.get(i).set(N - 1 - i, pom);
		}
	}

	public static void test1()
	{
		ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>>(Arrays.asList(new ArrayList<Integer>(Arrays.asList(1, 2, 3)), new ArrayList<Integer>(Arrays.asList(4, 5, 6)), new ArrayList<Integer>(Arrays.asList(7, 8, 9))));
		ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>>(Arrays.asList(new ArrayList<Integer>(Arrays.asList(7, 4, 1)), new ArrayList<Integer>(Arrays.asList(8, 5, 2)), new ArrayList<Integer>(Arrays.asList(9, 6, 3))));

		obroc(macierz);
		assert macierz == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}

}