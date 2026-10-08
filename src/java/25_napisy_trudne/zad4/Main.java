/*
ZAD-04 — Wszystkie wystąpienia podnapisu

**Poziom:** ★★☆
**Tagi:** `string`, `substring`, `find`

### Treść

Otrzymujesz napis `S` i napis `W` (wzorzec). Znajdź **wszystkie** pozycje w `S`, od których zaczyna się wystąpienie `W`, i wypisz je w kolejności rosnącej.

Wystąpienia mogą na siebie nachodzić: w napisie `aaaa` wzorzec `aa` zaczyna się na pozycjach `0`, `1` i `2`.

### Wejście

* 1. linia: napis `S`
* 2. linia: wzorzec `W`

### Wyjście

Jedna linia: indeksy początków wszystkich wystąpień `W` w `S`, oddzielone pojedynczymi spacjami.
Jeśli `W` nie występuje w `S`, wypisz `Brak`.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`
* `1 ≤ |W| ≤ 100`

### Przykład

**Wejście:**

```
abrakadabra
abra
```

**Wyjście:**

```
0 7
```

### Uwagi

* Spróbuj nie używać metod `find` ani `count`: dla każdej pozycji `i` od `0` do `len(S) - len(W)` sprawdź, czy od tego miejsca zaczyna się `W` — tak jak sprawdzałeś przedrostek w zadaniu ZAD-03.
* W przeciwieństwie do zadań ZAD-01 i ZAD-02 po znalezieniu wystąpienia **nie przeskakujemy** go — kolejną sprawdzaną pozycją jest `i + 1`.

*/
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class Main {
  // Indeksy wszystkich (także nachodzących) wystąpień wzorca w napisie.
  // Indeksy liczone po znakach Unicode (code points), tak jak w Pythonie.
  // Złożoność czasowa: O(n * m), pamięciowa: O(n + m)
  public static List<Integer> wystapienia(String napis, String wzorzec) {
    int[] s = napis.codePoints().toArray();
    int[] w = wzorzec.codePoints().toArray();
    List<Integer> pozycje = new ArrayList<>();
    for (int i = 0; i + w.length <= s.length; i++) {
      boolean pasuje = true;
      for (int j = 0; j < w.length; j++) {
        if (s[i + j] != w[j]) {
          pasuje = false;
          break;
        }
      }
      if (pasuje) {
        pozycje.add(i);
      }
    }
    return pozycje;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader wejscie =
        new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
    PrintStream wyjscie = new PrintStream(System.out, true, StandardCharsets.UTF_8);
    String napis = wejscie.readLine();
    String wzorzec = wejscie.readLine();

    List<Integer> pozycje = wystapienia(napis, wzorzec);
    if (pozycje.isEmpty()) {
      wyjscie.println("Brak");
    } else {
      StringBuilder wynik = new StringBuilder();
      for (int i = 0; i < pozycje.size(); i++) {
        if (i > 0) {
          wynik.append(' ');
        }
        wynik.append(pozycje.get(i));
      }
      wyjscie.println(wynik);
    }
  }
}
