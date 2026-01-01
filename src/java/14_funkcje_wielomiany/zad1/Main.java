/*
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `Horner`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `x`, a następnie zwraca wartość wielomianu w punkcie `x`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `x` — liczba naturalna (lub całkowita)

### Wyjście (zwracana wartość)

* jedna liczba (całkowita)

### Przykład

Dla `a = [3, 2, 1]` i `x = 1` funkcja zwraca:
`6`

### Uwagi

* Najprościej użyć schematu Hornera.

*/
import java.util.*;

public class Main {
	// Otrzymujesz liste n wspolczynnikow wielomianu postaci
	// a_nx^n + a_(n-1)x^(n-1) + ... + a_0 oraz liczbe x.
	// Znajdz wartosc wielomianu w punkcie.
	
	// Zlozonosc Czasowa: O(n)
	// Zlozonosc Pamieciowa: O(1)
	public static int wartoscWielomianu(ArrayList<Integer> lista, int x) {

		int n = lista.size();
		int wynik = 0;

		for (int i = 0; i < n; i++) {
			wynik += lista.get(i) * Math.pow(x, n - i - 1);
		}

		return wynik;
	}

	public static void test1() {
		ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(3, 2, 1));
		int x = 1;
		int wynik = 6;
		assert wartoscWielomianu(lista, x) == wynik;
	}

	public static void main(String[] args) {
		test1();
	}
}