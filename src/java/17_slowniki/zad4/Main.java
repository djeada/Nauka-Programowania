/*
Tytul: Histogram slow w tekscie
Tresc: Otrzymujesz tekst w postaci napisu. Twoim zadaniem jest znalezc czestosc wystepowania kazdego ze slow w tekscie. Nalezy zignorowac roznice miedzy malymi i wielkimi literami. Pamietaj, ze slowa skladaja sie wylacznie z liter.
Dane wejsciowe: Napis.
Dane wyjsciowe: Slownik par: napis, liczba naturalna.
Przyklad:
Dla otrzymanego napisu: "Here, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, perhaps a bit; in particular since my tricksy corpus will not match the pattern you expect from it; nor will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now."
Powinien zostac zwrocony slownik:
{"here": 1, "a": 12, "tricksy": 4, "corpus": 5, "will": 6, "exist": 1, "very": 2, "strange": 1, "sometimes": 1, "cryptic": 1, "dumbfound": 1, "you": 2, "maybe": 1, "perhaps": 1, "bit": 1, "in": 1, "particular": 1, "since": 1, "my": 1, "not": 1, "match": 1, "the": 2, "pattern": 1, "expect": 1, "from": 2, "it": 2, "nor": 1, "look": 1, "like": 1, "fish": 1, "boat": 1, "sunflower": 1, "or": 3, "handsome": 1, "kitten": 1, "surprise": 1, "user": 1, "named": 1, "ami": 1, "tavory": 1, "this": 1, "be": 1, "fun": 1, "to": 1, "follow": 1, "year": 1, "month": 1, "minute": 1, "now": 1}

*/
mport java.util.*;

public class Main {

	public static void usunZeSlownikaV1(Map<String, Integer> slownik, int wartosc) {

		for (Iterator<Map.Entry<String, Integer>> it = slownik.entrySet().iterator(); it.hasNext();) {

			Map.Entry<String, Integer> entry = it.next();

			if (entry.getValue().equals(wartosc))
				it.remove();
		}
	}

	public static void test1() {
		Map<String, Integer> slownik = new HashMap<String, Integer> () {
			{
				put("aaa", 5);
				put("abc", 1);
				put("xxx", 5);
				put("cba", 3);
			}
		};

		Map<String, Integer> wynik = new HashMap<String, Integer> () {
			{
				put("abc", 1);
				put("cba", 3);
			}
		};

		int wartosc = 5;

		usunZeSlownikaV1(slownik, wartosc);

		assert slownik.equals(wynik);
	}

	public static void main(String[] args) {

		test1();
	}

}

