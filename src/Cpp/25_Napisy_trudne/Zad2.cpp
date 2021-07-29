#include <cassert>
#include <string>

/*
Dla otrzymanych dwoch napisow, znajdz i usun w pierwszym z nich wystapienia
drugiego.
*/

std::string usunWszystkieV1(std::string zdanie, const std::string &slowo) {
  auto k = zdanie.find(slowo);

  while (k != string::npos) {
    zdanie.erase(k, slowo.length());
    k = zdanie.find(slowo);
  }

  return zdanie;
}

// Testy Poprawnosci
void test1() {
  std::string zdanie = "Lezy jezy na wiezy";
  std::string slowo = "zy";
  std::string wynik = "Le je na wie";

  assert(usunWszystkieV1(zdanie, slowo) == wynik);
}

int main() {

  test1();

  return 0;
}
