import java.util.*;

public class Main {
	//Dla otrzymanej liczby, stworz macierz kwadratowa skladajaca
	//się z liczby kolumn i wierszy rownej otrzymanej liczbie
	//ktorej kazdy element jest iloczynem jego wspolrzednych.

	public static ArrayList<ArrayList<Integer>> macierz(int n) {

		ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>> ();
		macierz.ensureCapacity(n);

		for (int i = 0; i<n; i++) {
			ArrayList<Integer> wiersz = new ArrayList<Integer> ();
			for (int j = 0; j<n; j++) {
				wiersz.add(i * j);
			}
			macierz.add(wiersz);
		}

		return new ArrayList<ArrayList<Integer>> (macierz);
	}

	public static void test1() {
		int n = 4;
		ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(0, 0, 0, 0)), new ArrayList<Integer> (Arrays.asList(0, 1, 2, 3)), new ArrayList<Integer> (Arrays.asList(0, 2, 4, 6)), new ArrayList<Integer> (Arrays.asList(0, 3, 6, 9))));
		assert wynik.equals(macierz(n));
	}

	public static void main(String[] args) {
		test1();
	}

}
