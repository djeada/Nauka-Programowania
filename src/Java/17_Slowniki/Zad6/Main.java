import java.util.*;

public class Main {
	// Otrzymujesz napis. Znajdz czestosc wystepowania znakow w otrzymanym napisie.

	public static HashMap<Character, Integer> budujSlownik(final String slowo) {
		HashMap<Character, Integer> slownik = new HashMap<Character, Integer> ();

		for (var znak: slowo.toCharArray()) {
			if (slownik.containsKey(znak))
				slownik.put(znak, slownik.get(znak) + 1);
			else
				slownik.put(znak, 1);
		}

		return new HashMap<Character, Integer> (slownik);
	}

	public static void test1() {
		String slowo = "klasa";
		HashMap<Character, Integer> wynik = new HashMap<Character, Integer> (Map.ofEntries(Map.entry('k', 1), Map.entry('l', 1), Map.entry('a', 2), Map.entry('s', 1)));

		assert wynik.equals(budujSlownik(slowo));
	}

	public static void test2() {
		String slowo = "robot";
		HashMap<Character, Integer> wynik = new HashMap<Character, Integer> (Map.ofEntries(Map.entry('r', 1), Map.entry('o', 2), Map.entry('b', 1), Map.entry('t', 1)));

		assert wynik.equals(budujSlownik(slowo));
	}

	public static void main(String[] args) {
		test1();
		test2();
	}
}
