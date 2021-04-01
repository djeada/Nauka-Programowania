import java.util.*;

public class Main
{
	//Otrzymujesz dwie posortowane listy.
	//Polacz je w posortowana liste.

	//Zlozonosc obliczeniowa O(n)
	//Zlozonosc pamieciowa O(n)
	public static ArrayList<Integer> polaczV1(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{

		if (listaA.isEmpty())
		{
			return listaB;
		}

		if (listaB.isEmpty())
		{
			return listaA;
		}

		ArrayList<Integer> wynik = new ArrayList<Integer>();

		int i = 0;
		int j = 0;

		while (i < listaA.size() && j < listaB.size())
		{
			if (listaA.get(i) < listaB.get(j))
			{
				wynik.add(listaA.get(i));
				i++;
			}
			else
			{
				wynik.add(listaB.get(j));
				j++;
			}
		}

		for (int k = i; k < listaA.size(); k++)
		{
			wynik.add(listaA.get(k));
		}

		for (int k = j; k < listaB.size(); k++)
		{
			wynik.add(listaB.get(k));
		}

		return new ArrayList<Integer>(wynik);
	}

	public static void test1()
	{
		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(5, 7, 11));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(1, 3, 8, 14));

		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 3, 5, 7, 8, 11, 14));
		assert wynik.equals(polaczV1(listaA, listaB));
	}

	public static void main(String[] args)
	{

		test1();

	}

}
