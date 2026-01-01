/*
ZAD-03 — Z ilu słów składa się zdanie?

**Poziom:** ★☆☆
**Tagi:** `string`, `split`

### Treść

Wczytaj zdanie i policz, z ilu słów się składa. Znaki interpunkcyjne nie są słowami.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: liczba słów

### Przykład

**Wejście:**

```
gram na pianinie.
```

**Wyjście:**

```
3
```

### Uwagi o formatowaniu

* Najprościej: podziel po białych znakach, a z końców słów usuń interpunkcję.

*/
import java.util.*;

public class Main {
  // Policz z ilu slow sklada sie zdanie.
  // Znaki interpunkcyjne nie sa liczone jako slowa.

  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(1)
  public static int policzSlowaV1(String slowo) {

    boolean spacja = true;
    int licznik = 0;

    for (var znak : slowo.toCharArray()) {
      if (Character.isWhitespace(znak)) {
        spacja = true;
      } else if (Character.isLetter(znak) && spacja) {
        licznik++;
        spacja = false;
      }
    }

    return licznik;
  }

  public static void test1() {
    String napis = "Ile to   ma :  slow w swoim zdaniu na   koniec?";
    int wynik = 9;

    assert policzSlowaV1(napis) == wynik;
  }

  public static void main(String[] args) {
    test1();
  }
}

