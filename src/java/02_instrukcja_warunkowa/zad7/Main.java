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
package test;

public class Main {
  public static void main(String[] args) {

    // Prawo wylacznego srodka
    System.out.print("Prawo wylacznego srodka");
    System.out.print(System.getProperty("line.separator"));
    boolean p = false;
    System.out.print("dla p majacego wartosc logiczna ");
    System.out.print(p);
    System.out.print(" wyrazenie p v ~p ma wartosc logiczna ");
    System.out.printf("%b", (p || !p));
    System.out.printf(System.getProperty("line.separator"));
    p = true;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" wyrazenie p v ~p ma wartosc logiczna ");
    System.out.printf("%b", (p || !p));
    System.out.printf(System.getProperty("line.separator"));

    // Zasada niesprzecznosci
    System.out.printf("\nZasada niesprzecznosci");
    System.out.printf(System.getProperty("line.separator"));
    p = false;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" wyrazenie ~(p Ʌ ~p) ma wartosc logiczna ");
    System.out.printf("%b", !(p && !p));
    System.out.printf(System.getProperty("line.separator"));
    p = true;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" wyrazenie ~(p Ʌ ~p) ma wartosc logiczna ");
    System.out.printf("%b", !(p && !p));
    System.out.printf(System.getProperty("line.separator"));

    // Przemiennosc koniunkcji
    System.out.printf("\nPrzemiennosc koniunkcji");
    System.out.printf(System.getProperty("line.separator"));
    p = false;
    boolean q = false;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" oraz q majacego wartosc logiczna ");
    System.out.printf("%b", q);
    System.out.printf(" wyrazenie (p Ʌ q)<= > (q Ʌ p) ma wartosc logiczna ");
    System.out.printf("%b", ((p && q) == (q && p)));
    System.out.printf(System.getProperty("line.separator"));
    p = true;
    q = false;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" oraz q majacego wartosc logiczna ");
    System.out.printf("%b", q);
    System.out.printf(" wyrazenie (p Ʌ q)<= > (q Ʌ p) ma wartosc logiczna ");
    System.out.printf("%b", ((p && q) == (q && p)));
    System.out.printf(System.getProperty("line.separator"));
    p = false;
    q = true;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" oraz q majacego wartosc logiczna ");
    System.out.printf("%b", q);
    System.out.printf(" wyrazenie (p Ʌ q)<= > (q Ʌ p) ma wartosc logiczna ");
    System.out.printf("%b", ((p && q) == (q && p)));
    System.out.printf(System.getProperty("line.separator"));
    p = true;
    q = true;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" oraz q majacego wartosc logiczna ");
    System.out.printf("%b", q);
    System.out.printf(" wyrazenie (p Ʌ q)<= > (q Ʌ p) ma wartosc logiczna ");
    System.out.printf("%b", ((p && q) == (q && p)));
    System.out.printf(System.getProperty("line.separator"));

    // Przemiennosc alternatywy
    System.out.printf("\nPrzemiennosc alternatywy");
    System.out.printf(System.getProperty("line.separator"));
    p = false;
    q = false;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" oraz q majacego wartosc logiczna ");
    System.out.printf("%b", q);
    System.out.printf(" wyrazenie (p v q)<= > (q v p) ma wartosc logiczna ");
    System.out.printf("%b", ((p || q) == (q || p)));
    System.out.printf(System.getProperty("line.separator"));
    p = true;
    q = false;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" oraz q majacego wartosc logiczna ");
    System.out.printf("%b", q);
    System.out.printf(" wyrazenie (p v q)<= > (q v p) ma wartosc logiczna ");
    System.out.printf("%b", ((p || q) == (q || p)));
    System.out.printf(System.getProperty("line.separator"));
    p = false;
    q = true;
    System.out.printf("dla p majacego wartosc logiczna ");
    System.out.printf("%b", p);
    System.out.printf(" oraz q majacego wartosc logiczna ");
    System.out.printf("%b", q);
    System.out.printf(" wyrazenie (p v q)<= > (q v p) ma wartosc logiczna ");
    System.out.printf("%b", ((p || q) == (q || p)));
    System.out.printf(System.getProperty("line.separator"));
  }
}

