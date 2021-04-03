import java.util.*;

public class Main {
	//Znajdz wszystkie permutacje slowa bedace palindromami.

	public static boolean palindrom(String slowo) {
		int N = slowo.length() - 1;
		for (int i = 0; i<= N / 2; i++) {
			if (slowo.charAt(i) != slowo.charAt(N - i)) {
				return false;
			}
		}

		return true;
	}

	public static void permutacja(String slowoWej, String slowoWyj, ArrayList<String> wynik) {
		if (slowoWej.isEmpty() && palindrom(slowoWyj) && !wynik.contains(slowoWyj)) {
			wynik.add(slowoWyj);
			return;
		}

		for (int i = 0; i<slowoWej.length(); ++i) {
			String noweSlowoWej = slowoWej;
			String noweSlowoWyj = slowoWyj;

			noweSlowoWej = noweSlowoWej.substring(0, i) + noweSlowoWej.substring(i + 1);
			noweSlowoWyj += slowoWej.charAt(i);
			permutacja(noweSlowoWej, noweSlowoWyj, wynik);
		}
	}

	public static ArrayList<String> permutacje(String slowoWej) {

		ArrayList<String> wynik = new ArrayList<String> ();

		String slowoWyj = "";
		permutacja(slowoWej, slowoWyj, wynik);

		return new ArrayList<String> (wynik);
	}

	public static boolean wektoryRowne(ArrayList<String> v1, ArrayList<String> v2) {
		Collections.sort(v1);
		Collections.sort(v2);
		return v1.equals(v2);
	}

	public static void test1() {
		String slowo = "adamm";
		ArrayList<String> wynik = new ArrayList<String> (Arrays.asList("madam", "amdma"));

		assert wektoryRowne(permutacje(slowo), wynik);
	}

	public static void main(String[] args) {
		test1();
	}

}
