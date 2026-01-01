/*
ZAD-05 — Co k-ty znak poziomo i pionowo

**Poziom:** ★☆☆
**Tagi:** `string`, `slicing`, `pętle`

### Treść

Wczytaj napis i liczbę `k`.

a) Wypisz co `k`-ty znak w jednym wierszu, oddzielając znaki spacjami.
b) Wypisz co `k`-ty znak pionowo (każdy w osobnej linii).

### Wejście

* 1. linia: napis
* 2. linia: liczba naturalna `k` (k ≥ 1)

### Wyjście

* (a) 1 linia: znaki oddzielone spacjami
* (b) wiele linii: każdy znak osobno

### Przykład

**Wejście:**

```
Grzechotnik
3
```

**Wyjście:**

```
z h n
z
h
n
```

### Uwagi o formatowaniu

* Dokładnie jedna spacja między znakami w punkcie (a), bez spacji na końcu linii.

*/
import java.util.*;

public class Main {
  // Otrzymujesz napis oraz liczbe k.
  // a) wypisz poziomo co k-ty znak. Znaki powinny byc oddzielone spacjami.
  public static void wypiszPoziomo(final String napis, int k) {

    for (int i = 0; i < napis.length(); i += k) {
      System.out.print(napis.charAt(i));
      System.out.print(", ");
    }

    System.out.print("\n");
  }

  // b) wypisz pionowo co k-ty znak. Znaki powinny byc oddzielone enterami.
  public static void wypiszPionowo(final String napis, int k) {
    for (int i = 0; i < napis.length(); i += k) {
      System.out.print(napis.charAt(i));
      System.out.print("\n");
    }
  }

  public static void main(String[] args) {
    String napis = "hej dzieci jesli chcecie zobaczyc smerfow las";
    int k = 3;
    wypiszPoziomo(napis, k);
    wypiszPionowo(napis, k);
  }
}

