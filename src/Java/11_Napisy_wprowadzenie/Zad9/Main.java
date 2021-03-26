import java.util.*;

public class GlobalMembers {
	//Otrzymujesz rekord z bazy danych reprezentujacy dane pracownika.
	//Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki.
	//Informacje rozdzielone sa srednikami. Zapisz je w osobnych zmiennych
	//i wypisz wraz z komunikatem.

	public static ArrayList<String> dane(String napis) {

		ArrayList<String> wynik = new ArrayList<String> ();
		std::stringstream ss = new std::stringstream(napis);

		for (String slowo; ss >> slowo;) {
			if (slowo.size() > 1) {
				wynik.add(slowo.substr(0, slowo.size() - 1));
				if (ss.peek() == ';') {
					ss.ignore();
				}
			}
		}

		return new ArrayList<String> (wynik);
	}

	public static void wypiszDane(String napis) {

		ArrayList<String> wynik = dane(napis);
		assert wynik.size() == 5;

		System.out.print("Imie: ");
		System.out.print(wynik.get(0));
		System.out.print("\n");
		System.out.print("Nazwisko: ");
		System.out.print(wynik.get(1));
		System.out.print("\n");
		System.out.print("Miejsce urodzenia: ");
		System.out.print(wynik.get(2));
		System.out.print("\n");
		System.out.print("Zawod: ");
		System.out.print(wynik.get(3));
		System.out.print("\n");
		System.out.print("Zarobki: ");
		System.out.print(wynik.get(4));
		System.out.print("\n");
	}

	public static void main(String[] args) {
		String napis = "Jan; Kowalski; Warszawa; Programista; 1000";
		wypiszDane(napis);
	}

}