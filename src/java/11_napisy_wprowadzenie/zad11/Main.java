import java.util.*;

public class Main {
	//Otrzymujesz napis reprezuntajacy zdanie.
	//Znajdz srednia dlugosc slow w zdaniu.
	//Znaki interpunkcyjne nie sa liczone jako slowa.

	public static String wyczysc(String napis) {
		napis = napis.trim();

		return napis.replaceAll("\\p{Punct}", "");
	}

	public static int srednia(final String napis) {
		int calk_dlugosc = 0;
		int n = 0;
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				slowo = wyczysc(slowo);
				if (!slowo.isEmpty()) {
					n++;
					calk_dlugosc += slowo.length();
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			slowo = wyczysc(slowo);
			if (!slowo.isEmpty()) {
				n++;
				calk_dlugosc += slowo.length();
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
