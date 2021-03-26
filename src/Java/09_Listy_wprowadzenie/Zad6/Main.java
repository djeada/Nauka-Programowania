public class GlobalMembers
{
	//Otrzymujesz liste liczb. Sprwadz czy srednia elementow
	//znajduje się w liscie. Dla sredniej nie bedacej liczba
	//calkowita, zaokraglij wynik w dol.

	public static int policzSrednia(ArrayList<Integer> lista)
	{

		int suma = 0;

		for (var liczba : lista)
		{
			suma += liczba;
		}

		return suma / lista.size();
	}

	public static boolean czySredniaWLiscie(ArrayList<Integer> lista)
	{

		int srednia = policzSrednia(lista);

		for (var liczba : lista)
		{
			if (liczba == srednia)
			{
				return true;
			}
		}

		return false;
	}

	public static void test1()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 5, -7, 4, 9, -11, 2));
		assert!czySredniaWLiscie(lista);
	}

	public static void test2()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(1, 2, 3));
		assert czySredniaWLiscie(lista);
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}