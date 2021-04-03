import java.util.*;

public class Main {
	//Otrzymujesz liste 2d. Znajdz w niej klepsydre o najwiekszej sumie.
	//Klepsydra sklada sie z dokladnie 7 elementow. Trzy pierwsze elementy
	//są kolejnymi elementami dowolnego wiersza listy 2d. Nastepny element
	//znajduje sie w tej samej kolumnie co drugi element i w dokladnie
	//jednym wierszu nizej. Trzy nastepne znajduja sie w tych samych
	//kolumnach co trzy pierwsze i dokladnie dwie wiersze nizej.

	public static int klepsydraV1(ArrayList<ArrayList<Integer>> macierz) {
		int wynik = Integer.MIN_VALUE;

		int N = macierz.size();

		for (int wiersz = 0; wiersz<N; wiersz++) {
			for (int kolumna = 0; kolumna<N; kolumna++) {
				if (!(wiersz == 0 || wiersz == N - 1 || kolumna == 0 || kolumna == N - 1)) {
					wynik = Math.max(wynik, (macierz.get(wiersz - 1).get(kolumna - 1) + macierz.get(wiersz - 1).get(kolumna) + macierz.get(wiersz - 1).get(kolumna + 1) + macierz.get(wiersz).get(kolumna) + macierz.get(wiersz + 1).get(kolumna - 1) + macierz.get(wiersz + 1).get(kolumna) + macierz.get(wiersz + 1).get(kolumna + 1)));
				}
			}
		}

		return wynik;
	}

	public static void test1() {
		ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(10, 99, 28, 21, 78)), new ArrayList<Integer> (Arrays.asList(35, 78, 31, 56, 24)), new ArrayList<Integer> (Arrays.asList(7, 18, 2, 50, 87)), new ArrayList<Integer> (Arrays.asList(59, 67, 9, 82, 53)), new ArrayList<Integer> (Arrays.asList(23, 26, 76, 62, 36))));

		int wynik = 395;
		assert klepsydraV1(macierz) == wynik;
	}

	public static void main(String[] args) {
		test1();
	}

}
