/*
ZAD-01 — Najdłuższy ciąg jedynek

**Poziom:** ★★☆
**Tagi:** `list`, `0/1`, `analiza`, `indeksy`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Znajdź **indeks zera**, które po zamianie na `1` da **najdłuższy ciąg kolejnych jedynek**.

Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz `-1`.

### Wejście

* 1 linia: lista `A` (tylko `0` i `1`)

### Wyjście

* 1 linia: indeks (liczba całkowita) albo `-1`

### Przykład

**Wejście:**

```
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
```

**Wyjście:**

```
7
```

### Uwagi

* Jeśli kilka zer daje ten sam maksymalny wynik — wybierz to o **najmniejszym indeksie** (jeśli nie określono inaczej w testach).

*/
import java.util.*;

public class Main {
  // Znajduje indeks zera, które po zamianie na 1 maksymalizuje długość podciągu jedynek
  // Złożoność czasowa: O(n) gdzie n to długość listy
  // Złożoność pamięciowa: O(1)
  public static int indeksZera(ArrayList<Integer> lista) {
    int licznikJedynek = 0;
    int licznikZer = 0;

    int indeksZera = -1;
    int poprzedniIndeksZera = -1;

    for (int i = 0; i < lista.size(); i++) {
      if (lista.get(i) == 1) {
        licznikZer++;
      } else {
        licznikZer = i - poprzedniIndeksZera;
        poprzedniIndeksZera = i;
      }

      if (licznikZer > licznikJedynek) {
        licznikJedynek = licznikZer;
        indeksZera = poprzedniIndeksZera;
      }
    }

    return indeksZera;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(0);
    lista.add(0);
    lista.add(1);
    lista.add(0);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(0);
    lista.add(1);
    lista.add(1);

    int oczekiwane = 7;
    int wynik = indeksZera(lista);
    assert (wynik == oczekiwane);
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);

    int oczekiwane = -1;
    int wynik = indeksZera(lista);
    assert (wynik == oczekiwane);
  }

  public static void test3() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    lista.add(1);
    lista.add(0);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);
    lista.add(1);

    int oczekiwane = 1;
    int wynik = indeksZera(lista);
    assert (wynik == oczekiwane);
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

