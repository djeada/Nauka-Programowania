/*
ZAD-02 — Sortowanie słów w zdaniu

**Poziom:** ★★☆
**Tagi:** `sort`, `string`, `split`

### Treść

Otrzymujesz zdanie. Podziel je na słowa, traktując znaki interpunkcyjne jako separatory, a następnie posortuj słowa alfabetycznie i wypisz listę.

### Wejście

* 1 linia: napis `zdanie`

### Wyjście

* 1 linia: lista słów w formacie jak w przykładzie, np. `['Ala', 'kota', 'ma']`

### Przykład

**Wejście:**

```
Lemur wygina śmiało ciało
```

**Wyjście:**

```
['Lemur', 'ciało', 'wygina', 'śmiało']
```

### Uwagi o formatowaniu

* Ignoruj znaki interpunkcyjne (np. `.,!?;:`) — nie są częścią słów.
* Wielkość liter pozostaje bez zmian (nie zamieniaj na małe/duże), sortujesz to, co w tekście.

*/
import java.util.*;

public class Main {

  public static String wyczysc(final String napis) {
    return napis.trim().replaceAll("\\p{Punct}", "");
  }

  public static ArrayList<String> slowa(final String napis) {
    ArrayList<String> wynik = new ArrayList<String>();
    int pocz = 0;
    int konc = 0;
    while ((konc = napis.indexOf(' ', pocz)) != -1) {
      if (konc != pocz) {
        var slowo = napis.substring(pocz, konc);
        slowo = wyczysc(slowo);
        if (!slowo.isEmpty()) {
          wynik.add(slowo);
        }
      }
      pocz = konc + 1;
    }
    if (konc != pocz) {
      var slowo = napis.substring(pocz);
      slowo = wyczysc(slowo);
      if (!slowo.isEmpty()) {
        wynik.add(slowo);
      }
    }

    return new ArrayList<String>(wynik);
  }

  public static ArrayList<String> sortuj(final String zdanie) {
    ArrayList<String> wynik = slowa(zdanie);
    Collections.sort(wynik);
    return wynik;
  }

  public static void test1() {
    final String napis = "Lemur wygina smialo cialo";
    final ArrayList<String> oczekiwane =
        new ArrayList<String>(Arrays.asList("Lemur", "cialo", "smialo", "wygina"));
    final ArrayList<String> wynik = sortuj(napis);

    assert oczekiwane.equals(wynik);
  }

  public static void main(String[] args) {

    test1();
  }
}

