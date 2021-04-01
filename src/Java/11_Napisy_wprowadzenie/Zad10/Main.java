import java.util.*;

public class Main {
	//Otrzymujesz napis reprezuntajacy zdanie.
	//Znajdz najdluzsze oraz najkrotsze slowo w zdaniu.
	//Jesli wiecej niz jedno slowo ma ekstremalna dlugosc,
	//zwroc te, ktore wystepuje w zdaniu jako pierwsze.
	//Znaki interpunkcyjne nie sa liczone jako slowa.

	public static String wyczysc(String napis) {
		napis = napis.trim();

		return napis.replaceAll("\\p{Punct}", "");
	}

	public static String najdluzsze(String napis) {
		String wynik = null;
		int dlugosc = 0;
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				slowo = wyczysc(slowo);
				
				if (slowo.length() > dlugosc) {
					wynik = slowo;
					dlugosc = slowo.length();
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			slowo = wyczysc(slowo);
			if (slowo.length() > dlugosc) {
				wynik = slowo;
				dlugosc = slowo.length();
			}
		}

		return wynik;
	}

	public static String najkrotsze(String napis) {
		String wynik = null;
		int dlugosc = napis.length();
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				slowo = wyczysc(slowo);
				
				if (slowo.length()<dlugosc) {
					wynik = slowo;
					dlugosc = slowo.length();
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			slowo = wyczysc(slowo);
			if (slowo.length()<dlugosc) {
				wynik = slowo;
				dlugosc = slowo.length();
			}
		}

		return wynik;
	}

	public static void test1() {
		String napis = "Kaczka lubi wiosne.";
		String wynik = "Kaczka";
		assert wynik.equals(najdluzsze(napis));
	}

	public static void test2() {
		String napis = "Kaczka lubi wiosne.";
		String wynik = "lubi";
		assert wynik.equals(najkrotsze(napis));
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}
