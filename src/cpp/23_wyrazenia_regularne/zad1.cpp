/*
Tytul: Sprawdz poprawnosc adresu e-mail.
Tresc: Masz napis reprezentujacy adres e-mail. Sprawdz, czy jest on poprawny.
Pamietaj, ze kazdy adres e-mail sklada sie z identyfikatora uzytkownika, znaku @
oraz nazwy domenowej. Identyfikator uzytkownika sklada sie tylko z:
* Malych (a-z) i wielkich (A-Z) liter.
* Cyfr (0-9).
* Znakow ! # $ % & ' * + — / = ? ^ _ ` { | } ~.
* Kropek . pod warunkiem, ze nie jest pierwszym lub ostatnim znakiem i nie
wystepuje dwukrotnie po sobie. Nazwa domenowa sklada sie tylko z:
* Malych (a-z) i wielkich (A-Z) liter.
* Cyfr (0-9).
* Kropek . oraz myslnika — pod warunkiem, ze nie sa pierwszym lub ostatnim
znakiem i nie wystepuja dwukrotnie po sobie. Dane wejsciowe: Napis. Dane
wyjsciowe: Wartosc logiczna. Przyklad: Dla napisu: “adam@gmail.com”, powinna
zostac zwrocona wartosc logiczna: Prawda.

*/

#include <cassert>
#include <regex>
#include <string>
#include <vector>

bool poprawnyIdentyfikator(std::string &napis) {
  std::regex wzorzec("^[^.][a-zA-Z0-9!#$%&'*+-/"
                     "=?^_`{|}~\\.]*[a-zA-Z0-9!#$%&'*+-/=?^_`{|}~]+[^.]$");
  return regex_match(napis, wzorzec);
}

bool poprawnaNazwaDomenowa(std::string &napis) {
  std::regex wzorzec(
      "[a-zA-Z0-9]+[-a-zA-Z0-9\\.]*\\.[-a-zA-Z0-9\\.]*[a-zA-Z0-9]+");
  return regex_match(napis, wzorzec);
}

bool poprawnyEmail(std::string &napis) {
  if (std::count(napis.begin(), napis.end(), '@') != 1)
    return false;

  // zam
  if (regex_replace(napis, std::regex("\\.(?=\\.)"), "x") != napis)
    return false;

  auto malpa = std::find(napis.begin(), napis.end(), '@') - napis.begin();

  auto identyfikator = napis.substr(0, malpa);
  auto nazwaDomenowa = napis.substr(++malpa, napis.size());

  return poprawnyIdentyfikator(identyfikator) &&
         poprawnaNazwaDomenowa(nazwaDomenowa);
}

void test1() {
  std::vector<std::string> poprawneAdresy{
      "email@example.com",           "firstname.lastname@example.com",
      "email@subdomain.example.com", "firstname+lastname@example.com",
      "email@123.123.123.123",       "1234567890@example.com",
      "email@example-one.com",       "_______@example.com",
      "email@example.name",          "email@example.museum",
      "email@example.co.jp",         "firstname-lastname@example.com"};

  for (auto adresEmail : poprawneAdresy)
    assert(poprawnyEmail(adresEmail));
}

void test2() {

  std::vector<std::string> niepoprawneAdresy{
      "plainaddress",           "#@%^%#$@#$@#.com",
      "@example.com",           "Joe Smith <email@example.com>",
      "email.example.com",      "email@example@example.com",
      ".email@example.com",     "email..email@example.com",
      "あいうえお@example.com", "email@example.com (Joe Smith)",
      "email@example",          "email@-example.com",
      "email@example..com",     "Abc..123@example.com"};

  for (auto adresEmail : niepoprawneAdresy)
    assert(!poprawnyEmail(adresEmail));
}

int main() {

  test1();
  test2();

  return 0;
}

