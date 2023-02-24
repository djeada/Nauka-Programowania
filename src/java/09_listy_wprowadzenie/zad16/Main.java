import java.util.*;
public class Main {
	//Znajdz takie pary elementow w liscie, ktorych suma jest rowna liczbie.
	//Element nie moze byc w parze sam ze soba.

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

	public static ArrayList<Pair<Integer, Integer>> znajdzParyV1(ArrayList<Integer> lista, int suma) {

		ArrayList<Pair<Integer, Integer>> wynik = new ArrayList<Pair<Integer, Integer>> ();

		for (int i = 0; i<lista.size(); i++) {
			for (int j = i + 1; j<lista.size(); j++) {
				if (lista.get(i) + lista.get(j) == suma) {
					Pair<Integer, Integer> para = new Pair<Integer, Integer> (lista.get(i), lista.get(j));
					wynik.add(para);
				}
			}
		}
		

		return new ArrayList<Pair<Integer, Integer>> (wynik);
	}

	public static void test1() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(0, 4, 5, 6, 2, 9, 2, 3));
		ArrayList<Pair<Integer, Integer>> wynik = new ArrayList<Pair<Integer, Integer>> ();
		wynik.add(new Pair<Integer, Integer> (0, 5));
		wynik.add(new Pair<Integer, Integer> (2, 3));
		wynik.add(new Pair<Integer, Integer> (2, 3));

		int suma = 5;

		assert wynik.equals(znajdzParyV1(lista, suma));
	}

	public static void main(String[] args) {

		test1();

	}

}
