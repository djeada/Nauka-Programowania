/*
ZAD-06 — Wiersze kończące się określonym napisem

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`, `linijki`

### Treść

Otrzymujesz dwa napisy:

1. tekst wielowierszowy,
2. słowo lub fragment.

Znajdź wszystkie wiersze, które kończą się podanym napisem (wiersz może kończyć się znakiem interpunkcyjnym).

### Wejście

Dwie części:

1. Tekst (wiele wierszy)
2. W osobnej linii: `koncowka`

*(Sposób wczytania tekstu wielowierszowego zależy od platformy — przyjmij, że tekst jest podany w całości jako wejście, a ostatnia linia to `koncowka`.)*

### Wyjście

Wiersze spełniające warunek, każdy w osobnej linii, w kolejności występowania.

### Przykład

**Wejście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godności trzeba nie za nic tu cnota,
Miłości pragną nie pragną tu złota.
da
```

**Wyjście:**

```
Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
```

*/
import java.util.*;
import java.util.regex.Pattern;

public class Main {
  public static ArrayList<String> znajdzWierszeV1(String napis, String podnapis) {
    ArrayList<String> wynik = new ArrayList<String>();
    String[] tablica = napis.split("\n");
    for (String wiersz : tablica) {
      if (wiersz.endsWith(podnapis)) {
        wynik.add(wiersz);
      }
    }
    return wynik;
  }

  public static ArrayList<String> znajdzWierszeV2(String napis, String podnapis) {
    // using regex
    ArrayList<String> wynik = new ArrayList<String>();
    String regex = ".*" + Pattern.quote(podnapis) + ".*";
    String[] tablica = napis.split("\n");
    for (String wiersz : tablica) {
      if (wiersz.matches(regex)) {
        wynik.add(wiersz);
      }
    }

    return wynik;
  }

  public static void test1() {
    String tekst =
        "Folgujmy paniom nie sobie, ma rada;\nMilujmy wiernie "
            + "nie jest w nich przysada.\nGodnosci trzeba nie za nic "
            + "tu cnota,\nMilosci pragna nie pragna tu zlota";
    String napis = "ada";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("Folgujmy paniom nie sobie, ma rada;");
    oczekiwane.add("Milujmy wiernie nie jest w nich przysada.");
    assert (znajdzWierszeV1(tekst, napis).equals(oczekiwane));
  }

  public static void test2() {
    String tekst =
        "Folgujmy paniom nie sobie, ma rada;\nMilujmy wiernie "
            + "nie jest w nich przysada.\nGodnosci trzeba nie za nic "
            + "tu cnota,\nMilosci pragna nie pragna tu zlota";
    String napis = "ada";
    ArrayList<String> oczekiwane = new ArrayList<String>();
    oczekiwane.add("Folgujmy paniom nie sobie, ma rada;");
    oczekiwane.add("Milujmy wiernie nie jest w nich przysada.");
    assert (znajdzWierszeV2(tekst, napis).equals(oczekiwane));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

