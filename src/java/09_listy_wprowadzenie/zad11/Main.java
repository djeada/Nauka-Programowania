/*
ZAD-11 — Samochody jadące w przeciwnych kierunkach

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`, `string`

### Treść

Wczytaj `N` oraz napis długości `N` złożony z liter `A` i `B`:

* `A` oznacza samochód jadący na wschód,
* `B` oznacza samochód jadący na zachód.

Policz, ile par samochodów minie się, gdy uznamy, że para mija się wtedy, gdy `A` stoi **przed** `B` w ciągu.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* 2. linia: napis długości `N`, tylko `A` i `B` (bez spacji)

### Wyjście

Jedna liczba naturalna — liczba mijających się par.

### Przykład

**Wejście:**

```
5
ABABB
```

**Wyjście:**

```
5
```

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste skladajaca sie z ciagu liter A i B.
  // Litery A reprezentuja samochod jadacy na wschod, a
  // litery B jadacy na zachod.  Samochody jadace w przeciwna
  // stronw mijaja sie. Policz mijajace sie samochody.

  public static int policzSamochodyV1(ArrayList<Character> lista) {

    int licznik = 0;

    for (int i = 0; i < lista.size(); i++) {
      if (lista.get(i) == 'A') {
        for (int j = i + 1; j < lista.size(); j++) {
          if (lista.get(j) == 'B') {
            licznik++;
          }
        }
      } else if (lista.get(i) == 'B') {
        for (int j = i - 1; j > -1; j--) {
          if (lista.get(j) == 'A') {
            licznik++;
          }
        }
      }
    }

    return licznik / 2;
  }

  public static int policzSamochodyV2(ArrayList<Character> lista) {
    int licznik = 0;
    int pom = 0;

    for (var x : lista) {
      if (x == 'A') {
        pom++;
      } else if (x == 'B') {
        licznik += pom;
      }
    }

    return licznik;
  }

  public static void test1() {
    ArrayList<Character> lista = new ArrayList<Character>(Arrays.asList('A', 'B', 'A', 'B', 'B'));
    int wynik = 5;
    assert policzSamochodyV1(lista) == wynik;
    assert policzSamochodyV2(lista) == wynik;
  }

  public static void test2() {
    ArrayList<Character> lista =
        new ArrayList<Character>(
            Arrays.asList('A', 'A', 'A', 'B', 'B', 'A', 'B', 'A', 'B', 'A', 'A', 'A'));
    int wynik = 15;
    assert policzSamochodyV1(lista) == wynik;
    assert policzSamochodyV2(lista) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

