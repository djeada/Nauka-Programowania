import java.util.*;

public class Main {
	//Otrzymujesz liste n wspolczynnikow wielomianu postaci
	//a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe k.
	//Oblicz wartosc wspolczynnikow wielomianu bedacego k-ta
	//pochodna otrzymanego wielomianu.
	public static ArrayList<Integer> pochodna(ArrayList<Integer> lista, int k) {

		ArrayList<Integer> wynik = new ArrayList<Integer> ();
		ArrayList<Integer> kopia = new ArrayList<Integer> (lista);

		for (int j = 0; j<k; j++) {
			wynik.clear();
			int n = kopia.size();
			for (int i = 0; i<n - 1; i++) {
				wynik.add(kopia.get(i) * (n - i - 1));
			}
			kopia = new ArrayList<Integer> (wynik);
		}

		return new ArrayList<Integer> (wynik);
	}

	public static void test1() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(4, -3, 2));
		int k = 1;
		ArrayList<Integer> wynik = new ArrayList<Integer> (Arrays.asList(8, -3));
		assert wynik.equals(pochodna(lista, k));
	}

	public static void test2() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(13, -6, 0, -1, -1));
		int k = 2;
		ArrayList<Integer> wynik = new ArrayList<Integer> (Arrays.asList(156, -36, 0));
		assert wynik.equals(pochodna(lista, k));
	}

	public static void main(String[] args) {
		test1();
		test2();
	}
}
