/*
ZAD-05 — Sprawdzanie, czy liczba jest palindromem

**Poziom:** ★★☆
**Tagi:** `string`, `pętle`, `odwracanie`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jest palindromem (czyli czy po
odwróceniu cyfr pozostaje taka sama). Wypisz odpowiedni komunikat:

* `Liczba jest palindromem.`
* `Liczba nie jest palindromem.`

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Jeden komunikat tekstowy (dokładnie jeden z powyższych).

### Przykład

**Wejście:**

```
13231
```

**Wyjście:**

```
Liczba jest palindromem.
```

### Uwagi o formatowaniu

* `0` jest palindromem.

*/
#include <iostream>

int main() {
  int liczba;
  std::cin >> liczba;

  int odwrocona = 0;
  int temp = liczba;

  while (temp > 0) {
    int cyfra = temp % 10;
    odwrocona = (odwrocona * 10 + cyfra);
    temp /= 10;
  }

  if (odwrocona == liczba)
    std::cout << "Liczba jest palindromem." << std::endl;
  else
    std::cout << "Liczba nie jest palindromem." << std::endl;

  return 0;
}
