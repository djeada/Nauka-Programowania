import java.util.*;

public class Main
{
	//Otrzymujesz liste wspolczynnikow a, b, c rownania
	//kwadratowego ax^2 + bx + c.
	//Znajdz rzeczywiste miejsca zerowe rownania kwadratowego.
	public static Pair<Double, Double> pierwiastki(ArrayList<Integer> lista)
	{

		assert lista.size() == 3;

		Pair<Double, Double> wynik = new Pair<Double, Double>();

		int delta = lista.get(1) * lista.get(1) - 4 * lista.get(0) * lista.get(2);

		if (delta > 0)
		{
			wynik.first = (-lista.get(1) + Math.sqrt(delta)) / (2 * lista.get(0));
			wynik.second = (-lista.get(1) - Math.sqrt(delta)) / (2 * lista.get(0));
		}

		else if (delta == 0)
		{
			wynik.first = -lista.get(1) / (2 * lista.get(0));
			wynik.second = -lista.get(1) / (2 * lista.get(0));
		}

		return new Pair<Double, Double>(wynik);
	}

	public static void test1()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 1));
		Pair<Double, Double> wynik = new Pair<Double, Double>(-1, -1);
		assert pierwiastki(lista) == wynik;
	}

	public static void test2()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, -4, 5));
		Pair<Double, Double> wynik = new Pair<Double, Double>();
		assert pierwiastki(lista) == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();
	}

}