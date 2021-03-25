#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <unordered_map>
#include <vector>

//Otrzymujesz napis reprezentujacy scieżke pliku tekstowego. Oblicz:
void wyczysc(std::string& napis)
{
    auto it = napis.begin();

    while (it != napis.end()) {
        if (ispunct(*it))
            napis.erase(it);
        else
            it++;
    }
}

void naMale(std::string& slowo)
{
    transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower);
}

std::vector<std::string> rozdzielSlowa(std::string& napis)
{
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

std::vector<std::string> wczytajPlik(const std::string& sciezka)
{

    std::vector<std::string> tresc;
    try {
        std::string wiersz;
        std::ifstream plik(sciezka);
        plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit | std::ifstream::badbit);

        while (plik) {
            getline(plik, wiersz);
            tresc.push_back(wiersz);
        }

        plik.close();
    }

    catch (std::exception const& e) {
        std::cout << "Error : " << e.what() << std::endl;
    }

    return tresc;
}

//Liczbe wierszy pliku.
int liczbaWierszy(std::vector<std::string>& trescPliku)
{
    return trescPliku.size();
}

//Liczbe slow w pliku. Slowa oddzielone sa spacjami i nie moga skladac
//sie wylacznie ze znakow nie bedacych literami.
int liczbaSlow(std::vector<std::string>& trescPliku)
{
    int wynik = 0;

    for (std::string& wiersz : trescPliku)
        wynik += rozdzielSlowa(wiersz).size();

    return wynik;
}

//srednia dlugosc wiersza.
double sredniaDlugoscWiersza(std::vector<std::string>& trescPliku)
{

    int calkDlugosc = 0;

    for (const std::string& wiersz : trescPliku)
        calkDlugosc += wiersz.size();

    return calkDlugosc / (double)trescPliku.size();
}

//srednia liczbe slow na wiersz.
double sredniaLiczbaSlow(std::vector<std::string>& trescPliku)
{
    return liczbaSlow(trescPliku) / (double)liczbaWierszy(trescPliku);
}

//Czestosc wystepowania każdego ze slow w pliku.
std::string wektorNaString(std::vector<std::string>& wektor)
{
    std::string s;
    for (const auto& piece : wektor)
        s += piece;
    return s;
}

std::unordered_map<std::string, int> histogramSlow(std::string& trescPliku)
{
    std::unordered_map<std::string, int> slownik;

    std::vector<std::string> slowa = rozdzielSlowa(trescPliku);

    for (const auto& slowo : slowa)
        slownik[slowo]++;

    return slownik;
}

int main()
{

    std::string sciezka = "folder/test.txt";
    auto trescPliku = wczytajPlik(sciezka);

    std::cout << "Liczba wierszy: " << liczbaWierszy(trescPliku) << std::endl;
    std::cout << "Liczba slow: " << liczbaSlow(trescPliku) << std::endl;
    std::cout << "Srednia dlugosc wiersza: " << sredniaDlugoscWiersza(trescPliku) << std::endl;
    std::cout << "Srednia liczba slow na wiersz: " << sredniaLiczbaSlow(trescPliku) << std::endl;
    std::cout << "Histogram slow: " << std::endl;

    auto tekst = wektorNaString(trescPliku);

    for (auto it : histogramSlow(tekst))
        std::cout << it.first << " : " << it.second << std::endl;

    return 0;
}
