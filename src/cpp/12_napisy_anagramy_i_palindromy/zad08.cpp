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
#include <algorithm>
#include <cassert>
#include <set>
#include <string>
#include <vector>

// Zlozonosc Czasowa: O(n^2)
// Zlozonosc Pamieciowa: O(n)
std::set<std::string> wyjatkowePalindromy(const std::string slowo) {
  std::set<std::string> wynik;

  for (unsigned int i = 0; i < slowo.size(); i++) {
    wynik.insert(std::string(1, slowo[i]));

    unsigned int j = i + 1;
    unsigned int k = 0;
    while (j < slowo.size() && slowo[i] == slowo[j]) j++;

    if (j > i + 1) wynik.insert(slowo.substr(i, i - j));

    if (j + 1 < slowo.size() && slowo[i] == slowo[j + 1]) k = j + 1;

    while (k > i && slowo[i] == slowo[k]) k--;

    if (i + 1 == k) wynik.insert(slowo.substr(i, 2 * (j - i) + 1));
  }

  return wynik;
}

void testWyjatkowePalindromy() {
  assert(wyjatkowePalindromy("xxx") ==
         std::set<std::string>{"x", "xx", "xxx", "xxxx"});
  assert(wyjatkowePalindromy("ccdcc") ==
         std::set<std::string>{"cc", "d", "ccdcc", "c", "cdc"});
  assert(wyjatkowePalindromy("abc") == std::set<std::string>{"a", "b", "c"});
  assert(wyjatkowePalindromy("") == std::set<std::string>());
}

int main() {
  testWyjatkowePalindromy();

  return 0;
}
