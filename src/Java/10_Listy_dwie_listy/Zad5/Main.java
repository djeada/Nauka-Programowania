public class GlobalMembers
{
	//Otrzymujesz dwie listy: wagi oraz wartosci.
	//Znajdz srednia wazona wartosci.
	public static double sredniaWazona(ArrayList<Double> wagi, ArrayList<Double> wartosci)
	{

		assert wagi.size() == wartosci.size();

		double suma = accumulate(wartosci.iterator(), wartosci.end(), 0);
		double sumaIloczynow = 0;

		for (int i = 0; i < wartosci.size(); i++)
		{
			sumaIloczynow += (wartosci.get(i) * wagi.get(i));
		}

		return sumaIloczynow / suma;
	}

	public static void test1()
	{
		ArrayList<Double> wartosci = new ArrayList<Double>(Arrays.asList(0, -23, -5, 2, -3, 4, 9));
		ArrayList<Double> wagi = new ArrayList<Double>(Arrays.asList(1, 2, 3, 4, 5, 6, 7));

		double wynik = -1.1875;
		assert sredniaWazona(wagi, wartosci) == wynik;
	}

	public static void test2()
	{
		ArrayList<Double> wartosci = new ArrayList<Double>(Arrays.asList(2, 5, 0, 2, 1));
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