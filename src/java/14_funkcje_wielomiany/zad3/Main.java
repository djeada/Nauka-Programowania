import java.util.*;

public class Main {
	//Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci
	//a_nx^n + a_(n-1)x^(n-1) + ... + a_. Oblicz wartosc wspolczynnikow
	//wielomianu bedacego suma otrzymanych wielomianow.
	public static ArrayList<Integer> suma(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {

		assert listaA.size() == listaB.size();
		ArrayList<Integer> wynik = new ArrayList<Integer> ();

		for (int i = 0; i<listaA.size(); i++) {
			wynik.add(listaA.get(i) + listaB.get(i));
		}

		return new ArrayList<Integer> (wynik);
	}

	public static void test1() {
		ArrayList<Integer> listaA = new ArrayList<Integer> (Arrays.asList(3, 2, 1));
		ArrayList<Integer> listaB = new ArrayList<Integer> (Arrays.asList(8, 9, 2));
		ArrayList<Integer> wynik = new ArrayList<Integer> (Arrays.asList(11, 11, 3));
		assert wynik.equals(suma(listaA, listaB));
	}

	public static void main(String[] args) {
		test1();
	}
}
