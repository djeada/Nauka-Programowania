import java.util.*;

public class Main
{
	//Dla otrzymanych dwoch list zwroc liste powstala poprzez:
	//a) dostawienie drugiej listy na koniec pierwszej listy;
	public static ArrayList<Integer> dostaw(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{

		ArrayList<Integer> wynik = new ArrayList<Integer>(listaA);

		for (var liczba : listaB)
		{
			wynik.add(liczba);
		}

		return new ArrayList<Integer>(wynik);
	}

	//wstawienie elemntów o indeksach parzystych z drugiej
	//listy na odpowiadające im indeksy pierwszej listy.
	public static ArrayList<Integer> podmien(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{
		ArrayList<Integer> wynik = new ArrayList<Integer>(listaA);
		for (int i = 0; i < wynik.size(); i += 2)
		{
			wynik.set(i, listaB.get(i));
		}

		return new ArrayList<Integer>(wynik);
	}

	public static void test1()
	{
		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(-2, 8, 3, 6));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(7, 5, 0));

		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(-2, 8, 3, 6, 7, 5, 0));
		assert wynik.equals(dostaw(listaA, listaB));
	}

	public static void test2()
	{
		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(-2, 8, 3, 6));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(7, 5, 0));

		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(7, 8, 0, 6));
		assert wynik.equals(podmien(listaA, listaB));
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}
