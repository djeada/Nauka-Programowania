/*
Tytul: Obliczenie wartosci wielomianu w punkcie.
Tresc: Otrzymujesz liste n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbe naturalna x. Znajdz wartosc wielomianu w podanym punkcie.
Dane wejsciowe: Lista liczb naturalnych i liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
Dla listy wspolczynnikow [3, 2, 1] i liczby x = 1, zostanie zwrocona liczba 6.

*/
import java.util.*;

public class Main {
	//Otrzymujesz liste n wspolczynnikow wielomianu postaci
	//a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe x.
	//Znajdz wartosc wielomianu w punkcie.
	public static int wartoscWielomianu(ArrayList<Integer> lista, int x) {

		int n = lista.size();
		int wynik = 0;

		for (int i = 0; i<n; i++) {
			wynik += lista.get(i) * Math.pow(x, n - i);
		}

		return wynik;
	}

	public static void test1() {
		ArrayList<Integer> lista = new ArrayList<Integer> (Arrays.asList(3, 2, 1));
		int x = 1;
		int wynik = 6;
		assert wartoscWielomianu(lista, x) == wynik;
	}

	public static void main(String[] args) {

		test1();

	}

