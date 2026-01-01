/*
ZAD-05 — Sortowanie listy miast

**Poziom:** ★☆☆
**Tagi:** `class`, `sort`, `obiekty`

### Treść

Masz klasę `Miasto` z polami:

* `nazwa` (napis),
* `liczba_mieszkancow` (liczba naturalna).

Otrzymujesz listę miast.

a) Posortuj miasta alfabetycznie po nazwie.
b) Posortuj miasta rosnąco po liczbie mieszkańców.

Wypisz wyniki w dwóch liniach jako listy w formacie jak w przykładzie.

### Wejście

* 1 linia: liczba naturalna `N`
* następnie `N` linii: `nazwa liczba_mieszkancow` (nazwa bez spacji)

### Wyjście

* 1 linia: lista miast po sortowaniu a)
* 2 linia: lista miast po sortowaniu b)

### Przykład

**Wejście:**

```
3
Paris 2150000
Berlin 3800000
New_York 8400000
```

**Wyjście:**

```
[Miasto("Berlin", 3800000), Miasto("New_York", 8400000), Miasto("Paris", 2150000)]
[Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New_York", 8400000)]
```

### Uwagi o formatowaniu

* Wydruk obiektów ma mieć dokładnie format: `Miasto("NAZWA", LICZBA)`.

*/
import java.util.*;

public class Main {

  // Klasa reprezentująca miasto z nazwą i liczbą mieszkańców
  private static class Miasto implements Comparable<Miasto> {
    private final String nazwa;
    private final int liczba_mieszkancow;

    public Miasto(final String nazwa, final int liczba_mieszkancow) {
      this.nazwa = nazwa;
      this.liczba_mieszkancow = liczba_mieszkancow;
    }

    public String getNazwa() {
      return nazwa;
    }

    public int getLiczba_mieszkancow() {
      return liczba_mieszkancow;
    }

    @Override
    public int compareTo(final Miasto o) {
      if (nazwa.compareTo(o.nazwa) < 0) {
        return -1;
      } else if (nazwa.compareTo(o.nazwa) > 0) {
        return 1;
      } else {
        return 0;
      }
    }
  }

  public static void sortujWzgledemNazwy(ArrayList<Miasto> lista) {
    Collections.sort(
        lista,
        new Comparator<Miasto>() {
          @Override
          public int compare(final Miasto o1, final Miasto o2) {
            return o1.nazwa.compareTo(o2.nazwa);
          }
        });
  }

  public static void sortujWzgledemLiczbyMieszkancow(ArrayList<Miasto> lista) {
    Collections.sort(
        lista,
        new Comparator<Miasto>() {
          @Override
          public int compare(final Miasto o1, final Miasto o2) {
            return o1.liczba_mieszkancow - o2.liczba_mieszkancow;
          }
        });
  }

  public static void test1() {
    ArrayList<Miasto> miasta =
        new ArrayList<Miasto>(
            Arrays.asList(
                new Miasto("New York", 8400000),
                new Miasto("Paris", 2150000),
                new Miasto("Berlin", 3800000)));
    ArrayList<Miasto> oczekiwane =
        new ArrayList<Miasto>(
            Arrays.asList(
                new Miasto("Berlin", 3800000),
                new Miasto("New York", 8400000),
                new Miasto("Paris", 2150000)));

    sortujWzgledemNazwy(miasta);

    assert miasta.equals(oczekiwane);
  }

  public static void test2() {
    ArrayList<Miasto> miasta =
        new ArrayList<Miasto>(
            Arrays.asList(
                new Miasto("New York", 8400000),
                new Miasto("Paris", 2150000),
                new Miasto("Berlin", 3800000)));

    ArrayList<Miasto> oczekiwane =
        new ArrayList<Miasto>(
            Arrays.asList(
                new Miasto("Paris", 2150000),
                new Miasto("Berlin", 3800000),
                new Miasto("New York", 8400000)));
    sortujWzgledemLiczbyMieszkancow(miasta);

    assert miasta.equals(oczekiwane);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

