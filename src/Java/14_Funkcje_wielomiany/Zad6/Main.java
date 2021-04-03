import java.util.*;

public class Main {
	//Otrzymujesz liste wspolczynnikow a, b, c rownania
	//kwadratowego ax^2 + bx + c.
	//Znajdz rzeczywiste miejsca zerowe rownania kwadratowego.
	private static class Pair<T1, T2 > {
		public T1 first;
		public T2 second;

		public Pair() {
			first = null;
			second = null;
		}

		public Pair(T1 firstValue, T2 secondValue) {
			first = firstValue;
			second = secondValue;
		}

		@Override public boolean equals(Object o) {
			return (o instanceof Pair) && (this.first == ((Pair) o).first) && (this.second == ((Pair) o).second);
		}
	}

	public static Pair<Double, Double> pierwiastki(ArrayList<Double> lista) {

		assert lista.size() == 3;

		Pair<Double, Double> wynik = new Pair<Double, Double> ();

		double delta = lista.get(1) * lista.get(1) - 4 * lista.get(0) * lista.get(2);

		if (delta > 0) {
			wynik.first = (-lista.get(1) + Math.sqrt(delta)) / (2 * lista.get(0));
			wynik.second = (-lista.get(1) - Math.sqrt(delta)) / (2 * lista.get(0));
		} else if (delta == 0) {
			wynik.first = -lista.get(1) / (2 * lista.get(0));
			wynik.second = -lista.get(1) / (2 * lista.get(0));
		}

		return wynik;
	}

	public static void test1() {
		ArrayList<Double> lista = new ArrayList<Double> (Arrays.asList(1.0, 2.0, 1.0));
		Pair<Double, Double> wynik = new Pair<Double, Double> (-1.0, -1.0);

		assert wynik.first.compareTo(pierwiastki(lista).first) == 0;
		assert wynik.second.compareTo(pierwiastki(lista).second) == 0;
	}

	public static void test2() {
		ArrayList<Double> lista = new ArrayList<Double> (Arrays.asList(1.0, -4.0, 5.0));
		Pair<Double, Double> wynik = new Pair<Double, Double> ();
		assert wynik.equals(pierwiastki(lista));
	}

	public static void main(String[] args) {

		test1();
		test2();
	}

}
