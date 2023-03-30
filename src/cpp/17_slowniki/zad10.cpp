/*
Tytul: Anagramy w tekscie
Otrzymujesz tekst w postaci napisu. Twoim zadaniem jest znalezienie wszystkich slow, w ktorych te same znaki wystepuja te sama liczbe razy. Innymi slowy, szukasz anagramow w tekscie. Nalezy zignorowac roznice miedzy malymi i wielkimi literami. Pamietaj, ze slowa skladaja sie wylacznie z liter.
Dane wejsciowe: Napis.
Dane wyjsciowe: Lista list napisow.
Przyklad:
Dla otrzymanego napisu:
"To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. Burza nad galeria i alergia na narty to zadna zbrodnia jak bandzior i jego arbuz.",
powinna zostac zwrocona lista:
[["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]].

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <unordered_map>
#include <vector>

void wyczysc(std::string &napis) {
  /*
   * Usuwa z napisu wszystkie znaki nie bedace literami.
   */
  auto it = napis.begin();

  while (it != napis.end()) {
    if (ispunct(*it))
      napis.erase(it);
    else
      it++;
  }
}

void naMale(std::string &slowo) {
  /*
   * Zamienia wszystkie wielkie litery na male litery.
   */
  transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower);
}

std::vector<std::string> rozdzielSlowa(const std::string &napis) {
  /*
   * Funkcja rozdziela napis na poszczegolne slowa.
   */
  std::vector<std::string> wynik;
  int pocz = 0;
  int konc = 0;
  while ((konc = napis.find(' ', pocz)) != std::string::npos) {
    if (konc != pocz) {
      auto slowo = napis.substr(pocz, konc - pocz);
      wyczysc(slowo);
      naMale(slowo);
      if (!slowo.empty())
        wynik.push_back(slowo);
    }
    pocz = konc + 1;
  }
  if (konc != pocz) {
    auto slowo = napis.substr(pocz);
    wyczysc(slowo);
    naMale(slowo);
    if (!slowo.empty())
      wynik.push_back(slowo);
  }

  return wynik;
}

std::unordered_map<char, int> budujSlownik(const std::string &slowo) {
  /*
   * Funkcja zwraca slownik zawierajacy litery z slowa oraz ich iloscia.
   */
  std::unordered_map<char, int> slownik;

  for (const auto &znak : slowo)
    slownik[znak]++;

  return slownik;
}

std::vector<std::vector<std::string>> znajdzAnagramy(const std::string &tekst) {
  /*
   * Funkcja zwraca wektor wszystkich anagramow w tekscie.
   */

  auto slowa = rozdzielSlowa(tekst);

  std::vector<std::vector<std::string>> wynik;

  auto it = slowa.begin();

  while (it != slowa.end()) {
    auto it2 = it;
    auto slowo = *it;
    auto histogram = budujSlownik(slowo);

    std::vector<std::string> anagramy{slowo};

    it2++;
    while (it2 != slowa.end()) {
      slowo = *it2;

      if (histogram == budujSlownik(slowo)) {
        if (find(anagramy.begin(), anagramy.end(), slowo) == anagramy.end())
          anagramy.push_back(slowo);
        it2 = slowa.erase(it2);
      } else
        it2++;
    }

    if (anagramy.size() > 1)
      wynik.push_back(anagramy);

    it = slowa.erase(it);
  }

  return wynik;
}

void test1() {
  std::string slowo = "To absurd, ze tyran Brudas, ten straszliwy bandzior "
                      "sprawuje rzady w tym kraju. "
                      "Burza nad galeria i alergia na narty to zadna zbrodnia, "
                      "jak bandzior i jego arbuz.";

  std::vector<std::vector<std::string>> wynik{{"absurd", "brudas"},
                                              {"tyran", "narty"},
                                              {"bandzior", "zbrodnia"},
                                              {"burza", "arbuz"},
                                              {"galeria", "alergia"}};

  auto anagramy = znajdzAnagramy(slowo);
  assert(equal(anagramy.begin(), anagramy.end(), wynik.begin()));
}

void test2() {
  std::string slowo = "I love the way sometimes the letters of an anagram "
                      "rearrange themselves in my "
                      "head with no effort, whereas sometimes I have to write "
                      "them out in a circle to work it out.";

  std::vector<std::vector<std::string>> wynik;

  auto anagramy = znajdzAnagramy(slowo);
  assert(equal(anagramy.begin(), anagramy.end(), wynik.begin()));
}

int main() {

  test1();
  test2();

  return 0;
}

