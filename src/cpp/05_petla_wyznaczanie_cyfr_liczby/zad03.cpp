/*
ZAD-03 — Sumowanie cyfr liczby

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i oblicz sumę jej cyfr. Następnie wypisz wynik.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jedna liczba naturalna — suma cyfr liczby `n`.

### Przykład

**Wejście:**

```
129
```

**Wyjście:**

```
12
```

### Uwagi o formatowaniu

* Dla `n = 0` suma cyfr wynosi `0`.

*/
#include <iostream>

int main() {
  std::cout << "Podaj liczbe" << std::endl;
  int liczba;
  std::cin >> liczba;

  int suma = 0;

  while (liczba > 0) {
    suma += (liczba % 10);
    liczba = liczba / 10;
  }

  std::cout << "Suma cyfr podanej liczby wynosi " << suma << std::endl;

  return 0;
}
