import java.util.*;
public class Main {
	//Usun wszystkie wystapienia klucza z listy.
	//Kolejnosc elementow w liscie powinna zostac zachowana.

	public static ArrayList<Integer> usunWszystkieWystapieniaV1(ArrayList<Integer> lista, int klucz) {
		for (int i = 0; i<lista.size(); i++) {
			if (lista.get(i).equals(klucz)) {
				lista.remove(i--);
			}
		}
		return lista;
	}

	public static ArrayList<Integer> usunWszystkieWystapieniaV2(ArrayList<Integer> lista, int klucz) {
		lista.removeAll(Collections.singleton(klucz));
		return lista;
	}

	public static void test1() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(6, 7, 2, 1, 8));
		ArrayList<Integer> wynik = new ArrayList<Integer> (Arrays.asList(6, 7, 1, 8));
		int klucz = 2;

		assert wynik.equals(usunWszystkieWystapieniaV1(lista, klucz));
	}

	public static void test2() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(6, 7, 2, 1, 8));
		ArrayList<Integer> wynik = new ArrayList<Integer> (Arrays.asList(6, 7, 1, 8));
		int klucz = 2;

		assert wynik.equals(usunWszystkieWystapieniaV2(lista, klucz));

	}

	public static void main(String[] args) {

		test1();
		test2();

	}

}
