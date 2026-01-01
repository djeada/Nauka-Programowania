/*
ZAD-04 — Sortowanie przez scalanie

**Poziom:** ★★☆
**Tagi:** `sorting`, `merge-sort`, `recursion`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez scalanie**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
2. Podziel listę na dwie (w miarę) równe części.
3. Rekurencyjnie posortuj obie części.
4. **Scal** dwie posortowane listy w jedną posortowaną.

### Wejście

* 1 linia: lista liczb całkowitych

### Wyjście

* 1 linia: posortowana lista rosnąco

### Przykład

**Wejście:**

```
[6, 2, 1, 4, 27]
```

**Wyjście:**

```
[1, 2, 4, 6, 27]
```

### Uwagi o algorytmie

* Złożoność czasowa: `O(n log n)`.

*/
import java.util.*;

public class Main {

  // Sortowanie przez scalanie - dzieli listę na połowy i rekurencyjnie sortuje
  // Złożoność czasowa: O(n log n) - podział logarytmiczny i scalanie liniowe
  // Złożoność pamięciowa: O(n) - tworzenie pomocniczych list
  public static ArrayList<Integer> sortuj(ArrayList<Integer> lista) {
    if (lista.size() <= 1) {
      return lista;
    }
    ArrayList<Integer> posortowana = new ArrayList<Integer>();

    ArrayList<Integer> lewaLista = new ArrayList<Integer>();
    ArrayList<Integer> prawaLista = new ArrayList<Integer>();
    int middle = lista.size() / 2;

    for (int i = 0; i < lista.size(); i++) {
      if (i < middle) {
        lewaLista.add(lista.get(i));
      } else {
        prawaLista.add(lista.get(i));
      }
    }
    lewaLista = sortuj(lewaLista);
    prawaLista = sortuj(prawaLista);

    posortowana = polacz(lewaLista, prawaLista);
    return posortowana;
  }

  // Scala dwie posortowane listy w jedną posortowaną listę
  // Złożoność czasowa: O(n+m) gdzie n i m to rozmiary list
  // Złożoność pamięciowa: O(n+m)
  public static ArrayList<Integer> polacz(
      ArrayList<Integer> lewaLista, ArrayList<Integer> prawaLista) {
    ArrayList<Integer> polaczonaLista = new ArrayList<Integer>();
    while (lewaLista.size() > 0 || prawaLista.size() > 0) {
      if (lewaLista.size() > 0 && prawaLista.size() > 0) {
        if (lewaLista.get(0) < prawaLista.get(0)) {
          polaczonaLista.add(lewaLista.get(0));
          lewaLista.remove(0);
        } else {
          polaczonaLista.add(prawaLista.get(0));
          prawaLista.remove(0);
        }
      } else if (lewaLista.size() > 0) {
        polaczonaLista.add(lewaLista.get(0));
        lewaLista.remove(0);
      } else if (prawaLista.size() > 0) {
        polaczonaLista.add(prawaLista.get(0));
        prawaLista.remove(0);
      }
    }
    return polaczonaLista;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(4, 2, 5, 3, 1));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5));

    lista = sortuj(lista);
    assert lista == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

