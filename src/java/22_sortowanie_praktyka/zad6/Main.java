/*
ZAD-06 — Scalanie nakładających się przedziałów

**Poziom:** ★★☆
**Tagi:** `sort`, `przedziały`, `tuple`

### Treść

Wczytaj $N$ przedziałów domkniętych $[a, b]$ — np. godziny zajęcia sali przez kolejne rezerwacje. Scal wszystkie przedziały, które mają **co najmniej jeden wspólny punkt**, i wypisz otrzymane rozłączne przedziały w kolejności rosnącej.

Przedziały, które się tylko stykają (koniec jednego jest początkiem drugiego), też mają wspólny punkt: $[1, 3]$ i $[3, 5]$ scalamy w $[1, 5]$. Scalanie może łączyć całe łańcuchy przedziałów, a przedział zawarty w innym po prostu w nim „znika”.

### Wejście

* 1. linia: liczba przedziałów $N$
* kolejne $N$ linii: dwie liczby całkowite $a$ i $b$ oddzielone spacją — początek i koniec przedziału

Przedziały są podane w dowolnej kolejności.

### Wyjście

Scalone przedziały posortowane rosnąco według początku — każdy w osobnej linii, jako dwie liczby (początek i koniec) oddzielone spacją.

### Ograniczenia

* $1 \le N \le 10^4$
* $-10^9 \le a \le b \le 10^9$

### Przykład

**Wejście:**

```
4
8 10
1 3
15 18
2 6
```

**Wyjście:**

```
1 6
8 10
15 18
```

Przedziały $[1, 3]$ i $[2, 6]$ mają część wspólną $[2, 3]$, więc tworzą przedział $[1, 6]$. Pozostałe przedziały są rozłączne z resztą.

### Uwagi

* Najpierw posortuj przedziały według początku (listę krotek `(a, b)` posortuje samo `sorted()`). Potem przejdź po nich raz: jeśli kolejny przedział zaczyna się nie później niż kończy się ostatni scalony, wydłuż ostatni scalony do $\max$ obu końców; w przeciwnym razie zacznij nowy scalony przedział.
* Przedziały $[1, 2]$ i $[3, 4]$ **nie** mają wspólnego punktu (choć są „sąsiadami” na osi liczb całkowitych), więc zostają osobno.
* Bez sortowania trzeba by porównywać każdą parę przedziałów — sortowanie daje rozwiązanie w czasie $O(N \log N)$.

*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
  // Scala przedziały domknięte mające wspólny punkt
  // Złożoność czasowa: O(n log n), pamięciowa: O(n)
  public static List<long[]> scalPrzedzialy(long[][] przedzialy) {
    long[][] posortowane = przedzialy.clone();
    Arrays.sort(
        posortowane,
        (p, q) -> p[0] != q[0] ? Long.compare(p[0], q[0]) : Long.compare(p[1], q[1]));

    List<long[]> scalone = new ArrayList<>();
    for (long[] przedzial : posortowane) {
      if (!scalone.isEmpty() && przedzial[0] <= scalone.get(scalone.size() - 1)[1]) {
        long[] ostatni = scalone.get(scalone.size() - 1);
        ostatni[1] = Math.max(ostatni[1], przedzial[1]);
      } else {
        scalone.add(new long[] {przedzial[0], przedzial[1]});
      }
    }
    return scalone;
  }

  public static void main(String[] args) {
    Scanner skaner = new Scanner(System.in);
    int n = skaner.nextInt();
    long[][] przedzialy = new long[n][2];
    for (int i = 0; i < n; i++) {
      przedzialy[i][0] = skaner.nextLong();
      przedzialy[i][1] = skaner.nextLong();
    }

    StringBuilder wynik = new StringBuilder();
    for (long[] przedzial : scalPrzedzialy(przedzialy)) {
      wynik.append(przedzial[0]).append(' ').append(przedzial[1]).append('\n');
    }
    System.out.print(wynik);
  }
}
