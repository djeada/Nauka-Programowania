import java.util.*;

public class Main
{
	//Otrzymujesz listę par liczb. Liczby w parze reprezentuja poczatek i
	//koniec przedzialu. Niektore przedzialy moga na siebie nachodzic. W takim
	//przypadku polacz je ze soba i zwroc liste niepokrywajacych sie przedzialow.

	public static ArrayList<Pair<Integer, Integer>> polaczPrzedzialyV1(ArrayList<Pair<Integer, Integer>> lista)
	{
		Collections.sort(lista);

		int pocz = lista.get(0).first;
		int koniec = lista.get(0).second;
		lista.erase(lista.iterator());

		ArrayList<Pair<Integer, Integer>> wynik = new ArrayList<Pair<Integer, Integer>>();

		for (var para : lista)
		{
			if (koniec >= para.first)
			{
				if (koniec < para.second)
				{
					koniec = para.second;
				}
			}
			else
			{
				wynik.add(<Integer, Integer>Pair(pocz, koniec));
				pocz = para.first;
				koniec = para.second;
			}
		}

		wynik.add(<Integer, Integer>Pair(pocz, koniec));

		return new ArrayList<Pair<Integer, Integer>>(wynik);
	}

	public static void test1()
	{
		ArrayList<Pair<Integer, Integer>> lista = new ArrayList<Pair<Integer, Integer>>(Arrays.asList({23, 67}, {23, 53}, {45, 88}, {77, 88}, {10, 22}, {11, 12}, {42, 45}));

		ArrayList<Pair<Integer, Integer>> wynik = new ArrayList<Pair<Integer, Integer>>(Arrays.asList({10, 22}, {23, 88}));
		assert polaczPrzedzialyV1(lista) == wynik;
	}

	public static void main(String[] args)
	{
		test1();
	}

}