import java.util.*;

public class Main {
	//Otrzymujesz napis reprezentujacy zdanie oraz slowo.
	//Znajdz wszystkie anagramy otrzymanego slowa w zdaniu.
	//Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

	public static boolean anagram(String s1, String s2) {

		int N = s1.length();
		int M = s2.length();

		if (N != M) {
			return false;
		}

		int[] pom = new int[256];

		for (int znak: s1.toCharArray()) {
			pom[znak]++;
		}

		for (int znak: s2.toCharArray()) {
			pom[znak]--;
		}

		for (var x: pom) {
			if (x != 0) {
				return false;
			}
		}

		return true;
	}

	public static String wyczysc(String napis) {
		napis = napis.trim();
		return napis.replaceAll("\\p{Punct}", "");
	}

	public static ArrayList<String> anagramyV1(final String zdanie, final String napis) {
		ArrayList<String> wynik = new ArrayList<String> ();
		int pocz = 0;
		int konc = 0;
		while ((konc = zdanie.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = zdanie.substring(pocz, konc);
				slowo = wyczysc(slowo);
				slowo = slowo.toLowerCase();
				if (!slowo.isEmpty() && anagram(slowo, napis)) {
					wynik.add(slowo);
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = zdanie.substring(pocz);
			slowo = wyczysc(slowo);
			slowo = slowo.toLowerCase();
			if (!slowo.isEmpty() && anagram(slowo, napis)) {
				wynik.add(slowo);
			}
		}

		return new ArrayList<String> (wynik);
	}

	public static void test1() {
		String zdanie = "Za jego nikczemne uczynki, spotakla go wysoce sroga kara.";
		String slowo = "arak";
		ArrayList<String> wynik = new ArrayList<String> (Arrays.asList("kara"));
		assert wynik.equals(anagramyV1(zdanie, slowo));
	}

	public static void main(String[] args) {
		test1();

	}

}
