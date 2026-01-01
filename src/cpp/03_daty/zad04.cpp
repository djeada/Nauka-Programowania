/*
ZAD-04 — Dzień tygodnia z numeru

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `mapowanie`, `string`

### Treść

Wczytaj liczbę `n`. Jeśli `n` jest w zakresie 1–7, wypisz nazwę dnia tygodnia:

1. Poniedziałek
2. Wtorek
3. Środa
4. Czwartek
5. Piątek
6. Sobota
7. Niedziela

W przeciwnym razie wypisz:
`Niepoprawny numer dnia tygodnia.`

### Wejście

* 1 linia: `n` (liczba całkowita, `n ≥ 0`)

### Wyjście

Jedna linia: nazwa dnia lub komunikat o błędzie.

### Przykład

**Wejście:**

```
8
```

**Wyjście:**

```
Niepoprawny numer dnia tygodnia.
```

*/
#include <iostream>

int main() {
  std::cout << "Podaj numer dnia tygodnia:" << std::endl;

  int dzien;
  std::cin >> dzien;

  switch (dzien) {
    case 1:
      std::cout << "Pierwszym dniem tygodnia jest poniedzialek." << std::endl;
      break;

    case 2:
      std::cout << "Drugim dniem tygodnia jest wtorek." << std::endl;
      break;

    case 3:
      std::cout << "Trzecim dniem tygodnia jest sroda." << std::endl;
      break;

    case 4:
      std::cout << "Czwartym dniem tygodnia jest czwartek." << std::endl;
      break;

    case 5:
      std::cout << "Piatym dniem tygodnia jest piatek." << std::endl;
      break;

    case 6:
      std::cout << "Szostym dniem tygodnia jest sobota." << std::endl;
      break;

    case 7:
      std::cout << "Siodmym dniem tygodnia jest niedziela." << std::endl;
      break;

    default:
      std::cout << "Podano niepoprawna liczbe." << std::endl;
  }

  return 0;
}
