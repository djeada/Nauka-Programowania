/*
Tytul: Wczytaj i wypisz tresc pliku.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego.
Wczytaj plik i wypisz jego tresc. Dane wejsciowe: Napis reprezentujacy sciezke
do pliku. Dane wyjsciowe: Napis zawierajacy tresc pliku.

*/
#include <cassert>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>

namespace filesys = std::experimental::filesystem;

std::string nazwaPliku(const std::string &sciezka) {
  return filesys::path(sciezka).filename();
}

void przeniesPlik(const std::string &sciezka,
                  const std::string &sciezkaDocelowa) {

  try {
    filesys::copy_file(sciezka,
                       sciezkaDocelowa + filesys::path::preferred_separator +
                           nazwaPliku(sciezka),
                       filesys::copy_options::overwrite_existing);
    filesys::remove(sciezka);
  } catch (filesys::filesystem_error &e) {
    std::cout << e.what() << std::endl;
  }
}

std::string znajdzRozszerzenie(std::string sciezka) {

  filesys::path obiekt(sciezka);

  if (obiekt.has_extension())
    return obiekt.extension().string();

  return "";
}

void przeniesPliki(const std::string &sciezka,
                   const std::string &sciezkaDocelowa) {

  for (const auto plik : filesys::directory_iterator(sciezka)) {
    if (znajdzRozszerzenie(plik.path()) == ".csv")
      przeniesPlik(plik.path(), sciezkaDocelowa);
  }
}

void testPrzeniesPliki() {

  // stworz foldery test1 i test2
  filesys::create_directory("test1");
  filesys::create_directory("test2");

  // stworz pliki test1/plik1.csv i test1/plik2.csv

  std::string sciezka1 = "test1/plik1.csv";
  std::string sciezka2 = "test1/plik2.csv";

  std::ofstream plik1(sciezka1);
  plik1 << "test1; test2" << std::endl;
  plik1.close();

  std::ofstream plik2(sciezka2);
  plik2 << "test3; test4" << std::endl;
  plik2.close();

  // przenies pliki z test1 do test2
  przeniesPliki("test1", "test2");

  // sprawdz czy pliki zostaly przeniesione
  assert(filesys::exists("test2/plik1.csv"));
  assert(filesys::exists("test2/plik2.csv"));
  assert(!filesys::exists("test1/plik1.csv"));
  assert(!filesys::exists("test1/plik2.csv"));

  // usun foldery test1 i test2
  filesys::remove_all("test1");
  filesys::remove_all("test2");
}

int main() {

  testPrzeniesPliki();

  return 0;
}

