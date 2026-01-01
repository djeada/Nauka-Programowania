/*
ZAD-05 — Liczba dni w miesiącu (rok nieprzestępny)

**Poziom:** ★☆☆
**Tagi:** `if`, `tablice`, `walidacja`

### Treść

Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni
w tym miesiącu. Jeśli `m` nie jest w zakresie 1–12, wypisz: `Niepoprawny numer
miesiąca.`

### Wejście

* 1 linia: `m` (liczba całkowita, `m ≥ 0`)

### Wyjście

* liczba dni (jedna linia) **albo**
* komunikat o błędzie (jedna linia)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
28
```

*/
#include <iostream>

int main() {
  int numer;
  std::cin >> numer;

  switch (numer) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
      std::cout << "31" << std::endl;
      break;
    case 4:
    case 6:
    case 9:
    case 11:
      std::cout << "30" << std::endl;
      break;
    case 2:
      std::cout << "28" << std::endl;
      break;
    default:
      std::cout << "Niepoprawny numer miesiąca." << std::endl;
  }

  return 0;
}
