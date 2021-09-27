import java.util.*;

public class Main {
	//Otrzymujesz liste 2d. Zbierz spiralnie elementy
	//otrzymanej listy i zapisz je w zwyklej liscie.

	public static ArrayList<Integer> spiralaV1(ArrayList<ArrayList<Integer>> macierz) {
		ArrayList<Integer> wynik = new ArrayList<Integer> ();

		int x = macierz.get(0).size();
		int y = macierz.size();
		int k = 0;
		int l = 0;

		while (k<y && l<x) {

			for (int i = l; i<x; i++) {
				wynik.add(macierz.get(k).get(i));
			}

			k++;

			for (int i = k; i<y; i++) {
				wynik.add(macierz.get(i).get(x - 1));
			}

			x--;

			if (k<x) {

				for (int i = x - 1; i > l - 1; i--) {
					wynik.add(macierz.get(y - 1).get(i));
				}
				y--;
			}

			if (l<y) {

				for (int i = y - 1; i > k - 1; i--) {
					wynik.add(macierz.get(i).get(l));
				}
				l++;
			}
		}

		return new ArrayList<Integer> (wynik);
	}

	public static void test1() {
		ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(1, 2, 3, 4, 5)), new ArrayList<Integer> (Arrays.asList(16, 17, 18, 19, 6)), new ArrayList<Integer> (Arrays.asList(15, 24, 25, 20, 7)), new ArrayList<Integer> (Arrays.asList(14, 23, 22, 21, 8)), new ArrayList<Integer> (Arrays.asList(13, 12, 11, 10, 9))));

		ArrayList<Integer> wynik = new ArrayList<Integer> (Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25));

		assert wynik.equals(spiralaV1(macierz));
	}

	public static void test2() {
		ArrayList<ArrayList<Integer>> macierz = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(1, 2, 3)), new ArrayList<Integer> (Arrays.asList(4, 5, 6)), new ArrayList<Integer> (Arrays.asList(7, 8, 9))));

		ArrayList<Integer> wynik = new ArrayList<Integer> (Arrays.asList(1, 2, 3, 6, 9, 8, 7, 4, 5));

		assert wynik.equals(spiralaV1(macierz));
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}
