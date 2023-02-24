import java.util.*;

public class Main {
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

	public static void oblicz(int n, Pair<Integer, Integer> wyniki) {
		oblicz(n, wyniki, "AB");
	}
	/*
	Gracz A oraz gracz B graja w kapsle.
	Na poczatku gry otrzymuja pewna liczbe kapsli.
	W kazdej turze grac moze z puli kapsli zabrac 1, 2 badz 4 kapsle.
	Gracz, ktory zabral ostatni kapsel wygyrwa.
	Gre rozpoczyna gracz A.
	Znajdz liczbe mozliwych kombinacji wybrania liczby kapsli w danej turze
	prowadzaca do zwyciestwa kazdego z graczy.
	*/
	private static String swapChars(String slowa, int i, int j) {
		StringBuilder sb = new StringBuilder(slowa);
		char l = sb.charAt(i), r = sb.charAt(j);
		sb.setCharAt(i, r);
		sb.setCharAt(j, l);
		return sb.toString();
	}

	public static void oblicz(int n, Pair<Integer, Integer> wyniki, String s) {

		if (n<= 0) {
			return;
		}

		if (n == 1 || n == 2 || n == 4) {

			if (s.charAt(0) == 'A') {
				wyniki.first += 1;
			} else {
				wyniki.second += 1;
			}

			return;
		} else {
			s = swapChars(s, 0, 1);

			oblicz(n - 1, wyniki, s);
			oblicz(n - 2, wyniki, s);
			oblicz(n - 4, wyniki, s);
		}
	}

	public static void test1() {

		Pair<Integer, Integer> wyniki = new Pair<Integer, Integer> (0, 0);

		oblicz(1, wyniki);
		assert wyniki.first == 1;
		assert wyniki.second == 0;
	}

	public static void test2() {

		Pair<Integer, Integer> wyniki = new Pair<Integer, Integer> (0, 0);

		oblicz(3, wyniki);
		assert wyniki.first == 0;
		assert wyniki.second == 2;

	}

	public static void test3() {

		Pair<Integer, Integer> wyniki = new Pair<Integer, Integer> (0, 0);

		oblicz(10, wyniki);
		assert wyniki.first == 33;
		assert wyniki.second == 27;

	}

	public static void main(String[] args) {

		test1();
		test2();
		test3();

	}

}
