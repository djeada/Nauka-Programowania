/*
Tytul: Podmien napisy z listy A na napisy z listy B.
Tresc: Dostajesz napis oraz dwie listy napisow. Zastap napisy z pierwszej listy
w pierwszym napisie odpowiadajacymi im napisami z drugiej listy. Dane wejsciowe:
Napis oraz dwie listy napisow. Dane wyjsciowe: Napis. Przyklad: Dla podanych
danych: > 'Every mile was tilted at seven or. Wished her entire esteem mr oh by.
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
#include <sstream>
#include <string>
#include <vector>

std::vector<std::string> cyfry(const std::string &napis) {
  std::string slowo;
  std::stringstream ss(napis);

  std::vector<std::string> wynik;

  while (ss >> slowo) {
    if (std::regex_search(slowo, std::regex("[0-9]+")) &&
        std::regex_search(slowo, std::regex("[^0-9]+")))
      wynik.push_back(std::regex_replace(slowo, std::regex("[^0-9]*"), ""));
  }

  return wynik;
}

void test1() {
  std::string napis = "jerzy29 i an37a s3uc8ali91 lekcji 22 2 jezyka polki3go";
  std::vector<std::string> wynik{"29", "37", "3891", "3"};

  assert(cyfry(napis) == wynik);
}

int main() {

  test1();

  return 0;
}

