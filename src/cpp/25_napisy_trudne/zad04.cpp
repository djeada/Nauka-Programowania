/*
ZAD-04 — Wszystkie wystąpienia podnapisu

**Poziom:** ★★☆
**Tagi:** `string`, `substring`, `find`

### Treść

Otrzymujesz napis `S` i napis `W` (wzorzec). Znajdź **wszystkie** pozycje w `S`,
od których zaczyna się wystąpienie `W`, i wypisz je w kolejności rosnącej.

Wystąpienia mogą na siebie nachodzić: w napisie `aaaa` wzorzec `aa` zaczyna się
na pozycjach `0`, `1` i `2`.

### Wejście

* 1. linia: napis `S`
* 2. linia: wzorzec `W`

### Wyjście

Jedna linia: indeksy początków wszystkich wystąpień `W` w `S`, oddzielone
pojedynczymi spacjami. Jeśli `W` nie występuje w `S`, wypisz `Brak`.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`
* `1 ≤ |W| ≤ 100`

### Przykład

**Wejście:**

```
abrakadabra
abra
```

**Wyjście:**

```
0 7
```

### Uwagi

* Spróbuj nie używać metod `find` ani `count`: dla każdej pozycji `i` od `0` do
`len(S) - len(W)` sprawdź, czy od tego miejsca zaczyna się `W` — tak jak
sprawdzałeś przedrostek w zadaniu ZAD-03.
* W przeciwieństwie do zadań ZAD-01 i ZAD-02 po znalezieniu wystąpienia **nie
przeskakujemy** go — kolejną sprawdzaną pozycją jest `i + 1`.

*/
#include <iostream>
#include <string>
#include <vector>

// Dzieli napis UTF-8 na znaki, aby indeksy odpowiadały indeksom w Pythonie.
std::vector<std::string> znakiUtf8(const std::string &napis) {
  std::vector<std::string> znaki;
  for (std::size_t i = 0; i < napis.size();) {
    unsigned char bajt = napis[i];
    std::size_t dlugosc = bajt < 0x80    ? 1
                          : bajt >= 0xF0 ? 4
                          : bajt >= 0xE0 ? 3
                                         : 2;
    znaki.push_back(napis.substr(i, dlugosc));
    i += dlugosc;
  }
  return znaki;
}

// Indeksy wszystkich (także nachodzących) wystąpień wzorca w napisie.
// Złożoność czasowa: O(n * m), pamięciowa: O(n + m)
std::vector<std::size_t> wystapienia(const std::string &napis,
                                     const std::string &wzorzec) {
  std::vector<std::string> s = znakiUtf8(napis), w = znakiUtf8(wzorzec);
  std::vector<std::size_t> pozycje;
  for (std::size_t i = 0; i + w.size() <= s.size(); i++) {
    bool pasuje = true;
    for (std::size_t j = 0; j < w.size() && pasuje; j++) {
      if (s[i + j] != w[j]) pasuje = false;
    }
    if (pasuje) pozycje.push_back(i);
  }
  return pozycje;
}

int main() {
  std::string napis, wzorzec;
  std::getline(std::cin, napis);
  std::getline(std::cin, wzorzec);
  if (!napis.empty() && napis.back() == '\r') napis.pop_back();
  if (!wzorzec.empty() && wzorzec.back() == '\r') wzorzec.pop_back();

  std::vector<std::size_t> pozycje = wystapienia(napis, wzorzec);
  if (pozycje.empty()) {
    std::cout << "Brak\n";
    return 0;
  }
  for (std::size_t i = 0; i < pozycje.size(); i++) {
    if (i > 0) std::cout << ' ';
    std::cout << pozycje[i];
  }
  std::cout << '\n';
  return 0;
}
