/*
ZAD-07 — Zamiana sąsiadujących bitów

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `maski`, `swap bits`

### Treść

Wczytaj liczbę naturalną `n`. Zamień miejscami każdą parę sąsiadujących bitów w jej zapisie binarnym:

* bit 0 z bitem 1,
* bit 2 z bitem 3,
* bit 4 z bitem 5,
* itd.

Następnie wypisz wynik w systemie dziesiętnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: wynik po zamianie bitów.

### Przykład

**Wejście:**

```
9131
```

**Wyjście:**

```
4951
```

### Uwagi

* Jeśli liczba ma nieparzystą liczbę bitów, najwyższy (samotny) bit pozostaje bez zmian.

*/
public class Main {
  // Zamien miejscami sasiadujace bity.
  
  // Zlozonosc Czasowa: O(1)
  // Zlozonosc Pamieciowa: O(1)
  public static int zamienSasiadow(int liczba) {
    int parzyste = (int) (liczba & 0xAAAAAAAA);
    int nieparzyste = liczba & 0x55555555;

    parzyste >>= 1;
    nieparzyste <<= 1;

    return parzyste | nieparzyste;
  }

  public static void test1() {
    int liczba = 9131;
    int wynik = 4951;

    assert zamienSasiadow(liczba) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

