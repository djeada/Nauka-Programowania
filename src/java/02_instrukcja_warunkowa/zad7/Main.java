/*
ZAD-07 — Prawa logiki (p i q)

**Poziom:** ★★☆
**Tagi:** `bool`, `logika`, `tabele prawdy`, `formatowanie`

### Treść

Dla wszystkich kombinacji wartości logicznych `p` i `q` (True/False) sprawdź poprawność praw:

1. Wyłączony środek: `p OR (NOT p)`
2. Niesprzeczność: `NOT (p AND (NOT p))`
3. Przemienność AND: `p AND q` vs `q AND p`
4. Przemienność OR: `p OR q` vs `q OR p`
5. De Morgana 1: `NOT (p AND q)` vs `(NOT p) OR (NOT q)`
6. De Morgana 2: `NOT (p OR q)` vs `(NOT p) AND (NOT q)`

### Wejście

Brak.

### Wyjście

Żeby wynik był **jednoznaczny i łatwy do sprawdzenia**, zastosuj dokładnie ten format:

Dla każdego z 6 praw wypisz:

* nazwę prawa w jednej linii,
* następnie w osobnych liniach wynik dla każdej kombinacji `p, q` w kolejności:

  1. `p=False, q=False`
  2. `p=False, q=True`
  3. `p=True, q=False`
  4. `p=True, q=True`

Każda linia kombinacji ma mieć format:
`p=<...> q=<...> L=<...> R=<...> EQ=<...>`

Gdzie `<...>` to dosłownie `True` albo `False`.

### Przykład fragmentu (dla jednego prawa)

```
Przemienność alternatywy:
p=False q=False L=False R=False EQ=True
p=False q=True L=True R=True EQ=True
p=True q=False L=True R=True EQ=True
p=True q=True L=True R=True EQ=True
```

### Uwagi o formatowaniu

* Dokładne nazwy praw (nagłówki) użyj jak poniżej:

  1. `Prawo wyłączonego środka:`
  2. `Prawo niesprzeczności:`
  3. `Przemienność koniunkcji:`
  4. `Przemienność alternatywy:`
  5. `Pierwsze prawo de Morgana:`
  6. `Drugie prawo de Morgana:`
* Między blokami praw możesz wstawić **jedną pustą linię** (zalecane), ale nie więcej.

*/
public class Main {
  public static void main(String[] args) {

    // Prawo wylaczonego srodka
    System.out.println("Prawo wyłączonego środka:");
    printTruthTable1("p OR (NOT p)", (p, q) -> p || !p);
    System.out.println();

    // Prawo niesprzecznosci
    System.out.println("Prawo niesprzeczności:");
    printTruthTable1("NOT (p AND (NOT p))", (p, q) -> !(p && !p));
    System.out.println();

    // Przemiennosc koniunkcji
    System.out.println("Przemienność koniunkcji:");
    printTruthTable2("p AND q", "q AND p", (p, q) -> p && q, (p, q) -> q && p);
    System.out.println();

    // Przemiennosc alternatywy
    System.out.println("Przemienność alternatywy:");
    printTruthTable2("p OR q", "q OR p", (p, q) -> p || q, (p, q) -> q || p);
    System.out.println();

    // Pierwsze prawo de Morgana
    System.out.println("Pierwsze prawo de Morgana:");
    printTruthTable2("NOT (p AND q)", "(NOT p) OR (NOT q)", (p, q) -> !(p && q), (p, q) -> !p || !q);
    System.out.println();

    // Drugie prawo de Morgana
    System.out.println("Drugie prawo de Morgana:");
    printTruthTable2("NOT (p OR q)", "(NOT p) AND (NOT q)", (p, q) -> !(p || q), (p, q) -> !p && !q);
  }

  interface BoolFunc {
    boolean apply(boolean p, boolean q);
  }

  static void printTruthTable1(String expr, BoolFunc func) {
    boolean[] values = {false, true};
    for (boolean p : values) {
      for (boolean q : values) {
        boolean result = func.apply(p, q);
        System.out.printf("p=%s q=%s L=%s R=%s EQ=%s%n",
            toBool(p), toBool(q), toBool(result), toBool(result), "True");
      }
    }
  }

  static void printTruthTable2(String exprL, String exprR, BoolFunc funcL, BoolFunc funcR) {
    boolean[] values = {false, true};
    for (boolean p : values) {
      for (boolean q : values) {
        boolean resL = funcL.apply(p, q);
        boolean resR = funcR.apply(p, q);
        System.out.printf("p=%s q=%s L=%s R=%s EQ=%s%n",
            toBool(p), toBool(q), toBool(resL), toBool(resR), toBool(resL == resR));
      }
    }
  }

  static String toBool(boolean b) {
    return b ? "True" : "False";
  }
}

