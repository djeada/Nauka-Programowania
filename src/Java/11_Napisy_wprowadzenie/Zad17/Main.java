import java.util.*;

public class GlobalMembers {
	//Otrzymujesz liste liczb.
	//Zamien liste na napis.

	public static String liczby(final ArrayList<Integer> lista) {
		String wynik = "";

		for (var liczba: lista) {
			wynik += String.valueOf(liczba);
		}

		return wynik;
	}

	public static void test1() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(2, 4, 7));
		String wynik = "247";
		assert wynik.equals(liczby(lista));
	}

	public static void test2() {
		ArrayList<Integer> lista = new ArrayList<Integer> ();
		String wynik = "";
		assert wynik.equals(liczby(lista));
	}

	public static void main(String[] args) {
		test1();
		test2();
	}

}