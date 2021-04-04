import java.util.*;

public class Main {
	//Zbuduj prosta baze danych dla biblioteki oparta o slownik w ktorym kluczami
	//sa imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek.
	//Baza danych powinna umozliwiac:
	//a) dodanie wypozyczonej ksiazki do danego czytelnika;
	public static void dodajKsiazke(HashMap<String, ArrayList<String>> lista, final String uzytkownik, final String ksiazka) {
		if (lista.containsKey(uzytkownik)) {
			ArrayList<String> ksiazki = lista.get(uzytkownik);

			if (!ksiazki.contains(ksiazka)) {
				ksiazki.add(ksiazka);
				lista.put(uzytkownik, ksiazki);
			} else {
				System.out.println("Uzytkownik juz wypozyczyl ta ksiazke.");
			}
		} else {
			ArrayList<String> ksiazki = new ArrayList<String> (Arrays.asList(ksiazka));
			lista.put(uzytkownik, ksiazki);
		}
	}

	//b) usuniecie wypozyczonej ksiazki z listy odpowiadajacej czytelnikowi;
	public static void usunKsiazke(HashMap<String, ArrayList<String>> lista, final String uzytkownik, final String ksiazka) {

		if (!lista.containsKey(uzytkownik)) {
			System.out.println("Podany uzytkownik nie znajduje sie w liscie.");
			return;
		}

		ArrayList<String> ksiazki = lista.get(uzytkownik);

		if (ksiazki.contains(ksiazka)) {
			while (ksiazki.remove(ksiazka)) {}
			lista.put(uzytkownik, ksiazki);
		} else {
			System.out.println("Uzytkownik nie wypozyczyl tej ksiazki.");
		}
	}

	//c) wyswietlenie aktualnej listy ksiazek dla konkretnego czytelnika oraz
	//dla wszystkich czytelnikow;
	public static void wyswietlKsiazki(HashMap<String, ArrayList<String>> lista, final String uzytkownik) {

		if (!lista.containsKey(uzytkownik)) {
			System.out.println("Podany uzytkownik nie znajduje sie w liscie.");
			return;
		}

		System.out.print("Uzytkownik ");
		System.out.print(uzytkownik);
		System.out.println(" wypozyczyl nastepujace ksiazki: ");

		for (var ksiazka: lista.get(uzytkownik)) {
			System.out.println(ksiazka);
		}
	}

	public static void wyswietlWszystkieKsiazki(HashMap<String, ArrayList<String>> lista) {

		for (String klucz: lista.keySet()) {
			wyswietlKsiazki(lista, klucz);
			System.out.print("\n");
		}
	}

	public static void main(String[] args) {

		HashMap<String, ArrayList<String>> lista = new HashMap<String, ArrayList<String>> ();

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
