import java.util.*;

public class Main {
	//Otrzymujesz tekst w postaci napisu. Znajdz czestosc wystepowania kazdego ze slow w tekscie.
	//Zignoruj roznice miedzy malymi i wielkimi literami. Pamietaj, slowa skladaja sie wylacznie z liter!

	public static String wyczysc(String napis) {
		napis = napis.trim();
		return napis.replaceAll("\\p{Punct}", "");
	}

	public static ArrayList<String> rozdzielSlowa(final String napis) {
		ArrayList<String> wynik = new ArrayList<String> ();
		int pocz = 0;
		int konc = 0;
		while ((konc = napis.indexOf(' ', pocz)) != -1) {
			if (konc != pocz) {
				var slowo = napis.substring(pocz, konc);
				slowo = wyczysc(slowo);
				slowo = slowo.toLowerCase();
				if (!slowo.isEmpty() && !wynik.contains(slowo)) {
					{
						wynik.add(slowo);
					}
				}
				pocz = konc + 1;
			}
			if (konc != pocz) {
				var slowo = napis.substring(pocz);
				slowo = wyczysc(slowo);
				slowo = slowo.toLowerCase();
				if (!slowo.isEmpty() && !wynik.contains(slowo)) {
					wynik.add(slowo);
				}
			}
		}

		return new ArrayList<String> (wynik);
	}

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

	public static ArrayList<ArrayList<String>> znajdzAnagramy(final String tekst) {

		var slowa = rozdzielSlowa(tekst);

		ArrayList<ArrayList<String>> wynik = new ArrayList<ArrayList<String>> ();

		for (int i = 0; i<slowa.size(); i++) {

			var slowo = slowa.get(i);
			var histogram = budujSlownik(slowo);
			ArrayList<String> anagramy = new ArrayList<String> (Arrays.asList(slowo));

			for (int j = i + 1; j<slowa.size(); j++) {

				var porownywaneSlowo = slowa.get(j);
				if (histogram.equals(budujSlownik(porownywaneSlowo))) {
					anagramy.add(porownywaneSlowo);
					break;
				}
			}

			if (anagramy.size() > 1) {
				wynik.add(anagramy);
			}
		}

		return new ArrayList<ArrayList<String>> (wynik);
	}

	public static void test1() {
		String slowo = "To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. " + "Burza nad galeria i alergia na narty to zadna zbrodnia, jak bandzior i jego arbuz.";
		ArrayList<ArrayList<String>> wynik = new ArrayList<ArrayList<String>> (Arrays.asList(
			new ArrayList<String> (Arrays.asList("absurd", "brudas")),
			new ArrayList<String> (Arrays.asList("tyran", "narty")),
			new ArrayList<String> (Arrays.asList("bandzior", "zbrodnia")), n ew ArrayList<String> (Arrays.asList("burza", "arbuz")),
			new ArrayList<String> (Arrays.asList("galeria", "alergia"))));

		assert wynik.equals(znajdzAnagramy(slowo));
	}

	public static void test2() {
		String slowo = "I love the way sometimes the letters of an anagram rearrange themselves in my " + "head with no effort, whereas sometimes I have to write them out in a circle to work it out.";
		ArrayList<ArrayList<String>> wynik = new ArrayList<ArrayList<String>> ();

		assert wynik.equals(znajdzAnagramy(slowo));
	}

	public static void main(String[] args) {

		test1();
		test2();

	}

}
