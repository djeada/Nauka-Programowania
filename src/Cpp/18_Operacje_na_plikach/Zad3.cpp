#include <cassert>
#include <cstdlib>
#include <experimental/filesystem>
#include <iostream>
#include <pwd.h>
#include <string>
#include <sys/types.h>
#include <unistd.h>
#include <vector>

namespace filesys = std::experimental::filesystem;

//Otrzymujesz napis reprezentujący nazwe pliku.
//Przeszukaj caly system i zapisz w liscie wszystkie sciezki plikow o danej nazwie.

std::string katalogDomowy()
{

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
    return std::string(getenv("HOMEDRIVE")) + std::string(getenv("HOMEPATH"));

#else
    const char* homedir;

    if ((homedir = getenv("HOME")) == NULL)
        homedir = getpwuid(getuid())->pw_dir;

    return std::string(homedir);
#endif

    return "";
}

std::vector<std::string> plikiWFolderze(const std::string& sciezkaFolderu, const std::string& szukanyPlik)
{
    std::cout << sciezkaFolderu << std::endl;

    std::vector<std::string> listaSciezek;
    try {
        for (auto& file : filesys::recursive_directory_iterator(sciezkaFolderu)) {
            if (file.path().filename().string() == szukanyPlik)
                listaSciezek.push_back(file.path());
        }
    }

    catch (std::system_error& e) {
        std::cerr << "Exception :: " << e.what();
    }

    return listaSciezek;
}

std::vector<std::string> sciezkiWSystemie(const std::string& szukanyPlik)
{
    return plikiWFolderze(katalogDomowy(), szukanyPlik);
}

int main()
{

    const std::string nazwaPliku = "test.txt";
    for (auto& sciezka : sciezkiWSystemie(nazwaPliku))
        std::cout << sciezka << std::endl;

    return 0;
}
