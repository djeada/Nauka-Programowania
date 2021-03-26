public class GlobalMembers
{
	//Usun wszystkie wystapienia klucza z listy.
	//Kolejnosc elementow w liscie powinna zostac zachowana.

	public static void usunPierwszeWystapienieV1(ArrayList<Integer> lista, int klucz)
	{
		Iterator<Integer> it = lista.iterator();
		while (it.hasNext())
		{
			if (it.next() == klucz)
			{
				it.copyFrom(lista.erase(it));
				return;
			}
			else
			{
			}
		}
	}

	//Zlozonosc Czasowa O(n^2)
	//erase przesuwa wszystkie elementy wiec sam ma zlozonosc O(n)
	public static void usunWszystkieWystapieniaV1(ArrayList<Integer> lista, int klucz)
	{
		Iterator<Integer> it = lista.iterator();
		while (it.hasNext())
		{
			if (it.next() == klucz)
			{
				it.copyFrom(lista.erase(it));
			}

			else
			{
			}
		}
	}

	//Zlozonosc Czasowa O(n)
	public static void usunWszystkieWystapieniaV2(ArrayList<Integer> lista, int klucz)
	{
		lista.erase(std::remove(lista.iterator(), lista.end(), klucz), lista.end());
	}

	public static void test1()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(6, 7, 2, 1, 8));
		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(6, 7, 1, 8));
		int klucz = 2;

		usunWszystkieWystapieniaV1(lista, klucz);

		assert lista == wynik;
	}

	public static void test2()
	{
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(6, 7, 2, 1, 8));
		ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(6, 7, 1, 8));
		int klucz = 2;

		usunWszystkieWystapieniaV2(lista, klucz);

		assert lista == wynik;
	}

	public static void main(String[] args)
	{

		test1();
		test2();

	}

}