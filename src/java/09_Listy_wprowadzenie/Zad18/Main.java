import java.util.*;
public class Main {
	//Dla otrzymanej listy znajdz indeks najmniejszego elementu.
	//Lista jest posortowana rosnaco, ale zostala przesunieta.
	//Przykladowo przez przesuniecie w prawo o 1 rozumiemy, ze
	//ostatni element trafi na miejsce pierwszego, pierwszy drugiego, itd.

	public static int indeksMin(ArrayList<Integer> lista) {
		int n = lista.size();

		for (int i = 0; i<n - 1; i++) {
			if (lista.get(i) > lista.get(i + 1)) {
				return i + 1;
			}
		}

		return 0;
	}

	public static void test1() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(7, 8, -1, 4, 5));
		int wynik = 2;
		assert indeksMin(lista) == wynik;
	}

	public static void test2() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(2, 3, 4, 5, 6));
		int wynik = 0;
		assert indeksMin(lista) == wynik;
	}

	public static void test3() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(8, 9, 10, 11, 1));
		int wynik = 4;
		assert indeksMin(lista) == wynik;
	}

	public static void main(String[] args) {

		test1();
		test2();
		test3();

	}

}
