import java.util.*;

public class Main {
	//Otrzymujesz napis reprezentujacy zdanie.
	//Znajdz wszystkie palindromy w zdaniu.
	//Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

	public static boolean palindrom(String slowo) {
		int N = slowo.length() - 1;
		for (int i = 0; i<= N / 2; i++) {
			if (slowo.charAt(i) != slowo.charAt(N - i)) {
				return false;
			}
		}

		return true;
	}

	public static String wyczysc(String napis) {
		napis = napis.trim();
		return napis.replaceAll("\\p{Punct}", "");
	}

	public static ArrayList<String> palindromyV1(String napis) {
		ArrayList<String> wynik = new ArrayList<String> ();
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				slowo = wyczysc(slowo);
				slowo = slowo.toLowerCase();
				if (!slowo.isEmpty() && palindrom(slowo)) {
					wynik.add(slowo);
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			slowo = wyczysc(slowo);
			slowo = slowo.toLowerCase();
			if (!slowo.isEmpty() && palindrom(slowo)) {
				wynik.add(slowo);
			}
		}

		return new ArrayList<String> (wynik);
	}

	public static void test1() {
		String napis = "Tata zbaral kajak na wycieczke i uderzyl sie w oko";
		ArrayList<String> wynik = new ArrayList<String> (Arrays.asList("kajak", "i", "w", "oko"));
		assert wynik.equals(palindromyV1(napis));
	}

	public static void main(String[] args) {
		test1();

	}

}
