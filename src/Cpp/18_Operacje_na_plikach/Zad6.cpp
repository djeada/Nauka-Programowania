#include <algorithm>
#include <cassert>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <unordered_map>

namespace filesys = std::experimental::filesystem;

/*
Otrzymujesz napis reprezentujacy sciezke pliku tekstowego. Oblicz:
a) Liczbe wierszy pliku.
b) Liczbe slow w pliku. Slowa oddzielone sa spacjami i nie moga
skladac sie wylacznie ze znakow nie bedacych literami.
c) Srednia dlugosc wiersza.
d) Srednia liczbe slow na wiersz.
e) Czestosc wystepowania kazdego ze slow w pliku.
*/

void wyczysc(std::string &napis) {
  auto it = napis.begin();

  while (it != napis.end()) {
    if (ispunct(*it))
      napis.erase(it);
    else
      it++;
  }
}

void naMale(std::string &slowo) {
  transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower);
}

std::vector<std::string> rozdzielSlowa(std::string &napis) {
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

std::vector<std::string> wczytajPlik(const std::string &sciezka) {

  std::vector<std::string> tresc;
  try {
    std::string wiersz;
    std::ifstream plik(sciezka);
    plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit |
                    std::ifstream::badbit);

    while (plik) {
      getline(plik, wiersz);
      tresc.push_back(wiersz);
    }

    plik.close();
  }

  catch (std::exception const &e) {
    std::cout << "Error : " << e.what() << std::endl;
  }

  return tresc;
}

int liczbaWierszy(std::vector<std::string> &trescPliku) {
  return trescPliku.size();
}

int liczbaSlow(std::vector<std::string> &trescPliku) {
  int wynik = 0;

  for (std::string &wiersz : trescPliku)
    wynik += rozdzielSlowa(wiersz).size();

  return wynik;
}

double sredniaDlugoscWiersza(std::vector<std::string> &trescPliku) {

  int calkDlugosc = 0;

  for (const std::string &wiersz : trescPliku)
    calkDlugosc += wiersz.size();

  return calkDlugosc / (double)trescPliku.size();
}

double sredniaLiczbaSlow(std::vector<std::string> &trescPliku) {
  return liczbaSlow(trescPliku) / (double)liczbaWierszy(trescPliku);
}

std::string wektorNaString(std::vector<std::string> &wektor) {
  std::string s;
  for (const auto &piece : wektor)
    s += piece;
  return s;
}

std::unordered_map<std::string, int> histogramSlow(std::string &trescPliku) {
  std::unordered_map<std::string, int> slownik;

  std::vector<std::string> slowa = rozdzielSlowa(trescPliku);

  for (const auto &slowo : slowa)
    slownik[slowo]++;

  return slownik;
}

void test1() {
  filesys::path sciezka{"temp.txt"};

  std::ofstream ofs(sciezka);
  ofs << "Hej \n";
  ofs << "This is an example of a simple ASCII text file stored on a Web "
         "server. Note that it has a file\n";
  ofs << "extension of \".txt\".\n\n";
  ofs << "Although such files may contains some basic layout formatting, such "
         "as paragraphs, there is no\n";
  ofs << "support for the text to have attributes, such as bolding.\n\n";
  ofs << "Text files can contain Hypertext Mark-up codes but these will not be "
         "interpreted by the \n";
  ofs << "browser. For example, if the following characters "
         "<strong>hello</strong> were typed into an\n";
  ofs << "\"html\" file then the word \"hello\" would be shown in bold.\n";
  ofs.close();

  auto trescPliku = wczytajPlik(sciezka);
  auto tekst = wektorNaString(trescPliku);

  int _liczbaWierszy = 10;
  assert(liczbaWierszy(trescPliku) == _liczbaWierszy);

  int _liczbaSlow = 88;
  assert(liczbaSlow(trescPliku) == _liczbaSlow);

  double _sredniaDlugoscWiersza = 50.6;
  assert(abs(sredniaDlugoscWiersza(trescPliku) - _sredniaDlugoscWiersza) <
         0.01);

  double _sredniaLiczbaSlow = 8.8;
  assert(abs(sredniaLiczbaSlow(trescPliku) - _sredniaLiczbaSlow) < 0.01);

  std::unordered_map<std::string, int> _histogramSlow = {
      {"bold", 1},        {"in", 1},
      {"shown", 1},       {"word", 1},
      {"then", 1},        {"anhtml", 1},
      {"simple", 1},      {"basic", 1},
      {"contains", 1},    {"layout", 1},
      {"were", 1},        {"may", 1},
      {"such", 3},        {"fileextension", 1},
      {"files", 2},       {"it", 1},
      {"hypertext", 1},   {"hello", 1},
      {"note", 1},        {"file", 2},
      {"web", 1},         {"ascii", 1},
      {"is", 2},          {"an", 1},
      {"example", 2},     {"hej", 1},
      {"following", 1},   {"this", 1},
      {"of", 2},          {"txtalthough", 1},
      {"text", 2},        {"stored", 1},
      {"that", 1},        {"by", 1},
      {"on", 1},          {"formatting", 1},
      {"nosupport", 1},   {"browser", 1},
      {"typed", 1},       {"a", 3},
      {"server", 1},      {"would", 1},
      {"contain", 1},     {"as", 2},
      {"markup", 1},      {"characters", 1},
      {"there", 1},       {"for", 2},
      {"the", 4},         {"to", 1},
      {"have", 1},        {"these", 1},
      {"will", 1},        {"paragraphs", 1},
      {"attributes", 1},  {"boldingtext", 1},
      {"can", 1},         {"has", 1},
      {"codes", 1},       {"if", 1},
      {"some", 1},        {"but", 1},
      {"not", 1},         {"be", 2},
      {"interpreted", 1}, {"stronghellostrong", 1},
      {"into", 1}};

  auto trescPlikuJakoString = wektorNaString(trescPliku);
  auto wynik = histogramSlow(trescPlikuJakoString);
  assert(histogramSlow(trescPlikuJakoString) == _histogramSlow);

  filesys::remove(sciezka);
}

int main() {

  test1();

  return 0;
}
