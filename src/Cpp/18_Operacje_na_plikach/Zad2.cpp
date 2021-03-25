#include <cassert>
#include <experimental/filesystem>
#include <string>
#include <vector>

namespace filesys = std::experimental::filesystem;

//Otrzymujesz dwa napisy. Pierwszy reprezentuje sciezke folderu.
//Drugi rozszerzenie plikow. Znajdz w folderze wszystkie pliki z
//danym rozszerzeniem. Nazwy znalezionych plikow zapisz w liscie.

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
            pliki.push_back(filesys::path(plik.path()).filename());
    }

    return pliki;
}

void test1()
{
    std::string sciezka = "/home/adam/Documents";
    std::string rozszerzenie = ".txt";
    std::vector<std::string> wynik{ "lista.txt", "test.txt" };
    assert(plikiWFolderze(sciezka, rozszerzenie) == wynik);
}

int main()
{

    test1();

    return 0;
}
