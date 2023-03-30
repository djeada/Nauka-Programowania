/*
Tytul: Podmien napisy z listy A na napisy z listy B.
Tresc: Dostajesz napis oraz dwie listy napisow. Zastap napisy z pierwszej listy w pierwszym napisie odpowiadajacymi im napisami z drugiej listy.
Dane wejsciowe: Napis oraz dwie listy napisow.
Dane wyjsciowe: Napis.
Przyklad:
Dla podanych danych:
> 'Every mile was tilted at seven or.
Wished her entire esteem mr oh by.
He prevents requests by if in pleased.
Picture too and concerned was comforting.
Ten difficult resembled eagerness nor.
Same park bore on be.
Warmth his law design says he is a person.
Pronunciation suspected in belonging conveying ye repulsive.
oraz ['or', 'be', 'he'] i ['and', 'off', 'she'], powinien zostac zwrocony napis:
> Every mile was tilted at seven and.
Wished her entire esteem mr oh by.
She prevents requests by if in pleased.
Picture too and concerned was comforting.
Ten difficult resembled eagerness nor.
Same park bore on and off.
Warmth his law design says she is a person.
Pronunciation suspected in belonging conveying ye repulsive.

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

