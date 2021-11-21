/*
Otrzymujesz napis reprezentujacy haslo. Sprawdz czy 
haslo spelnia nastepujace warunki:
1. Haslo musi zawierac przynajmniej jedna mala litere [a-z].
2. Haslo musi zawierac przynajmniej jedna duza litere [A-Z].
3. Haslo musi zawierac przynajmniej jedna cyfre [0-9].
4. Haslo musi zawierac przynajmniej jeden znak specjalny 
[! # $ % & ' * + - / = ? ^ _ ` { | } ~].
5. Minimalna dlugosc hasla to 8 znakow.
6. Maksymalna dlugosc hasla to 20 znakow.
*/

#include <cassert>
#include <regex>
#include <string>
#include <vector>


bool poprawneHaslo(std::string &haslo) {
  if (regex_search(haslo, std::regex("[a-z]")) &&
      regex_search(haslo, std::regex("[A-Z]"))) {
    if (regex_search(haslo, std::regex("[0-9]")) &&
        regex_search(haslo, std::regex("[!#$%&'*+-/=?^_`{|}~]")))
      return haslo.size() >= 8 && haslo.size() <= 20;
  }

  return false;
}

void test1() {
  std::vector<std::string> poprawneHasla{
      "HulaKula123!",  "$$KAsiORA302$$",      "X'nQz{sH:6k4*3+T",
      "=3Xv+D]?''(_",  "Mt`VXsD^47+'H-",      "]t'N\"mtH'W9p<_<Vc)=",
      "b5TMq2L:'{f&",  "_t}s%Ymu2YP>w",       "'zGFbJg)~6;}",
      "\"Tuqb}h7)2Gv", "Ng2+]zLR7)nX7UXM]`T", ",{QPW7H+7za?95K&:wP"};

  for (auto haslo : poprawneHasla)
    assert(poprawneHaslo(haslo));
}

void test2() {
  std::vector<std::string> niepoprawneHasla{
      "123456",   "proste_haslo123", "haslo", "pizza&*!",
      "!!!!!!!!", "_____123_____",   "...",   "abcd32",
      "AB***DB",  "22tajnE",         "Ab6*"};

  for (auto haslo : niepoprawneHasla)
    assert(!poprawneHaslo(haslo));
}

int main() {

  test1();
  test2();

  return 0;
}
