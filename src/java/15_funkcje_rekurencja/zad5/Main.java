/*
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `pochodna`, `wielomiany`, `I/O`

### Treść

Wczytaj wielomian stopnia `n` oraz liczbę `k`. Wypisz współczynniki wielomianu będącego `k`-tą pochodną.

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `k` — rząd pochodnej (`k ≥ 1`)

### Wyjście

* Jeśli po zróżniczkowaniu `k` razy zostaje wielomian niezerowy: wypisz jego współczynniki w jednej linii (spacje).
* Jeśli wielomian „znika” (stopień < k): wypisz dokładnie `[]`.

### Przykład

**Wejście:**

```
2
4 -3 2
1
```

**Wyjście:**

```
8 -3
```

### Uwagi o formatowaniu

* Pochodna: jeśli aktualne współczynniki to `[c_d, c_{d-1}, ..., c_0]`, to pochodna ma współczynniki:
  `[d*c_d, (d-1)*c_{d-1}, ..., 1*c_1]`.

*/
public class Main {
  // Liczba Fibonacciego.

  // Zlozonosc Czasowa: O(2^n) - bez memoizacji
  // Zlozonosc Pamieciowa: O(n) - rekurencja uzywa stosu
  public static int fibonnaciV1(int n) {

    if (n == 0 || n == 1) {
      return n;
    }

    return fibonnaciV1(n - 1) + fibonnaciV1(n - 2);
  }

  public static int[] fibonnaciV2_pom = new int[256];

  public static int fibonnaciV2(int n) {

    if (fibonnaciV2_pom[n] != 0) {
      return fibonnaciV2_pom[n];
    }

    if (n == 0 || n == 1) {
      fibonnaciV2_pom[n] = n;
      return fibonnaciV2_pom[n];
    }

    fibonnaciV2_pom[n] = fibonnaciV2(n - 1) + fibonnaciV2(n - 2);

    return fibonnaciV2_pom[n];
  }

  public static void test1() {
    int n = 7;
    int wynik = 13;

    assert fibonnaciV1(n) == wynik;
    assert fibonnaciV2(n) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

