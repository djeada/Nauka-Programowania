/*
ZAD-07 — Prawa logiki (p i q)

**Poziom:** ★★☆
**Tagi:** `bool`, `logika`, `tabele prawdy`, `formatowanie`

### Treść

Dla wszystkich kombinacji wartości logicznych `p` i `q` (True/False) sprawdź
poprawność praw:

1. Wyłączony środek: `p OR (NOT p)`
2. Niesprzeczność: `NOT (p AND (NOT p))`
3. Przemienność AND: `p AND q` vs `q AND p`
4. Przemienność OR: `p OR q` vs `q OR p`
5. De Morgana 1: `NOT (p AND q)` vs `(NOT p) OR (NOT q)`
6. De Morgana 2: `NOT (p OR q)` vs `(NOT p) AND (NOT q)`

### Wejście

Brak.

### Wyjście

Żeby wynik był **jednoznaczny i łatwy do sprawdzenia**, zastosuj dokładnie ten
format:

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
* Między blokami praw możesz wstawić **jedną pustą linię** (zalecane), ale nie
więcej.

*/
#include <iostream>

int main() {
  std::cout << "Prawo wylacznego srodka" << std::endl;
  bool p = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " wyrazenie p v ~p ma wartosc logiczna " << std::boolalpha
            << (p || !p) << std::endl;
  p = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " wyrazenie p v ~p ma wartosc logiczna " << std::boolalpha
            << (p || !p) << std::endl;

  std::cout << "\nZasada niesprzecznosci" << std::endl;
  p = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna " << std::boolalpha
            << !(p && !p) << std::endl;
  p = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna " << std::boolalpha
            << !(p && !p) << std::endl;

  std::cout << "\nPrzemiennosc koniunkcji" << std::endl;
  p = false;
  bool q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna "
            << std::boolalpha << ((p && q) == (q && p)) << std::endl;
  p = true;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna "
            << std::boolalpha << ((p && q) == (q && p)) << std::endl;
  p = false;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna "
            << std::boolalpha << ((p && q) == (q && p)) << std::endl;
  p = true;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna "
            << std::boolalpha << ((p && q) == (q && p)) << std::endl;

  std::cout << "\nPrzemiennosc alternatywy" << std::endl;
  p = false;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna "
            << std::boolalpha << ((p || q) == (q || p)) << std::endl;
  p = true;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna "
            << std::boolalpha << ((p || q) == (q || p)) << std::endl;
  p = false;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna "
            << std::boolalpha << ((p || q) == (q || p)) << std::endl;
  p = true;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna "
            << std::boolalpha << ((p || q) == (q || p)) << std::endl;

  std::cout << "\nPierwsze prawo de Morgana" << std::endl;
  p = false;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;
  p = true;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << "wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;
  p = false;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;
  p = true;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;

  std::cout << "\nDrugie prawo de Morgana" << std::endl;
  p = false;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;
  p = true;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;
  p = false;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;
  p = true;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;

  return 0;
}
