/*
ZAD-01 — Obliczanie średniej z n liczb

**Poziom:** ★☆☆
**Tagi:** `pętle`, `suma`, `średnia`, `float`

### Treść

Napisz funkcję `oblicz_srednia()`, która:

1. Wczytuje liczbę naturalną `n` (`n ≥ 1`).
2. Wczytuje następnie `n` liczb (całkowitych lub zmiennoprzecinkowych).
3. Zwraca ich średnią arytmetyczną.

### Wejście

* 1. linia: `n` (`n ≥ 1`)
* kolejne `n` linii: liczby (int lub float)

### Wyjście

Funkcja zwraca jedną liczbę zmiennoprzecinkową — średnią arytmetyczną.

### Przykład

**Wejście:**

```
2
4
6
```

**Wywołanie funkcji:**

```python
wynik = oblicz_srednia()
print(wynik)
```

**Wyjście:**

```
5.0
```

### Uwagi o formatowaniu

* Nie narzucamy liczby miejsc po przecinku — wypisz wynik w domyślnym formacie
języka (lub jako `float`).

*/
#include <iostream>

float srednia(int n) {
  float suma = 0.0;
  int x;

  for (int i = 0; i < n; i++) {
    std::cout << "Podaj liczbe: " << std::endl;
    std::cin >> x;
    suma += x;
  }

  return suma / n;
}

int main() {
  std::cout << "Podaj liczbe n: " << std::endl;
  int n;
  std::cin >> n;

  float wynik = srednia(n);

  std::cout << "Srednia z podanych liczb to " << wynik << std::endl;

  return 0;
}
