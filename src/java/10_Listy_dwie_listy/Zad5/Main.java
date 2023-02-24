import java.util.*;

public class Main
{
	//Otrzymujesz dwie listy: wagi oraz wartosci.
	//Znajdz srednia wazona wartosci.
	public static double sredniaWazona(ArrayList<Double> wagi, ArrayList<Double> wartosci)
	{

		assert wagi.size() == wartosci.size();

		double suma = 0.0;

		for (var liczba: wartosci) {
			suma += liczba;
		}

		double sumaIloczynow = 0.0;

		for (int i = 0; i < wartosci.size(); i++)
		{
			sumaIloczynow += (wartosci.get(i) * wagi.get(i));
		}

		return sumaIloczynow / suma;
	}

	public static void test1()
	{
		ArrayList<Double> wartosci = new ArrayList<Double>(Arrays.asList(0.0, -23.0, -5.0, 2.0, -3.0, 4.0, 9.0));
		ArrayList<Double> wagi = new ArrayList<Double>(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0));

		double wynik = -1.1875;
		assert sredniaWazona(wagi, wartosci) == wynik;
	}

	public static void test2()
	{
		ArrayList<Double> wartosci = new ArrayList<Double>(Arrays.asList(2.0, 5.0, 0.0, 2.0, 1.0));
		ArrayList<Double> wagi = new ArrayList<Double>(Arrays.asList(0.2, 0.4, 0.1, 0.2, 0.1));

		double wynik = 0.29;
		assert sredniaWazona(wagi, wartosci) == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();
	}
}
