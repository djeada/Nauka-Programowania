import java.util.*;

public class Main
{
	//Otrzymujesz liste n wspolczynnikow wielomianu postaci
	//a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe x.
	//Oblicz wartosc wspolczynnikow wielomianu po
	//przemnozeniu przez liczbe x.
	public static ArrayList<Integer> iloczyn(ArrayList<Integer> lista, int x)
	{

		ArrayList<Integer> wynik = new ArrayList<Integer>();

		for (var liczba : lista)
		{
			wynik.add(liczba * x);
		}

		return new ArrayList<Integer>(wynik);
	}

	public static void test1()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 2, 1));
		int x = 2;
		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(6, 4, 2));
		assert iloczyn(lista, x) == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}

}