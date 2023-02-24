import java.util.*;

public class Main
{
	//Dla liczby N, wczytaj N liczb do listy, a nastepnie:
	public static void wczytaj(ArrayList<Integer> lista, int n)
	{
		for (int i = 0; i < n; i++)
		{
			Scanner s = new Scanner(System.in);
			int liczba = Integer.parseInt(s.nextLine());
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
		for (int i = lista.size() - 1; i >= 0; i--)
		{
			System.out.print(lista.get(i));
			if (i != 0)
				System.out.print(", ");
		}

		System.out.print("\n");
	}

	public static void main(String[] args)
	{

		ArrayList<Integer> lista = new ArrayList<Integer>();
		int n;

		System.out.print("podaj liczbe n: ");
		Scanner s = new Scanner(System.in);
		n = Integer.parseInt(s.nextLine());
		wczytaj(lista, n);
		wypiszOdPoczatku(lista);
		wypiszOdKonca(lista);

	}

}
