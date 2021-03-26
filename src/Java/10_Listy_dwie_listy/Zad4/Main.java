public class GlobalMembers
{
	//Otrzymujesz dwie listy liczb reprezentujacych
	//wspolrzedne dwoch wektorow. Zrealizuj:
	//a) mnozenie sklarne.
	public static int mnozenieSkalarne(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{

		assert listaA.size() == listaB.size();

		int wynik = 0;

		for (int i = 0; i < listaA.size(); i++)
		{
			wynik += listaA.get(i) * listaB.get(i);
		}

		return wynik;
	}

	//b) mnozenie wektorowe.
	public static ArrayList<Integer> mnozenieWektorowe(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{

		assert listaA.size() == listaB.size() && listaA.size() == 3;

		ArrayList<Integer> wynik = new ArrayList<Integer>();
		wynik.add(listaA.get(1) * listaB.get(2) - listaA.get(2) * listaB.get(1));
		wynik.add(listaA.get(2) * listaB.get(0) - listaA.get(0) * listaB.get(2));
		wynik.add(listaA.get(0) * listaB.get(1) - listaA.get(1) * listaB.get(0));

		return new ArrayList<Integer>(wynik);
	}

	public static void test1()
	{
		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, -5, 4));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(2, 6, 5));

		int iloczynSkalar = -4;
		assert mnozenieSkalarne(listaA, listaB) == iloczynSkalar;
	}

	public static void test2()
	{
		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, -5, 4));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(2, 6, 5));

		ArrayList<Integer> iloczynWekt = new ArrayList<Integer>(Arrays.asList(-49, -7, 28));
		assert mnozenieWektorowe(listaA, listaB) == iloczynWekt;
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}