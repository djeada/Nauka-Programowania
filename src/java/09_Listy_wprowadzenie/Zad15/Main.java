import java.util.*;
public class Main {
	//Dla otrzymanej listy liczb naturalnych, znajdz elemnt
	//dominujacy. Element dominujacy to element, ktorego liczba
	//wystapien w liscie jest wieksza niz polowa dlugosci listy.
	//Jesli lista nie ma elementu dominujacego, zwroc -1.

	public static int elementDominujacyV1(ArrayList<Integer> lista) {
		int n = lista.size();

		for (int i = 0; i<= n / 2; i++) {
			int licznik = 1;
			for (int j = i + 1; j<n; j++) {
				if (lista.get(j) == lista.get(i)) {
					licznik++;
				}
			}

			if (licznik > n / 2) {
				return lista.get(i);
			}
		}

		return -1;
	}

	public static int elementDominujacyV2(ArrayList<Integer> lista) {

		HashMap<Integer, Integer> histo = new HashMap<Integer, Integer> ();

		for (var liczba: lista) {
			if (histo.containsKey(liczba))
				histo.put(liczba, histo.get(liczba) + 1);
			else
				histo.put(liczba, 1);
		}

		for (Map.Entry<Integer, Integer> para: histo.entrySet()) {
			if (para.getValue() > lista.size() / 2) {
				return para.getKey();
			}

		}

		return -1;
	}

	public static void test1() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(4, 7, 4, 4, 2));
		int wynik = 4;
		assert elementDominujacyV1(lista) == wynik;
		assert elementDominujacyV2(lista) == wynik;
	}

	public static void test2() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(1, 2, 4, 5, 6));
		int wynik = -1;
		assert elementDominujacyV1(lista) == wynik;
		assert elementDominujacyV2(lista) == wynik;
	}

	public static void main(String[] args) {

		test1();
		test2();

	}

}
