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
				if (!slowo.isEmpty()) {
					wynik.add(slowo);
				}
			}
			pocz = konc + 1;
		}
		if (konc != pocz) {
			var slowo = napis.substring(pocz);
			slowo = wyczysc(slowo);
			slowo = slowo.toLowerCase();
			if (!slowo.isEmpty()) {
				wynik.add(slowo);
			}
		}

		return new ArrayList<String> (wynik);
	}

	public static HashMap<String, Integer> budujSlownik(final String tekst) {
		HashMap<String, Integer> slownik = new HashMap<String, Integer> ();

		ArrayList<String> slowa = rozdzielSlowa(tekst);

		for (var slowo: slowa) {
			if (slownik.containsKey(slowo))
				slownik.put(slowo, slownik.get(slowo) + 1);
			else
				slownik.put(slowo, 1);

		}

		return new HashMap<String, Integer> (slownik);
	}

	public static void test1() {
		String slowo = "Here,,,, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, " + "perhaps a bit; in particular since my tricksy corpus will not match the pattern you EXPECT from it; nor " + "will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise " + "a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now.";

		HashMap<String, Integer> wynik = new HashMap<String, Integer> (Map.ofEntries(
			Map.entry("here", 1),
			Map.entry("a", 12),
			Map.entry("tricksy", 4),
			Map.entry("corpus", 5),
			Map.entry("will", 6),
			Map.entry("exist", 1),
			Map.entry("very", 2),
			Map.entry("strange", 1),
			Map.entry("sometimes", 1),
			Map.entry("cryptic", 1),
			Map.entry("dumbfound", 1),
			Map.entry("you", 2),
			Map.entry("maybe", 1),
			Map.entry("perhaps", 1),
			Map.entry("bit", 1),
			Map.entry("in", 1),
			Map.entry("particular", 1),
			Map.entry("since", 1),
			Map.entry("my", 1),
			Map.entry("not", 1),
			Map.entry("match", 1),
			Map.entry("the", 2),
			Map.entry("pattern", 1),
			Map.entry("expect", 1),
			Map.entry("from", 2),
			Map.entry("it", 2),
			Map.entry("nor", 1),
			Map.entry("look", 1),
			Map.entry("like", 1),
			Map.entry("fish", 1),
			Map.entry("boat", 1),
			Map.entry("sunflower", 1),
			Map.entry("or", 3),
			Map.entry("handsome", 1),
			Map.entry("kitten", 1),
			Map.entry("surprise", 1),
			Map.entry("user", 1),
			Map.entry("named", 1),
			Map.entry("ami", 1),
			Map.entry("tavory", 1),
			Map.entry("this", 1),
			Map.entry("be", 1),
			Map.entry("fun", 1),
			Map.entry("to", 1),
			Map.entry("follow", 1),
			Map.entry("year", 1),
			Map.entry("month", 1),
			Map.entry("minute", 1),
			Map.entry("now", 1)));

		assert wynik.equals(budujSlownik(slowo));
	}

	public static void test2() {
		String slowo = "The most intelligent people disguise the fact that they are intelligent. Wise men do not wear name tags., " + "The more people talk about their own skills, the more desperate they are--their work should speak for itself.";

		HashMap<String, Integer> wynik = new HashMap<String, Integer> (Map.ofEntries(
			Map.entry("itself", 1),
			Map.entry("should", 1),
			Map.entry("desperate", 1),
			Map.entry("aretheir", 1),
			Map.entry("own", 1),
			Map.entry("their", 1),
			Map.entry("tags", 1),
			Map.entry("name", 1),
			Map.entry("wear", 1),
			Map.entry("the", 4),
			Map.entry("work", 1),
			Map.entry("most", 1),
			Map.entry("they", 2),
			Map.entry("intelligent", 2),
			Map.entry("for", 1),
			Map.entry("speak", 1),
			Map.entry("skills", 1),
			Map.entry("not", 1),
			Map.entry("people", 2),
			Map.entry("fact", 1),
			Map.entry("about", 1),
			Map.entry("do", 1),
			Map.entry("talk", 1),
			Map.entry("more", 2),
			Map.entry("disguise", 1),
			Map.entry("that", 1),
			Map.entry("are", 1),
			Map.entry("wise", 1),
			Map.entry("men", 1)));

		assert wynik.equals(budujSlownik(slowo));
	}

	public static void main(String[] args) {

		test1();
		test2();

	}

}
