/*
ZAD-02 — Sprawdź poprawność hasła

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `walidacja`

### Treść

Otrzymujesz napis reprezentujący hasło. Sprawdź, czy hasło spełnia wszystkie warunki:

1. Zawiera co najmniej jedną małą literę `[a–z]`.
2. Zawiera co najmniej jedną wielką literę `[A–Z]`.
3. Zawiera co najmniej jedną cyfrę `[0–9]`.
4. Zawiera co najmniej jeden znak specjalny spośród:
   `!`, `#`, `$`, `%`, `&`, `'`, `*`, `+`, `-`, `/`, `=`, `?`, `^`, `_`, `` ` ``, `{`, `|`, `}`, `~`.
5. Ma długość co najmniej 8 znaków.
6. Ma długość nie większą niż 20 znaków.

### Wejście

Jedna linia:

* `haslo`

### Wyjście

Jedna linia:

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
abc1234
```

**Wyjście:**

```
Fałsz
```

*/
import java.util.*;

public class Main {

  // Sprawdza czy hasło spełnia wszystkie wymagania bezpieczeństwa
  // Złożoność czasowa: O(n) gdzie n to długość hasła
  // Złożoność pamięciowa: O(1)
  public static boolean poprawneHaslo(String haslo) {
    if (haslo.matches("[a-z]+") && haslo.matches("[A-Z]+")) {
      if (haslo.matches("[0-9]+") && haslo.matches("[!#$%&'*+-/=?^_`{|}~]+"))
        return haslo.length() >= 8 && haslo.length() <= 20;
    }

    return false;
  }

  public static void test1() {
    List<String> poprawneHasla =
        Arrays.asList(
            "HulaKula123!",
            "$$KAsiORA302$$",
            "X'nQz{sH:6k4*3+T",
            "=3Xv+D]?''(_",
            "Mt`VXsD^47+'H-",
            "]t'N\"mtH'W9p<_<Vc)=",
            "b5TMq2L:'{f&",
            "_t}s%Ymu2YP>w",
            "'zGFbJg)~6;}",
            "\"Tuqb}h7)2Gv",
            "Ng2+]zLR7)nX7UXM]`T",
            ",{QPW7H+7za?95K&:wP");

    for (String haslo : poprawneHasla) assert (poprawneHaslo(haslo));
  }

  public static void test2() {
    List<String> niepoprawneHasla =
        Arrays.asList(
            "123456",
            "proste_haslo123",
            "haslo",
            "pizza&*!",
            "!!!!!!!!",
            "_____123_____",
            "...",
            "abcd32",
            "AB***DB",
            "22tajnE",
            "Ab6*");

    for (String haslo : niepoprawneHasla) assert (!poprawneHaslo(haslo));
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

