import java.util.*;

public class Main {
	//Otrzymujesz dwie listy. Zbuduj slownik skladajacy się z kluczy będacych
	//elementami pierwszej listy i wartosciami będacymi elementami drugiej listy.
	//Jesli listy sa roznej dlugosci zwroc pusty slownik.
	public static HashMap<Integer, Integer> budujSlownik(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {
		HashMap<Integer, Integer> slownik = new HashMap<Integer, Integer> ();

		if (listaA.size() != listaB.size()) {
			return new HashMap<Integer, Integer> (slownik);
		}

		for (int i = 0; i<listaA.size(); i++) {
			slownik.put(listaA.get(i), listaB.get(i));
		}

		return new HashMap<Integer, Integer> (slownik);
	}

	public static void test1() {
		ArrayList<Integer> listaA = new ArrayList<Integer> (Arrays.asList(3, 5, 8));
		ArrayList<Integer> listaB = new ArrayList<Integer> (Arrays.asList(1, 2, -1));
		HashMap<Integer, Integer> wynik = new HashMap<Integer, Integer> (Map.ofEntries(Map.entry(3, 1), Map.entry(5, 2), Map.entry(8, -1)));

		assert wynik.equals(budujSlownik(listaA, listaB));
	}

	public static void test2() {
		ArrayList<Integer> listaA = new ArrayList<Integer> (Arrays.asList(0, 1));
		ArrayList<Integer> listaB = new ArrayList<Integer> (Arrays.asList(1, 0));
		HashMap<Integer, Integer> wynik = new HashMap<Integer, Integer> (Map.ofEntries(Map.entry(0, 1), Map.entry(1, 0)));

		assert wynik.equals(budujSlownik(listaA, listaB));
	}

	public static void main(String[] args) {
		test1();
		test2();
	}
}
