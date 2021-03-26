public class GlobalMembers {
	//Otrzymujesz napis reprezuntajacy zdanie.
	//Znajdz najdluzsze oraz najkrotsze slowo w zdaniu.
	//Jesli wiecej niz jedno slowo ma ekstremalna dlugosc,
	//zwroc te, ktore wystepuje w zdaniu jako pierwsze.
	//Znaki interpunkcyjne nie sa liczone jako slowa.

	public static void wyczysc(String napis) {
		var it = napis.iterator();

		while (it != napis.end()) {
			if (ispunct( * it)) {
				napis = napis.substring(0, it);
			} else {
				it++;
			}
		}
	}

	public static String najdluzsze(String napis) {
		String wynik;
		int dlugosc = 0;
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				wyczysc(slowo);

				if (slowo.size() > dlugosc) {
					wynik = slowo;
					dlugosc = slowo.size();
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			wyczysc(slowo);
			if (slowo.size() > dlugosc) {
				wynik = slowo;
				dlugosc = slowo.size();
			}
		}

		return wynik;
	}

	public static String najkrotsze(String napis) {
		String wynik;
		int dlugosc = napis.length();
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				wyczysc(slowo);

				if (slowo.size()<dlugosc) {
					wynik = slowo;
					dlugosc = slowo.size();
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			wyczysc(slowo);
			if (slowo.size()<dlugosc) {
				wynik = slowo;
				dlugosc = slowo.size();
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