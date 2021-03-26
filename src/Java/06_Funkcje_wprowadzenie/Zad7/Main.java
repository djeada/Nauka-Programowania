public class Main {
	//Napisz dwie funkcje. Pierwsza powinna porsic uzytkownika o podanie 
	//nazwy i hasla oraz zwracac otrzymane dane.

	public static void inicjalizacjaDanych(String nazwa, String haslo) {
		System.out.print("podaj nazwe oraz haslo do zapamietania");
		System.out.print("\n");
		nazwa = System.console().readLine();
		haslo = System.console().readLine();
	}

	//Druga powinna otrzymywac dane od pierwszej i ponownie prosic o
	//podanie nazwy oraz hasla, dopoki dane nie beda identyczne z tymi
	//podanymi za pierwszym razem.

	public static void czyDanePoprawne(String nazwa, String haslo) {

		String nowaNazwa;
		String noweHaslo;

		while (!nazwa.equals(nowaNazwa) || !haslo.equals(noweHaslo)) {
			System.out.print("Aby zalogowac sie do systemu: podaj nazwe oraz haslo");
			System.out.print("\n");
			nowaNazwa = System.console().readLine();
			noweHaslo = System.console().readLine();
		}

		System.out.print("Logowanie do systemu przebieglo pomyslnie");
		System.out.print("\n");
	}

	public static void main(String[] args) {
		String nazwa;
		String haslo;
		inicjalizacjaDanych(nazwa, haslo);
		czyDanePoprawne(nazwa, haslo);

	}

}
