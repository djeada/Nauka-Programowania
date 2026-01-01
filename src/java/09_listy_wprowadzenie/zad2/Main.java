/*
ZAD-02 — Wczytaj, zmodyfikuj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `indeksy`, `modyfikacja`

### Treść

Wczytaj `N` oraz `N` liczb całkowitych do listy. Następnie:

a) Zwiększ każdy element o `1`.
b) Pomnóż każdy element przez jego indeks (indeksy od `0`).
c) Zastąp wszystkie elementy wartością pierwszego elementu.

Po każdym podpunkcie wypisz wynikową listę w **jednej** linii, elementy oddzielone przecinkami.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Trzy linie:

1. wynik po (a)
2. wynik po (b)
3. wynik po (c)

Elementy w linii oddzielone przecinkami (bez spacji).

### Przykład

**Wejście:**

```
3
3
9
7
```

**Wyjście:**

```
4,10,8
0,9,14
3,3,3
```

*/
import java.util.*;

public class Main {
  // Dla liczby N, wczytaj N liczb do listy, a nastepnie:
  public static void wczytaj(ArrayList<Integer> lista, int n) {
    for (int i = 0; i < n; i++) {
      Scanner s = new Scanner(System.in);
      int liczba = Integer.parseInt(s.nextLine());
      lista.add(liczba);
    }
  }

  // a)dodaj do kazdego elementu 1;
  public static void zwieksz(ArrayList<Integer> lista) {
    for (var liczba : lista) {
      liczba += 1;
    }
  }

  // b)pomnoz kazdy element przez jego indeks;
  public static void pomnoz(ArrayList<Integer> lista) {
    for (int i = 0; i < lista.size(); i++) {
      lista.set(i, lista.get(i) * i);
    }
  }

  // c)zastap wszystkie elementy wartoscia pierwszego elementu listy.
  public static void zastap(ArrayList<Integer> lista) {
    if (lista.isEmpty()) {
      return;
    }

    for (int i = 1; i < lista.size(); i++) {
      lista.set(i, lista.get(0));
    }
  }

  // Dla kazdego podpunktu wypisz zmodyfikowana liste. Elementy listy powinny
  // byc oddzielone przecinkami i wypisane w jednym wierszu.
  public static void wypiszOdKonca(ArrayList<Integer> lista) {
    for (var liczba : lista) {
      System.out.print(liczba);
      System.out.print(", ");
    }
    System.out.print("\n");
  }

  public static void main(String[] args) {

    ArrayList<Integer> lista = new ArrayList<Integer>();
    int n;

    System.out.print("podaj liczbe n: ");
    Scanner s = new Scanner(System.in);
    n = Integer.parseInt(s.nextLine());
    wczytaj(lista, n);

    ArrayList<Integer> kopia = new ArrayList<Integer>(lista);
    zwieksz(kopia);
    wypiszOdKonca(kopia);

    kopia = new ArrayList<Integer>(lista);
    pomnoz(kopia);
    wypiszOdKonca(kopia);

    kopia = new ArrayList<Integer>(lista);
    zastap(kopia);
    wypiszOdKonca(kopia);
  }
}

