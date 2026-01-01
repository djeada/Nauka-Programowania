/*
ZAD-03 — Sortowanie przez wstawianie

**Poziom:** ★★☆
**Tagi:** `sorting`, `insertion-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez wstawianie**.
Buduj posortowany fragment od lewej strony: każdy kolejny element „wstaw” w odpowiednie miejsce, przesuwając większe elementy w prawo.

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

* Działa bardzo dobrze dla danych prawie posortowanych.

*/
import java.util.*;

public class Main {
  // Sortowanie przez wstawianie - buduje posortowany fragment od lewej
  // Złożoność czasowa: O(n²) w najgorszym przypadku, O(n) dla danych prawie posortowanych
  // Złożoność pamięciowa: O(1) - sortowanie w miejscu
  public static void sortuj(ArrayList<Integer> lista) {

    for (int i = 1; i < lista.size(); i++) {
      var klucz = lista.get(i);
      var j = i - 1;

      while (j >= 0 && lista.get(j) > klucz) {
        lista.set(j + 1, lista.get(j));
        j--;
      }

      lista.set(j + 1, klucz);
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

