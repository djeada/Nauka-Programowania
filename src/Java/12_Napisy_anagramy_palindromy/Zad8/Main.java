import java.util.*;

public class Main {
	//Znajdz wszystkie wyjatkowe palindromy jakie mozna utworzyc ze znakow
	//w slowie (bez zmiany kolejnosci).
	//Wyjatkowy palindrom spelnia jeden z dwoch warunkow:
	//1. Wszystkie znaki sa identyczne, np. "xxx".
	//2. Wszystkie znaki poza srodkowym znakiem są identyczne, np. "ccdcc".
	//Pojedynczy znak jest rowniez uznawany za wyjatkowy palindrom.
	//Nie uwzgledniaj duplikatow w liscie.

	public static ArrayList<String> wyjatkowePalindromy(final String slowo) {
		ArrayList<String> wynik = new ArrayList<String> ();

		for (int i = 0; i<slowo.length(); i++) {
			wynik.add(String.valueOf(slowo.charAt(i)));
			int j = i + 1;
			int k = 0;
			while (j<slowo.length() && slowo.charAt(i) == slowo.charAt(j)) {
				j++;
			}

			if (j > i + 1) {
				int endIdex = 2 * i - j > 0 ? 2 * i - j : slowo.length() - i;
				String permutacja = slowo.substring(i, endIdex);
				if (!permutacja.isEmpty())
					wynik.add(permutacja);
			}

			if (j + 1<slowo.length() && slowo.charAt(i) == slowo.charAt(j + 1)) {
				k = j + 1;
			}

			while (k > i && slowo.charAt(i) == slowo.charAt(k)) {
				k--;
			}

			if (i + 1 == k) {
				String permutacja = slowo.substring(i, 2 * (j) + 1);
				if (!permutacja.isEmpty())
					wynik.add(permutacja);
			}
		}

		return new ArrayList<String> (wynik);
	}

	public static boolean wektoryRowne(ArrayList<String> v1, ArrayList<String> v2) {
		Collections.sort(v1);
		Collections.sort(v2);
		return v1.equals(v2);
	}

	public static void test1() {
		String slowo = "xxxx";
		ArrayList<String> wynik = new ArrayList<String> (Arrays.asList("x", "xxxx", "x", "xxx", "x", "xx", "x"));

		assert wektoryRowne(wyjatkowePalindromy(slowo), new ArrayList<String> (wynik));
	}

	public static void test2() {
		String slowo = "";
		ArrayList<String> wynik = new ArrayList<String> ();
		assert wektoryRowne(wyjatkowePalindromy(slowo), new ArrayList<String> (wynik));
	}

	public static void main(String[] args) {
		test1();
		test2();
	}
}
