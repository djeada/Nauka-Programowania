public class GlobalMembers
{
	//Otrzymujesz dwie listy. Usun z pierwszej listy te
	//elementy, ktore wystepuja rowniez w drugiej liscie.

	//Zlozonosc obliczeniowa O(n^2)
	//Zlozonosc pamieciowa O(n)
	public static void usunCzescWspolnaV1(ArrayList<Integer> listaA, ArrayList<Integer> listaB)
	{

		var it = listaA.iterator();

		while (it.hasNext())
		{
			if (find(listaB.iterator(), listaB.end(), it.next()) != listaB.end())
			{
				it.copyFrom(listaA.erase(it));
			}
			else
			{
			}
		}
	}

	public static void test1()
	{
		ArrayList<Integer> listaA = new ArrayList<Integer>(Arrays.asList(3, 6, 2, 7, 9));
		ArrayList<Integer> listaB = new ArrayList<Integer>(Arrays.asList(4, 2, 3, 5, 6));
		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(7, 9));

		usunCzescWspolnaV1(listaA, listaB);

		assert listaA == wynik;
	}

	public static void main(String[] args)
	{

		test1();

	}

}