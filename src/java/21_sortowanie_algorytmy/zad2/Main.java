/*
ZAD-02 — Sortowanie przez wybieranie

**Poziom:** ★★☆
**Tagi:** `sorting`, `selection-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wybieranie**.
Dla każdej pozycji `i` znajdź najmniejszy element w zakresie `i..koniec` i zamień go z elementem na pozycji `i`.

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

* Złożoność czasowa: `O(n^2)`.

*/
import java.util.*;

public class Main {

  // Sortowanie przez wybieranie - dla każdej pozycji znajduje najmniejszy element
  // Złożoność czasowa: O(n²) - dwie zagnieżdżone pętle
  // Złożoność pamięciowa: O(1) - sortowanie w miejscu
  public static void sortuj(ArrayList<Integer> lista) {
    for (int i = 0; i < lista.size() - 1; i++) {
      var i_min = i;
      for (int j = i + 1; j < lista.size(); j++) {
        if (lista.get(j) < lista.get(i_min)) i_min = j;

        var temp = lista.get(i);
        lista.set(i, lista.get(i_min));
        lista.set(i_min, temp);
      }
    }
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(4, 2, 5, 3, 1));
    ArrayList<Integer> wynik = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5));

    sortuj(lista);

    assert lista == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

