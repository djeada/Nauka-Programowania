/*
Tytul: Sprawdz poprawnosc hasla.
Tresc: Masz napis reprezentujacy haslo. Sprawdz, czy haslo spelnia nastepujace
warunki:
1. Haslo musi zawierac przynajmniej jedna mala litere [a-z].
2. Haslo musi zawierac przynajmniej jedna duza litere [A-Z].
3. Haslo musi zawierac przynajmniej jedna cyfre [0-9].
4. Haslo musi zawierac przynajmniej jeden znak specjalny [! # $ % & ' * + — / =
? ^ _ ` { | } ~].
5. Minimalna dlugosc hasla to 8 znakow.
6. Maksymalna dlugosc hasla to 20 znakow.
Dane wejsciowe: Napis.
Dane wyjsciowe: Wartosc logiczna.
Przyklad:
Dla napisu: “abc1234”, powinna zostac zwrocona wartosc logiczna: Falsz.

*/

#include <cassert>
#include <regex>
#include <string>
#include <vector>

void podmien(std::string &napis, std::vector<std::string> &listaA,
             std::vector<std::string> &listaB) {
  if (listaA.size() != listaB.size())
    return;

  auto itA = listaA.begin();
  auto itB = listaB.begin();

  while (itA != listaA.end() || itB != listaB.end()) {
    napis = std::regex_replace(napis, std::regex("\\b" + *itA + "\\b"), *itB);
    ++itA;
    ++itB;
  }
}

void test1() {
  std::string napis =
      "Every mile was tilted at seven or. Wished her entire esteem mr oh by. "
      "He prevents requests by if in pleased. Picture too and concerned was "
      "comforting. Ten difficult resembled eagerness nor. Same park bore on "
      "be. Warmth his law design says he is a person. Pronunciation suspected "
      "in belonging conveying ye repulsive.";

  std::vector<std::string> listaA{"or", "be", "he"};
  std::vector<std::string> listaB{"and", "off", "she"};

  std::string wynik =
      "Every mile was tilted at seven and. Wished her entire esteem mr oh by. "
      "He prevents requests by if in pleased. Picture too and concerned was "
      "comforting. Ten difficult resembled eagerness nor. Same park bore on "
      "off. Warmth his law design says she is a person. Pronunciation "
      "suspected in belonging conveying ye repulsive.";

  podmien(napis, listaA, listaB);

  assert(napis == wynik);
}

int main() {

  test1();

  return 0;
}

