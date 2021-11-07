#include <cassert>
#include <string>

/*
Otrzymujesz napis. Przy uzyciu operatorow bitowych:
a) Zamien wielkie litery na male litery.
b) Zamien male litery na wielkie litery.
c) Zamien male litery na wielkie litery i wielkie litery na male litery.
*/

std::string wielkieNaMale(std::string slowo) {
  /*
   * Funkcja zamienia wielkie litery na male litery.
   */
  std::string wynik = "";

  for (const int &litera : slowo)
    wynik += (char)(litera | (int)' ');

  return wynik;
}

std::string maleNaWielkie(std::string slowo) {
  /*
   * Funkcja zamienia male litery na wielkie litery.
   */
  std::string wynik = "";

  for (const int &litera : slowo)
    wynik += (char)(litera & (int)'_');

  return wynik;
}

std::string odwrocWielkoscLiter(std::string slowo) {
  /*
   * Funkcja zamienia male litery na wielkie litery i wielkie litery na male
   * litery.
   */
  std::string wynik = "";

  for (const int &litera : slowo) {

    if (litera >= 'a' and litera <= 'z')
      wynik += (char)(litera ^ (int)' ');

    else if (litera >= 'A' and litera <= 'Z')
      wynik += (char)(litera ^ (int)' ');

    else
      wynik += (char)litera;
  }

  return wynik;
}

void testWielkieNaMale() {
  std::string slowo = "KURCZAKU";
  std::string wynik = "kurczaku";

  assert(wielkieNaMale(slowo) == wynik);
}

void testMaleNaWielkie() {
  std::string slowo = "piesek";
  std::string wynik = "PIESEK";

  assert(maleNaWielkie(slowo) == wynik);
}

void testOdwrocWielkoscLiter() {
  std::string slowo = "wszedl Kotek na PloteK i mrUga";
  std::string wynik = "WSZEDL kOTEK NA pLOTEk I MRuGA";

  assert(odwrocWielkoscLiter(slowo) == wynik);
}

int main() {

  testWielkieNaMale();
  testMaleNaWielkie();
  testOdwrocWielkoscLiter();

  return 0;
}
