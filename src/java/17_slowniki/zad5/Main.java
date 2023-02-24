import java.util.*;

public class Main {
	//Otrzymujesz liste par. Pierwszym elementem pary jest napis reprezentujacy imie i nazwikso
	//pracownika, drugim zysk z transakcji jaka dany pracownik przeprowadzil. Znajdz pracownika,
	//ktory przyniosl firmie najwiecej zysku.
	private static class Pair<T1, T2 > {
		public T1 first;
		public T2 second;

		public Pair(T1 firstValue, T2 secondValue) {
			first = firstValue;
			second = secondValue;
		}

		@Override public boolean equals(Object o) {
			return (o instanceof Pair) && (this.first == ((Pair) o).first) && (this.second == ((Pair) o).second);
		}
	}
	public static void wypelnijSlownik(final ArrayList<Pair<String, Integer>> lista, HashMap<String, Integer> slownik) {

		for (var rekord: lista) {
			if (slownik.containsKey(rekord.first))
				slownik.put(rekord.first, slownik.get(rekord.first) + rekord.second);
			else
				slownik.put(rekord.first, rekord.second);

		}
	}

	public static String znajdzMaxZysk(HashMap<String, Integer> slownik) {
		String najlepszyPracownik = "";
		int maxZysk = -1;

		for (Map.Entry<String, Integer> entry: slownik.entrySet()) {
			if (entry.getValue() > maxZysk) {
				najlepszyPracownik = entry.getKey();
				maxZysk = entry.getValue();
			}
		}

		return najlepszyPracownik;
	}

	public static String pracownik(ArrayList<Pair<String, Integer>> lista) {

		if (lista.isEmpty()) {
			return "";
		}

		HashMap<String, Integer> slownik = new HashMap<String, Integer> ();
		wypelnijSlownik(lista, slownik);

		return znajdzMaxZysk(slownik);
	}

	public static void test1() {

		ArrayList<Pair<String, Integer>> lista = new ArrayList<Pair<String, Integer>> (Arrays.asList(
			new Pair<String, Integer> ("Barnaba Barabash", 120),
			new Pair<String, Integer> ("Jon Snow", 100),
			new Pair<String, Integer> ("Kira Summer", 300),
			new Pair<String, Integer> ("Barnaba Barabash", 200),
			new Pair<String, Integer> ("Bob Marley", 110)));

		String wynik = "Barnaba Barabash";

		assert wynik.equals(pracownik(lista));
	}

	public static void test2() {
		ArrayList<Pair<String, Integer>> lista = new ArrayList<Pair<String, Integer>> ();
		String wynik = "";

		assert wynik.equals(pracownik(lista));
	}

	public static void main(String[] args) {

		test1();
		test2();

	}

}
