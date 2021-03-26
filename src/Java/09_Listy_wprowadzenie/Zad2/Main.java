public class GlobalMembers
{
	//Dla liczby N, wczytaj N liczb do listy, a nastepnie:
	public static void wczytaj(ArrayList<Integer> lista, int n)
	{
		for (int i = 0; i < n; i++)
		{
			int liczba;
			liczba = Integer.parseInt(ConsoleInput.readToWhiteSpace(true));
			lista.add(liczba);
		}
	}

	//a)dodaj do kazdego elementu 1;
	public static void zwieksz(ArrayList<Integer> lista)
	{
		for (var liczba : lista)
		{
			liczba += 1;
		}
	}

	//b)pomnoz kazdy element przez jego indeks;
	public static void pomnoz(ArrayList<Integer> lista)
	{
	//C++ TO JAVA CONVERTER WARNING: Unsigned integer types have no direct equivalent in Java:
	//ORIGINAL LINE: for (unsigned int i = 0; i < lista.size(); i++)
		for (int i = 0; i < lista.size(); i++)
		{
			lista.set(i, lista.get(i) * i);
		}
	}

	//c)zastap wszystkie elementy wartoscia pierwszego elementu listy.
	public static void zastap(ArrayList<Integer> lista)
	{
		if (lista.isEmpty())
		{
			return;
		}

		for (var liczba : lista)
		{
			liczba = lista.get(0);
		}
	}

	//Dla każdego podpunktu wypisz zmodyfikowaną listę. Elementy listy powinny
	//być oddzielone przecinkami i wypisane w jednym wierszu.
	public static void wypiszOdKonca(ArrayList<Integer> lista)
	{
		for (var liczba : lista)
		{
			System.out.print(liczba);
			System.out.print(", ");
		}
		System.out.print("\n");
	}

	public static void main(String[] args)
	{

		ArrayList<Integer> lista = new ArrayList<Integer>();
		int n;

		System.out.print("podaj liczbe n: ");
		n = Integer.parseInt(ConsoleInput.readToWhiteSpace(true));
		wczytaj(lista, n);

		ArrayList<Integer> kopia = new ArrayList<Integer>(lista);
		zwieksz(kopia);
		wypiszOdKonca(kopia);

		kopia = new ArrayList<Integer>(lista);
		pomnoz(kopia);
		wypiszOdKonca(kopia);

		kopia = new ArrayList<Integer>(lista);
		zastap(kopia);
		wypiszOdKonca(kopia);

	}

}