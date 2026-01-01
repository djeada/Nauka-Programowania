/*
ZAD-01 — Numer dnia tygodnia lub miesiąca

**Poziom:** ★☆☆
**Tagi:** `if`, `zakresy`, `I/O`

### Treść

Wczytaj liczbę naturalną `n`. Wypisz `n` **tylko wtedy**, gdy jest poprawnym
numerem:

* dnia tygodnia (1–7) **lub**
* miesiąca (1–12).

W praktyce oznacza to: wypisz `n` tylko wtedy, gdy `1 ≤ n ≤ 12`.

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

* Jeśli `1 ≤ n ≤ 12`: wypisz `n` w osobnej linii
* W przeciwnym razie: brak wyjścia

### Przykłady

**Wejście:**

```
5
```

**Wyjście:**

```
5
```

**Wejście:**

```
15
```

**Wyjście:** *(brak)*

*/
#include <iostream>

int main() {
  std::cout << "Podaj liczbe:" << std::endl;
  int a;
  std::cin >> a;

  if (a >= 1 && a <= 7)
    std::cout << "Liczba jest poprawnym numerem tygodnia." << std::endl;

  else
    std::cout << "Liczba nie jest poprawnym numerem tygodnia." << std::endl;

  if (a >= 1 && a <= 12)
    std::cout << "Liczba jest poprawnym numerem miesiaca." << std::endl;
  else
    std::cout << "Liczba nie jest poprawnym numerem miesiaca." << std::endl;

  return 0;
}
