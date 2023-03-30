/*
Tytul: Nazwa pliku bez rozszerzenia.
Tresc: Otrzymujesz napis reprezentujacy sciezke pliku. Odfiltruj z niego nazwe pliku wraz z rozszerzeniem. Zwroc sama nazwe pliku bez rozszerzenia.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu "C:\my-long\path_directory\file.html", powinna zostac zwrocona nazwa pliku bez rozszerzenia "file".

*/

#include <cassert>
#include <regex>
#include <string>

std::string nazwaPliku(std::string &sciezka) {
  const std::regex wzorzec("(.*[\\\\/]+)?([^\\.]*)(.*)?");
  std::smatch wynik;

  if (std::regex_match(sciezka, wynik, wzorzec) && wynik.size() > 1)
    return wynik[2].str();

  return "";
}

void test1() {
  std::string sciezka = "C:\\Windows\\explorer.exe";
  std::string wynik = "explorer";

  assert(nazwaPliku(sciezka) == wynik);
}

void test2() {
  std::string sciezka = "/home/user/var/log/syslog";
  std::string wynik = "syslog";
  assert(nazwaPliku(sciezka) == wynik);
}

void test3() {
  std::string sciezka = "test.jpg.png.mp3.mp5.html.txt";
  std::string wynik = "test";
  assert(nazwaPliku(sciezka) == wynik);
}

void test4() {
  std::string sciezka = "test";
  std::string wynik = "test";
  assert(nazwaPliku(sciezka) == wynik);
}

int main() {

  test1();
  test2();
  test3();
  test4();

  return 0;
}

