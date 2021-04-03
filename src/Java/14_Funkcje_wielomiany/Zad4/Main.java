import java.util.*;

public class Main {
	//Otrzymujesz dwie listy n wspolczynnikow wielomianu postaci
	//a_nx^n + a_(n-1)x^(n-1) + ... + a_. Oblicz wartosc wspolczynnikow
	//wielomianu bedacego iloczynem otrzymanych wielomianow.
	public static ArrayList<Integer> iloczyn(ArrayList<Integer> listaA, ArrayList<Integer> listaB) {
		ArrayList<Integer> wynik = new ArrayList<Integer> (Collections.nCopies(listaA.size() + listaB.size() - 1, 0));

		for (int i = 0; i<listaA.size(); i++) {
			for (int j = 0; j<listaB.size(); j++) {
				wynik.set(i + j, wynik.get(i + j) + listaA.get(i) * listaB.get(j));
			}
		}

		return new ArrayList<Integer> (wynik);
	}

	public static void test1() {
		ArrayList<Integer> listaA = new ArrayList<Integer> (Arrays.asList(5, 0, 10, 6));
		ArrayList<Integer> listaB = new ArrayList<Integer> (Arrays.asList(1, 2, 4));
		ArrayList<Integer> wynik = new ArrayList<Integer> (Arrays.asList(5, 10, 30, 26, 52, 24));
		assert wynik.equals(iloczyn(listaA, listaB));
	}

	public static void main(String[] args) {
		test1();
	}

}
