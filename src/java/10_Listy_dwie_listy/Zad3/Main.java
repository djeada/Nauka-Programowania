import java.util.*;

public class Main
{
	//Dla otrzymanych dwoch list, zwroc liste, ktorej
	//elemnty sa suma odpowiadajacych sobie elementow
	//otrzymanych list.

	public static ArrayList<Integer> suma(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{

		ArrayList<Integer> wynik = new ArrayList<Integer>(listaA);

		int n = wynik.size() < listaB.size() ? wynik.size() : listaB.size();

		for (int i = 0; i < n; i++)
		{
			wynik.set(i, wynik.get(i) + listaB.get(i));
		}

		for (int i = n; i < listaB.size(); i++)
		{
			wynik.add(listaB.get(i));
		}

		return new ArrayList<Integer>(wynik);
	}

	public static void test1()
	{
		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, 1, 2, 5));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(2, 8, 6, 5));

		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(5, 9, 8, 10));
		assert wynik.equals(suma(listaA, listaB));
	}

	public static void main(String[] args)
	{

		test1();

	}

}
