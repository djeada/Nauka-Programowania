import java.util.*;

public class Main {
	//Otrzymujesz macierz kwadratowa. Sprawdz, czy macierz jest kwadratem magicznym.
	//Kwadrat magiczny sklada sie z nie powtarzajacych sie dodatnich liczb naturalnych.
	//Suma elementow w kazdym wierszu, w kazdej kolumnie oraz na kazdej przekatnej
	//jest taka sama.
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

	public static boolean macierzKwadratowa(final ArrayList<ArrayList<Integer>> macierz) {
		int n = macierz.size();

		for (int i = 0; i<n; i++) {
			if (macierz.get(i).size() != n) {
				return false;
			}
		}

		return true;
	}

	public static Pair<Integer, Integer> przekatne(final ArrayList<ArrayList<Integer>> macierz) {
		int sumaPrzekatnej1 = 0;
		int sumaPrzekatnej2 = 0;
		int n = macierz.size();
		for (int i = 0; i<n; i++) {
			for (int j = 0; j<n; j++) {
				if (i == j) {
					sumaPrzekatnej1 += macierz.get(i).get(j);
				}
				if (i + j == (n - 1)) {
					sumaPrzekatnej2 += macierz.get(i).get(j);
				}
			}
		}

		return new Pair<Integer, Integer> (sumaPrzekatnej1, sumaPrzekatnej2);
	}

	public static ArrayList<Integer> wiersze(final ArrayList<ArrayList<Integer>> macierz) {
		ArrayList<Integer> wynik = new ArrayList<Integer> ();

		for (var wiersz: macierz) {
			int sumaWiersz = 0;

			for (var liczba: wiersz) {
				sumaWiersz += liczba;
			}

			wynik.add(sumaWiersz);
		}

		return new ArrayList<Integer> (wynik);
	}

	public static ArrayList<Integer> kolumny(final ArrayList<ArrayList<Integer>> macierz) {
		ArrayList<Integer> wynik = new ArrayList<Integer> ();

		for (int i = 0; i<macierz.size(); i++) {
			int sumaKolumna = 0;

			for (int j = 0; j<macierz.size(); j++) {
				sumaKolumna += macierz.get(j).get(i);
			}

			wynik.add(sumaKolumna);
		}

		return new ArrayList<Integer> (wynik);
	}

	public static boolean magicznyKwadrat(final ArrayList<ArrayList<Integer>> macierz) {

		if (!macierzKwadratowa(macierz)) {
			return false;
		}

		int n = macierz.size();

		Pair<Integer, Integer> sumaPrzekatnych = przekatne(macierz);

		if (sumaPrzekatnych.first != sumaPrzekatnych.second) {
			return false;
		}

		for (var sumaWiersz: wiersze(macierz)) {
			if (sumaWiersz != sumaPrzekatnych.first) {
				return false;
			}
		}

		for (var sumaKolumna: kolumny(macierz)) {
			if (sumaKolumna != sumaPrzekatnych.first) {
				return false;
			}
		}

		return true;
	}

	public static void test1() {
		ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(2, 7, 6)), new ArrayList<Integer> (Arrays.asList(9, 5, 1)), new ArrayList<Integer> (Arrays.asList(4, 3, 8))));
		assert magicznyKwadrat(macierz);
	}

	public static void test2() {
		ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(1, 2)), new ArrayList<Integer> (Arrays.asList(-2, 0))));
		assert!magicznyKwadrat(macierz);
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}
