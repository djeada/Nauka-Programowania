
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

	//a) wypisz liste od poczatku do konca. Elementy listy powinny
	//znajdowac sie w osobnych wierszach.
	public static void wypiszOdPoczatku(ArrayList<Integer> lista)
	{
		for (var liczba : lista)
		{
			System.out.print(liczba);
			System.out.print("\n");
		}
	}

	//b) wypisz liste od konca. Elementy listy powinny byc oddzielone
	//przecinkami i wypisane w jednym wierszu.
	public static void wypiszOdKonca(ArrayList<Integer> lista)
	{
		var it = cend(lista);
		while (it != cbegin(lista))
		{
			System.out.print((--it));
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
		wypiszOdPoczatku(lista);
		wypiszOdKonca(lista);

	}

}