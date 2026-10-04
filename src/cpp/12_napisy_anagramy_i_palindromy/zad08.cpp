/*
ZAD-08 — Wyjątkowe palindromy (podciągi bez zmiany kolejności)

**Poziom:** ★★★
**Tagi:** `substring`, `palindrom`, `unikalność`

### Treść

Wczytaj słowo i znajdź wszystkie **unikalne** palindromy, które można z niego
utworzyć jako **spójne podciągi** (substringi), bez zmiany kolejności znaków,
spełniające warunek „wyjątkowości”:

1. wszystkie znaki są identyczne (np. `aaa`), **albo**
2. wszystkie znaki poza środkowym są identyczne (np. `cbc`).

Pojedynczy znak też jest wyjątkowym palindromem.

### Wejście

* 1. linia: słowo (litery)

### Wyjście

Każdy unikalny wyjątkowy palindrom w osobnej linii.
Jeśli nic poza pojedynczymi znakami nie pasuje, wypisz tylko te unikalne znaki
(po jednej linii na znak).

### Przykład

**Wejście:**

```
xxyxx
```

**Wyjście:**

```
x
xx
xxx
xxyxx
y
yxy
```

### Uwagi o formatowaniu

* Usuń duplikaty w wyniku (np. ten sam palindrom znaleziony w kilku miejscach
wypisz raz).
* Kolejność wypisywania może być zgodna z pierwszym pojawieniem się w tekście
(łatwe i czytelne): wypisuj przy pierwszym znalezieniu danego palindromu.

*/
#include <cassert>
#include <set>
#include <string>

// Zwraca wszystkie unikalne "wyjatkowe" palindromy bedace spojnymi
// podciagami slowa: takie, w ktorych wszystkie znaki sa identyczne (np. "aaa")
// albo wszystkie znaki poza srodkowym sa identyczne (np. "aabaa").
// Zlozonosc Czasowa: O(n^2)
// Zlozonosc Pamieciowa: O(n^2)
std::set<std::string> wyjatkowePalindromy(const std::string &slowo) {
  std::set<std::string> wynik;
  const std::size_t n = slowo.size();

  // 1. Podciagi zlozone z jednego, powtarzajacego sie znaku.
  for (std::size_t i = 0; i < n;) {
    std::size_t j = i;
    while (j < n && slowo[j] == slowo[i]) j++;

    for (std::size_t dlugosc = 1; dlugosc <= j - i; dlugosc++)
      wynik.insert(std::string(dlugosc, slowo[i]));

    i = j;
  }

  // 2. Podciagi postaci c..c x c..c, gdzie srodkowy znak x jest inny niz c.
  for (std::size_t srodek = 1; srodek + 1 < n; srodek++) {
    const char znak = slowo[srodek - 1];
    if (slowo[srodek] == znak || slowo[srodek + 1] != znak) continue;

    std::size_t k = 1;
    while (k <= srodek && srodek + k < n && slowo[srodek - k] == znak &&
           slowo[srodek + k] == znak) {
      wynik.insert(slowo.substr(srodek - k, 2 * k + 1));
      k++;
    }
  }

  return wynik;
}

void testWyjatkowePalindromy() {
  assert((wyjatkowePalindromy("xxx") ==
          std::set<std::string>{"x", "xx", "xxx"}));
  assert((wyjatkowePalindromy("ccdcc") ==
          std::set<std::string>{"cc", "d", "ccdcc", "c", "cdc"}));
  assert((wyjatkowePalindromy("abc") == std::set<std::string>{"a", "b", "c"}));
  assert((wyjatkowePalindromy("xxyxx") ==
          std::set<std::string>{"x", "xx", "y", "xyx", "xxyxx"}));
  assert((wyjatkowePalindromy("aabaaa") ==
          std::set<std::string>{"a", "aa", "aaa", "b", "aba", "aabaa"}));
  assert((wyjatkowePalindromy("abcb") ==
          std::set<std::string>{"a", "b", "c", "bcb"}));
  assert(wyjatkowePalindromy("").empty());
}

int main() {
  testWyjatkowePalindromy();

  return 0;
}
