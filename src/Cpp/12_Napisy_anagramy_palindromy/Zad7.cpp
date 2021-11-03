#include <algorithm>
#include <cassert>
#include <string>
#include <unordered_map>

/*
Dla dwóch słów, ile minimalnie znaków musimy usunąć aby uzyskać anagramy.
Zwróć -1 dla słów o różnych długościach.
*/

int liczbaZnakow(const std::string &slowoA, const std::string &slowoB) {

    std::vector<int> pom(256, 0);
    
    for (auto znak : slowoA)
        pom[znak - 'a']++;
     
    for (auto znak : slowoB)
        pom[znak - 'a']--;
     
    long wynik = 0;
    
    for(auto liczba : pom)
        wynik +=abs(liczba);

    return wynik;
}

void test1() {
  std::string slowoA = "grazyna";
  std::string slowoB = "razynax";
  int wynik = 2;
  assert(liczbaZnakow(slowoA, slowoB) == wynik);
}

void test2() {
  std::string slowoA = "pan cytryna";
  std::string slowoB = "pan pomarancza";
  int wynik = -1;
  assert(liczbaZnakow(slowoA, slowoB) == wynik);
}

void test3() {
  std::string slowoA = "20ejdy0978oa";
  std::string slowoB = "akv81w39j1ob";
  int wynik = 14;
  assert(liczbaZnakow(slowoA, slowoB) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}
