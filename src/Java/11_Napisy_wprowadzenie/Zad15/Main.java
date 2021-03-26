import java.util.*;

public class GlobalMembers {
	//Otrzymujesz napis reprezentajacy zdanie.
	//Zwroc liste skladajaca sie ze slow zdania.
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

	public static ArrayList<String> slowaV1(String napis) {
		ArrayList<String> wynik = new ArrayList<String> ();
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				wyczysc(slowo);
				if (!slowo.empty()) {
					wynik.add(slowo);
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			wyczysc(slowo);
			if (!slowo.empty()) {
				wynik.add(slowo);
			}
		}

		return new ArrayList<String> (wynik);
	}

	public static void test1() {
		String napis = "We think in generalities, but we live in details";
		ArrayList<String> wynik = new ArrayList<String> (Arrays.asList("We", "think", "in", "generalities", "but", "we", "live", "in", "details"));
		assert slowaV1(napis) == wynik;
	}

	public static void test2() {
		String napis = "";
		ArrayList<String> wynik = new ArrayList<String> ();
		assert slowaV1(napis) == wynik;
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}