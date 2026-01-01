/*
ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami

**Poziom:** ★★★
**Tagi:** `binarne`, `binary gap`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. W jej reprezentacji binarnej znajdź długość najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami** (tzw. *binary gap*).

Jeśli nie ma takiego ciągu — wypisz `0`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: długość najdłuższego „gapu”.

### Przykład

**Wejście:**

```
14
```

**Wyjście:**

```
0
```

### Uwagi (ważne)

* `14` ma zapis `1110` — zero na końcu **nie jest otoczone jedynkami z prawej**, więc wynik to `0`.
  Dla przykładu `20` (`10100`) najdłuższy gap ma długość `1` (między `1` i `1`).

*/
public class Main {
  // Znajdz dlugosc najdluzszego ciagu zer w liczbie binarnej.

  // Zlozonosc Czasowa: O(log n)
  // Zlozonosc Pamieciowa: O(1)
  public static int najdluzszyCiagZer(int liczba) {
    if (liczba == 0) {
      return 1;
    }

    int wynik = 0;
    int pom = 0;

    while (liczba != 0) {
      int reszta = liczba % 2;
      liczba /= 2;
      if (reszta == 1) {
        wynik = Math.max(wynik, pom);
        pom = 0;
      } else {
        pom++;
      }
    }
    return Math.max(wynik, pom);
  }

  public static void test1() {
    int liczba = 111;
    int wynik = 1;

    assert najdluzszyCiagZer(liczba) == wynik;
  }

  public static void test2() {
    int liczba = 8219;
    int wynik = 8;

    assert najdluzszyCiagZer(liczba) == wynik;
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

