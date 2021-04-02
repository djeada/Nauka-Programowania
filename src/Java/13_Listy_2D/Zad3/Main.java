import java.util.*;

public class Main
{
	//Dla otrzymanych dwoch list, stworz dwu-kolumnowa macierz,
	//ktorej pierwsza kolumna sklada się z elementow pierwszej
	//listy, a druga drugiej. Jesli otrzymane listy nie sa rownej
	//dlugosci zwroc pusta macierz.

	public static ArrayList<Pair<Integer, Integer>> macierz(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{

		ArrayList<Pair<Integer, Integer>> macierz = new ArrayList<Pair<Integer, Integer>>();

		if (listaA.size() != listaB.size())
		{
			return new ArrayList<Pair<Integer, Integer>>(macierz);
		}

		int n = listaA.size();
		macierz.ensureCapacity(n);

		for (int i = 0; i < n; i++)
		{
			macierz.add(<Integer, Integer>Pair(listaA.get(i), listaB.get(i)));
		}

		return new ArrayList<Pair<Integer, Integer>>(macierz);
	}

	public static void test1()
	{
		ArrayList<Pair<Integer, Integer>> wynik = new ArrayList<Pair<Integer, Integer>>(Arrays.asList({3, 2}, {5, 8}, {2, 1}));
		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, 5, 2));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(2, 8, 1));
		assert macierz(new ArrayList<Integer>(listaA), new ArrayList<Integer>(listaB)) == wynik;
	}

	public static void main(String[] args)
	{
		test1();
	}

}