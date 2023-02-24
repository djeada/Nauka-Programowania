import java.util.*;

public class Main {
	//Napisz dwie funkcje. Pierwsza powinna porsic uzytkownika o podanie 
	//nazwy i hasla oraz zwracac otrzymane dane.

	public static  String[] inicjalizacjaDanych() {
		System.out.print("podaj nazwe oraz haslo do zapamietania\n");
		Scanner s = new Scanner(System.in);
		String nazwa = s.nextLine();
		String haslo = s.nextLine();
		return new String[] {nazwa , haslo};
	}

	//Druga powinna otrzymywac dane od pierwszej i ponownie prosic o
	//podanie nazwy oraz hasla, dopoki dane nie beda identyczne z tymi
	//podanymi za pierwszym razem.

	public static void czyDanePoprawne(String nazwa, String haslo) {

		String nowaNazwa = null;
		String noweHaslo = null;
		Scanner s = new Scanner(System.in);

		while (!nazwa.equals(nowaNazwa) || !haslo.equals(noweHaslo)) {
			System.out.print("Aby zalogowac sie do systemu: podaj nazwe oraz haslo\n");
			nowaNazwa = s.nextLine();
			noweHaslo = s.nextLine();
		}

		System.out.print("Logowanie do systemu przebieglo pomyslnie\n");
	}

	public static void main(String[] args) {

		String[] wynik = inicjalizacjaDanych();
		String nazwa = wynik[0];
		String haslo = wynik[1];
		czyDanePoprawne(nazwa, haslo);

	}

}
