import java.util.*;



package <missing>;

public class GlobalMembers
{
	//Zbuduj prosta baze danych dla biblioteki oparta o slownik w ktorym kluczami
	//sa imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek.
	//Baza danych powinna umozliwiac:
	//a) dodanie wypozyczonej ksiazki do danego czytelnika;
	public static void dodajKsiazke(HashMap<String, ArrayList<String>> lista, final String uzytkownik, final String ksiazka)
	{
		if (lista.count(uzytkownik))
		{

			if (find(lista.get(uzytkownik).iterator(), lista.get(uzytkownik).end(), ksiazka) == lista.get(uzytkownik).end())
			{
				lista.get(uzytkownik).add(ksiazka);
			}

			else
			{
				System.out.print("Uzytkownik juz wypozyczyl ta ksiazke.");
				System.out.print("\n");
			}
		}

		else
		{
			ArrayList<String> ksiazki = new ArrayList<String>(Arrays.asList(ksiazka));
			lista.put(uzytkownik, ksiazki);
		}
	}

	//b) usuniecie wypozyczonej ksiazki z listy odpowiadajacej czytelnikowi;
	public static void usunKsiazke(HashMap<String, ArrayList<String>> lista, final String uzytkownik, final String ksiazka)
	{

		if (!lista.count(uzytkownik))
		{
			System.out.print("Podany uzytkownik nie znajduje sie w liscie.");
			System.out.print("\n");
			return;
		}

		if (find(lista.get(uzytkownik).iterator(), lista.get(uzytkownik).end(), ksiazka) != lista.get(uzytkownik).end())
		{
//C++ TO JAVA CONVERTER TODO TASK: There is no direct equivalent to the STL vector 'erase' method in Java:
			lista.get(uzytkownik).erase(remove(lista.get(uzytkownik).iterator(), lista.get(uzytkownik).end(), ksiazka), lista.get(uzytkownik).end());
		}

		else
		{
			System.out.print("Uzytkownik nie wypozyczyl tej ksiazki.");
			System.out.print("\n");
		}
	}

	//c) wyswietlenie aktualnej listy ksiazek dla konkretnego czytelnika oraz
	//dla wszystkich czytelnikow;
	public static void wyswietlKsiazki(HashMap<String, ArrayList<String>> lista, final String uzytkownik)
	{

		if (!lista.count(uzytkownik))
		{
			System.out.print("Podany uzytkownik nie znajduje sie w liscie.");
			System.out.print("\n");
			return;
		}

		System.out.print("Uzytkownik ");
		System.out.print(uzytkownik);
		System.out.print(" wypozyczyl nastepujace ksiazki: ");
		System.out.print("\n");

		for (var ksiazka : lista.get(uzytkownik))
		{
			System.out.print(ksiazka);
			System.out.print("\n");
		}
	}

	public static void wyswietlWszystkieKsiazki(HashMap<String, ArrayList<String>> lista)
	{

		for (var it = lista.iterator(); it != lista.end(); it++)
		{
			wyswietlKsiazki(lista, it.first);
			System.out.print("\n");
		}
	}

	public static void main(String[] args)
	{

		HashMap<String, ArrayList<String>> lista = new HashMap<String, ArrayList<String>>();

		dodajKsiazke(lista, "Pan T", "Duma i uprzedzenie – Jane Austen");
		dodajKsiazke(lista, "Pan T", "Zabić drozdad – Harper Lee");
		dodajKsiazke(lista, "Pan T", "Biblia");
		dodajKsiazke(lista, "Pan T", "Buszujący w zbożu – JD Salinger");
		dodajKsiazke(lista, "Pan T", "Rok 1984 – George Orwell");
		dodajKsiazke(lista, "Pan T", "Wedy");

		dodajKsiazke(lista, "Elzbieta", "Wielkie nadzieje – Charles Dickens");
		dodajKsiazke(lista, "Elzbieta", "Hobbit – JRR Tolkien");
		dodajKsiazke(lista, "Elzbieta", "Harry Potter – JK Rowling");

		wyswietlWszystkieKsiazki(lista);

		usunKsiazke(lista, "Elzbieta", "Hobbit – JRR Tolkien");
		usunKsiazke(lista, "Pan T", "Zabić drozdad – Harper Lee");
		usunKsiazke(lista, "Pan T", "Rok 1984 – George Orwell");

		wyswietlWszystkieKsiazki(lista);

	}

}