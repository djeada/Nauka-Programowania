/*
ZAD-15 — Akronim ze zdania

**Poziom:** ★☆☆
**Tagi:** `napisy`, `słowa`, `upper`

### Treść

**Akronim** to skrót utworzony z pierwszych liter kolejnych słów, np. „Polska Akademia Nauk” → `PAN`.

Wczytaj zdanie i wypisz jego akronim: pierwsze znaki wszystkich słów (zgodnie z konwencją rozdziału — bez interpunkcji), zapisane jeden za drugim **wielkimi** literami.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo; może zawierać polskie litery)

### Wyjście

Jedna linia: akronim.

### Przykład

**Wejście:**

```
Polska Akademia Nauk
```

**Wyjście:**

```
PAN
```

### Uwagi

* Słowa mogą być rozdzielone kilkoma spacjami, a zdanie może zaczynać się lub kończyć spacjami — `split()` bez argumentu poradzi sobie z tym.
* Interpunkcja nie należy do słowa: w zdaniu `(Unia Europejska)` słowami są `Unia` i `Europejska`, więc akronim to `UE`. Samotny myślnik `-` nie jest słowem.
* Zamiana na wielką literę dotyczy także polskich liter: `żółta łódź` → `ŻŁ`.

*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

public class Main {
  // Znaki interpunkcyjne (jak string.punctuation w Pythonie)
  private static final String INTERPUNKCJA = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";

  public static String usunInterpunkcje(String fragment) {
    int poczatek = 0;
    int koniec = fragment.length();
    while (poczatek < koniec && INTERPUNKCJA.indexOf(fragment.charAt(poczatek)) >= 0) {
      poczatek++;
    }
    while (koniec > poczatek && INTERPUNKCJA.indexOf(fragment.charAt(koniec - 1)) >= 0) {
      koniec--;
    }
    return fragment.substring(poczatek, koniec);
  }

  // Akronim: wielkie pierwsze litery kolejnych słów
  public static String akronim(String zdanie) {
    StringBuilder wynik = new StringBuilder();
    for (String fragment : zdanie.trim().split("\\s+")) {
      String slowo = usunInterpunkcje(fragment);
      if (!slowo.isEmpty()) {
        wynik.appendCodePoint(Character.toUpperCase(slowo.codePointAt(0)));
      }
    }
    return wynik.toString();
  }

  public static void main(String[] args) throws IOException {
    BufferedReader wejscie =
        new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
    PrintStream wyjscie = new PrintStream(System.out, true, StandardCharsets.UTF_8);
    String zdanie = wejscie.readLine();
    wyjscie.println(akronim(zdanie == null ? "" : zdanie));
  }
}
