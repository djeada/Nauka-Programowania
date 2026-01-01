/*
ZAD-01 — Sortowanie znaków w napisie

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`

### Treść

Otrzymujesz napis. Posortuj alfabetycznie wszystkie jego znaki i wypisz wynikowy napis.

### Wejście

* 1 linia: napis `s`

### Wyjście

* 1 linia: napis `s` po posortowaniu znaków rosnąco (porównanie znaków jak w Pythonie / Unicode)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
 Aaaaklmot
```

### Uwagi o formatowaniu

* Spacje też są znakami i biorą udział w sortowaniu (dlatego w przykładzie wyjście zaczyna się od spacji).

*/
import java.util.*;

public class Main {
  // Sortuje znaki w słowie alfabetycznie
  // Złożoność czasowa: O(n log n) - sortowanie wbudowane
  // Złożoność pamięciowa: O(n) - tablica znaków
  public static String sortujSlowoV1(final String slowo) {
    char[] tablica = slowo.toCharArray();
    Arrays.sort(tablica);
    return new String(tablica);
  }

  public static void test1() {

    final String napis = "bcda";
    final String oczekwiane = "abcd";

    final String wynik = sortujSlowoV1(napis);

    assert wynik.equals(oczekwiane);
  }

  public static void main(String[] args) {

    test1();
  }
}

