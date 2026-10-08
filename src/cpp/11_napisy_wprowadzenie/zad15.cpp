/*
ZAD-15 — Akronim ze zdania

**Poziom:** ★☆☆
**Tagi:** `napisy`, `słowa`, `upper`

### Treść

**Akronim** to skrót utworzony z pierwszych liter kolejnych słów, np. „Polska
Akademia Nauk” → `PAN`.

Wczytaj zdanie i wypisz jego akronim: pierwsze znaki wszystkich słów (zgodnie z
konwencją rozdziału — bez interpunkcji), zapisane jeden za drugim **wielkimi**
literami.

### Wejście

* 1. linia: zdanie (zawiera co najmniej jedno słowo; może zawierać polskie
litery)

### Wyjście

Jedna linia: akronim.

### Przykład

**Wejście:**

```
Polska Akademia Nauk
```

**Wyjście:**

```
PAN
```

### Uwagi

* Słowa mogą być rozdzielone kilkoma spacjami, a zdanie może zaczynać się lub
kończyć spacjami — `split()` bez argumentu poradzi sobie z tym.
* Interpunkcja nie należy do słowa: w zdaniu `(Unia Europejska)` słowami są
`Unia` i `Europejska`, więc akronim to `UE`. Samotny myślnik `-` nie jest
słowem.
* Zamiana na wielką literę dotyczy także polskich liter: `żółta łódź` → `ŻŁ`.

*/
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>

// Usuwa znaki interpunkcyjne ASCII (jak string.punctuation) z obu końców.
std::string usunInterpunkcje(const std::string &fragment) {
  std::size_t poczatek = 0, koniec = fragment.size();
  while (poczatek < koniec &&
         std::ispunct(static_cast<unsigned char>(fragment[poczatek])))
    poczatek++;
  while (koniec > poczatek &&
         std::ispunct(static_cast<unsigned char>(fragment[koniec - 1])))
    koniec--;
  return fragment.substr(poczatek, koniec - poczatek);
}

// Zamienia pierwszy znak słowa (w UTF-8) na wielką literę. Obsługuje litery
// ASCII oraz polskie litery ą ć ę ł ń ó ś ź ż.
std::string pierwszaWielka(const std::string &slowo) {
  unsigned char bajt = slowo[0];
  if (bajt < 0x80) {
    return std::string(1, static_cast<char>(std::toupper(bajt)));
  }

  // Długość znaku w UTF-8 i jego kod (punkt kodowy Unicode).
  std::size_t dlugosc = (bajt >= 0xF0) ? 4 : (bajt >= 0xE0) ? 3 : 2;
  std::string znak = slowo.substr(0, dlugosc);
  if (dlugosc != 2) return znak;
  int kod =
      ((bajt & 0x1F) << 6) | (static_cast<unsigned char>(slowo[1]) & 0x3F);

  switch (kod) {
    case 0x0105:
    case 0x0107:
    case 0x0119:
    case 0x0142:
    case 0x0144:
    case 0x015B:
    case 0x017A:
    case 0x017C:
      kod -= 1;  // małe polskie litery (poza ó) leżą tuż za wielkimi
      break;
    case 0x00F3:  // ó -> Ó
      kod = 0x00D3;
      break;
    default:
      return znak;
  }
  std::string wynik;
  wynik += static_cast<char>(0xC0 | (kod >> 6));
  wynik += static_cast<char>(0x80 | (kod & 0x3F));
  return wynik;
}

std::string akronim(const std::string &zdanie) {
  std::istringstream strumien(zdanie);
  std::string fragment, wynik;
  while (strumien >> fragment) {
    std::string slowo = usunInterpunkcje(fragment);
    if (!slowo.empty()) wynik += pierwszaWielka(slowo);
  }
  return wynik;
}

int main() {
  std::string zdanie;
  std::getline(std::cin, zdanie);
  std::cout << akronim(zdanie) << '\n';
  return 0;
}
