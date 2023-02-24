#include <algorithm>
#include <cassert>
#include <set>
#include <string>
#include <vector>

/*
Znajdz wszystkie wyjatkowe palindromy jakie mozna utworzyc ze znakow w slowie
(bez zmiany kolejnosci wystepowania). Nie uwzgledniaj duplikatow w liscie.

Wyjatkowy palindrom musi spelniac jeden z dwoch warunkow:
1. Wszystkie znaki sa identyczne, np. “xxx”.
2. Wszystkie znaki poza srodkowym znakiem sa identyczne, np. “ccdcc”.

Pojedynczy znak jest rowniez uznawany za wyjatkowy palindrom.
*/

std::set<std::string> wyjatkowePalindromy(const std::string slowo) {
  std::set<std::string> wynik;

  for (unsigned int i = 0; i < slowo.size(); i++) {
    wynik.insert(std::string(1, slowo[i]));

    unsigned int j = i + 1;
    unsigned int k = 0;
    while (j < slowo.size() && slowo[i] == slowo[j])
      j++;

    if (j > i + 1)
      wynik.insert(slowo.substr(i, i - j));

    if (j + 1 < slowo.size() && slowo[i] == slowo[j + 1])
      k = j + 1;

    while (k > i && slowo[i] == slowo[k])
      k--;

    if (i + 1 == k)
      wynik.insert(slowo.substr(i, 2 * (j - i) + 1));
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
