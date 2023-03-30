/*
Tytul: Skopiuj pliki.
Tresc zadania: Otrzymujesz dwa napisy reprezentujace sciezki do folderow. Skopiuj wszystkie pliki PNG z pierwszego folderu do drugiego folderu.
Dane wejsciowe: Dwa napisy reprezentujace sciezki do folderow.
Dane wyjsciowe: Brak.

*/
#include <cassert>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <string>

namespace filesys = std::experimental::filesystem;

std::string nazwaPliku(const std::string &sciezka) {
  return filesys::path(sciezka).filename();
}

void skopiujPlik(const std::string &sciezka,
                 const std::string &sciezkaDocelowa) {
  try {
    filesys::copy_file(sciezka,
                       sciezkaDocelowa + filesys::path::preferred_separator +
                           nazwaPliku(sciezka),
                       filesys::copy_options::overwrite_existing);
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

void skopiujPliki(const std::string &sciezka,
                  const std::string &sciezkaDocelowa) {

  for (const auto plik : filesys::directory_iterator(sciezka)) {
    if (znajdzRozszerzenie(plik.path()) == ".png")
      skopiujPlik(plik.path(), sciezkaDocelowa);
  }
}

void testSkopiujPliki() {

  // stworz foldery test1 i folder test2
  std::string sciezka1 = "test1";
  std::string sciezka2 = "test2";
  filesys::create_directory(sciezka1);
  filesys::create_directory(sciezka2);

  // stworz pliki test1/plik1.png i test1/plik2.png
  std::string sciezkaPliku1 =
      sciezka1 + filesys::path::preferred_separator + "plik1.png";
  std::string sciezkaPliku2 =
      sciezka1 + filesys::path::preferred_separator + "plik2.png";
  std::ofstream plik1(sciezkaPliku1);
  std::ofstream plik2(sciezkaPliku2);
  plik1.close();
  plik2.close();

  // skopiuj pliki z test1 do test2
  skopiujPliki(sciezka1, sciezka2);

  // sprawdz czy pliki zostaly skopiowane
  assert(filesys::exists(sciezka2 + filesys::path::preferred_separator +
                         "plik1.png"));
  assert(filesys::exists(sciezka2 + filesys::path::preferred_separator +
                         "plik2.png"));

  // usun foldery test1 i test2
  filesys::remove_all(sciezka1);
  filesys::remove_all(sciezka2);
}

int main() {

  testSkopiujPliki();

  return 0;
}

