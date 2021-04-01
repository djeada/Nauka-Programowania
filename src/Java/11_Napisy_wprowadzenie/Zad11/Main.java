public class Main {
	//Otrzymujesz napis reprezuntajacy zdanie.
	//Znajdz srednia dlugosc slow w zdaniu.
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

	public static int srednia(final String napis) {
		int calk_dlugosc = 0;
		int n = 0;
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				wyczysc(slowo);
				if (!slowo.empty()) {
					n++;
					calk_dlugosc += slowo.size();
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			wyczysc(slowo);
			if (!slowo.empty()) {
				n++;
				calk_dlugosc += slowo.size();
			}
		}

		return calk_dlugosc / n;
	}

	public static void test1() {
		String napis = "Kaczka lubi wiosne.";
		int wynik = 5;
		assert srednia(napis) == wynik;
	}

	public static void test2() {
		String napis = "Kaczka lubi wiosne.";
		int wynik = 5;
		assert srednia(napis) == wynik;
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}
