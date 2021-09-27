import java.util.*;

public class Main {
	//Otrzymujesz dwie macierze o tych samych wymiarach, zwroc macierz bedaca:

	//a) wynikiem dodawania otrzymanych macierzy;
	public static boolean wymiaryRowne(ArrayList<ArrayList<Integer>> macierzA, ArrayList<ArrayList<Integer>> macierzB) {

		if (macierzA.size() != macierzB.size()) {
			return false;
		}

		for (int i = 0; i<macierzA.size(); i++) {
			if (macierzA.get(i).size() != macierzB.get(i).size()) {
				return false;
			}
		}

		return true;
	}

	public static ArrayList<ArrayList<Integer>> dodaj(ArrayList<ArrayList<Integer>> macierzA, ArrayList<ArrayList<Integer>> macierzB) {

		ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>> ();

		if (!wymiaryRowne(new ArrayList<ArrayList<Integer>> (macierzA), new ArrayList<ArrayList<Integer>> (macierzB))) {
			return new ArrayList<ArrayList<Integer>> (wynik);
		}

		for (int i = 0; i<macierzA.size(); ++i) {
			ArrayList<Integer> wiersz = new ArrayList<Integer> ();
			for (int j = 0; j<macierzA.get(i).size(); ++j) {
				wiersz.add(macierzA.get(i).get(j) + macierzB.get(i).get(j));
			}
			wynik.add(wiersz);
		}

		return new ArrayList<ArrayList<Integer>> (wynik);
	}

	//b) odejmowania pierwszej macierzy od drugiej.
	public static ArrayList<ArrayList<Integer>> odejmij(ArrayList<ArrayList<Integer>> macierzA, ArrayList<ArrayList<Integer>> macierzB) {

		ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>> ();

		if (!wymiaryRowne(new ArrayList<ArrayList<Integer>> (macierzA), new ArrayList<ArrayList<Integer>> (macierzB))) {
			return new ArrayList<ArrayList<Integer>> (wynik);
		}

		for (int i = 0; i<macierzA.size(); ++i) {
			ArrayList<Integer> wiersz = new ArrayList<Integer> ();
			for (int j = 0; j<macierzA.get(i).size(); ++j) {
				wiersz.add(macierzA.get(i).get(j) - macierzB.get(i).get(j));
			}
			wynik.add(wiersz);
		}

		return new ArrayList<ArrayList<Integer>> (wynik);
	}

	public static void test1() {
		ArrayList<ArrayList<Integer>> macierzA = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(1, 2)), new ArrayList<Integer> (Arrays.asList(-2, 0))));
		ArrayList<ArrayList<Integer>> macierzB = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(5, -3)), new ArrayList<Integer> (Arrays.asList(1, 7))));
		ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(6, -1)), new ArrayList<Integer> (Arrays.asList(-1, 7))));
		assert wynik.equals(dodaj(macierzA, macierzB));
	}

	public static void test2() {
		ArrayList<ArrayList<Integer>> macierzA = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(1, 2)), new ArrayList<Integer> (Arrays.asList(-2, 0))));
		ArrayList<ArrayList<Integer>> macierzB = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(5, -3)), new ArrayList<Integer> (Arrays.asList(1, 7))));
		ArrayList<ArrayList<Integer>> wynik = new ArrayList<ArrayList<Integer>> (Arrays.asList(new ArrayList<Integer> (Arrays.asList(-4, 5)), new ArrayList<Integer> (Arrays.asList(-3, -7))));
		assert wynik.equals(odejmij(macierzA, macierzB));
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}
