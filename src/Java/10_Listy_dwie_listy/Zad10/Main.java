import java.util.*;

public class Main
{
	//Otrzymujesz dwie posortowane listy rownej
	//dlugosci. Znajdz ich mediane.

	//Zlozonosc obliczeniowa O(m + n)
	//Zlozonosc pamieciowa O(1)
	public static double mediana(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{
		int i = 0;
		int j = 0;
		int n = listaA.size();
		int m = listaB.size();
		double m1 = -1;
		double m2 = -1;

		for (int licznik = 0; licznik <= (n + m) / 2; licznik++)
		{
			if ((m + n) % 2 == 0)
			{
				m2 = m1;
			}

			if (i != n && j != m)
			{
				m1 = (listaA.get(i) > listaB.get(j)) ? listaB.get(j++) : listaA.get(i++);
			}

			else if (i < n)
			{
				m1 = listaA.get(i++);
			}

			else
			{
				m1 = listaB.get(j++);
			}
		}

		if ((m + n) % 2 == 1)
		{
			return m1;
		}

		return (m1 + m2) / 2.00;
	}

	public static void test1()
	{
		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(2, 4, 7));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(3, 5, 9));

		double wynik = 4.5;
		assert mediana(listaA, listaB) == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}

}
