/*
Tytul: Najczesciej wystepujaca litera w zdaniu
Tresc: Otrzymujesz napis reprezentujacy zdanie. Twoim zadaniem jest znalezienie najczesciej wystepujacej litery w zdaniu. Jesli wiecej niz jedna litera wystepuje te sama liczbe razy, nalezy zwrocic litere najwczesniej pojawiajaca sie w zdaniu.
Dane wejsciowe: Napis.
Dane wyjsciowe: Znak.
Przyklad:
Dla otrzymanego napisu: "lezy jerzy na wiezy"
Powinna zostac zwrocona litera: 'e'

*/
#include <cassert>
#include <string>
#include <unordered_map>

std::unordered_map<char, int> budujSlownik(const std::string &slowo) {
  /*
   * Tworzymy slownik, ktory bedzie przechowywal informacje o ilosci wystapien
   * liter w slowie.
   */
  std::unordered_map<char, int> slownik;

  for (const auto &znak : slowo)
    if (tolower(isalpha(znak)))
      slownik[znak]++;

  return slownik;
}

char litera(const std::string &slowo) {
  /*
   * Zwraca najczesciej wystepujaca litere w napisie.
   */
  std::unordered_map<char, int> histogram = budujSlownik(slowo);

  int max = -1;
  char maxLitera = '\0';

  for (auto &litera : slowo) {
    if (histogram[litera] > max) {
      maxLitera = litera;
      max = histogram[litera];
    }
  }

  return maxLitera;
}

void test1() {
  std::string slowo = "lezy jerzy na wiezy";
  char wynik = 'e';

  assert(litera(slowo) == wynik);
}

void test2() {
  std::string slowo = "The most intelligent people disguise the fact that they "
                      "are intelligent. Wise men do not wear name tags., "
                      "The more people talk about their own skills, the more "
                      "desperate they are--their work should speak for itself.";
  char wynik = 'e';

  assert(litera(slowo) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

