import java.util.*;
public class Main {
	//Dla otrzymanej listy oraz liczby X, znajdz indeksy pierwszej
	//pary elementów listy, ktorych suma jest rowna liczbie X.
	//Jesli w liscie nie ma takiej pary, zwroc pare (-1, -1)

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

	public static Pair<Integer, Integer> sumaDwochV1(ArrayList<Integer> lista, int liczba) {
		int n = lista.size();

		for (int i = 0; i<n; i++) {
			for (int j = i + 1; j<n; j++) {
				if (lista.get(j) + lista.get(i) == liczba) {
					return new Pair<Integer, Integer> (i, j);
				}
			}
		}

		return new Pair<Integer, Integer> (-1, -1);
	}

	public static void test1() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(1, 3, 4, 5, 2));
		int liczba = 5;
		Pair<Integer, Integer> wynik = new Pair<Integer, Integer> (0, 2);
		assert sumaDwochV1(lista, liczba).equals(wynik);
	}

	public static void test2() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(2, -6, 10, 21, 8));
		int liczba = 7;
		Pair<Integer, Integer> wynik = new Pair<Integer, Integer> (-1, -1);
		assert sumaDwochV1(lista, liczba).equals(wynik);
	}

	public static void main(String[] args) {

		test1();
		test2();

	}

}
