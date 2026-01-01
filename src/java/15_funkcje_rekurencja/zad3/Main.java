/*
ZAD-03 — Suma wielomianów

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `wyrównanie stopni`, `I/O`

### Treść

Wczytaj dwa wielomiany i wypisz współczynniki wielomianu będącego ich sumą.

### Wejście

* 1. linia: `n` — stopień pierwszego wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb: `a_n ... a_0`
* 3. linia: `m` — stopień drugiego wielomianu (`m ≥ 0`)
* 4. linia: `m+1` liczb: `b_m ... b_0`

### Wyjście

Jedna linia: współczynniki sumy od najwyższej potęgi, oddzielone spacją.

### Przykład

**Wejście:**

```
2
3 5 2
2
2 -8 1
```

**Wyjście:**

```
5 -3 3
```

### Uwagi o formatowaniu

* Jeśli stopnie są różne, wyrównaj listy „od końca” (od wyrazu wolnego), dopisując zera na początku krótszej.

*/
public class Main {

  // Zlozonosc Czasowa: O(b)
  // Zlozonosc Pamieciowa: O(b) - rekurencja uzywa stosu
  public static int potegaV1(int a, int b) {

    if (b == 0) {
      return 1;
    }

    return a * potegaV1(a, b - 1);
  }

  public static void test1() {
    int a = 3;
    int b = 2;
    int wynik = 9;

    assert potegaV1(a, b) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

