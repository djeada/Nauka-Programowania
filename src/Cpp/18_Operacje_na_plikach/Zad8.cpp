#include <cstring>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>

namespace filesys = std::experimental::filesystem;

//Otrzymujesz napis reprezentujacy sciezkę folderu.
//Dodaj swoje inicjaly na koncu wszystkich plikow tekstowych znajdujacych
//się w folderze oraz podfolderach.

std::string znajdzRozszerzenie(std::string sciezka)
{

    filesys::path obiekt(sciezka);

    if (obiekt.has_extension())
        return obiekt.extension().string();

    return "";
}

std::vector<std::string> plikiWFolderze(const std::string& sciezka, const std::string& rozszerzenie)
{

    std::vector<std::string> pliki;

    for (const auto plik : filesys::directory_iterator(sciezka)) {
        if (znajdzRozszerzenie(plik.path()) == rozszerzenie)
            pliki.push_back(filesys::path(plik.path()));
    }

    return pliki;
}

void dodajInicjaly(const std::string& sciezkaFolderu, const std::string& dane)
{

    auto _dodajInicjaly = [](const std::string& sciezka, const std::string& dane) {
        std::ofstream plik;
        plik.open(sciezka, std::ios::out | std::ios::app);
        if (plik.fail())
            throw std::ios_base::failure(std::strerror(errno));

        plik.exceptions(plik.exceptions() | std::ios::failbit | std::ifstream::badbit);
        plik << dane << std::endl;
        std::cout << dane << std::endl;
    };

    auto sciezki = plikiWFolderze(sciezkaFolderu, ".txt");

    for (const auto& sciezka : sciezki)
        _dodajInicjaly(sciezka, dane);
}

//Usun srodkowy wiersz z kazdego pliku csv znajdujacego się w folderze
//oraz podfolderach.
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

void usunSrodkowy(const std::string& sciezkaFolderu)
{

    auto _usunSrodkowy = [](const std::string& sciezka) {
        auto trescPliku = wczytajPlik(sciezka);

        try {
            std::string wiersz;
            std::ofstream plik(sciezka);
            plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit | std::ifstream::badbit);

            trescPliku.erase(trescPliku.begin() + trescPliku.size() / 2);

            for (auto& wiersz : trescPliku)
                plik << wiersz + "\n";

            plik.close();
        }

        catch (std::exception const& e) {
            std::cout << "Error: " << e.what() << std::endl;
        }
    };

    auto sciezki = plikiWFolderze(sciezkaFolderu, ".csv");

    for (const auto& sciezka : sciezki)
        _usunSrodkowy(sciezka);
}

int main()
{

    std::string sciezka = std::string(filesys::current_path()) + filesys::path::preferred_separator + "folder/";
    std::string dane = "A.D.";
    dodajInicjaly(sciezka, dane);
    usunSrodkowy(sciezka);

    return 0;
}
