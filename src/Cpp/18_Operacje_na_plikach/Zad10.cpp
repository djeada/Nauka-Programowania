#include <experimental/filesystem>
#include <iostream>
#include <string>

namespace filesys = std::experimental::filesystem;

//Otrzymujesz dwa napisy reprezentujace sciezki folderow.
//Skopiuj wszystkie pliki .png z pierwszego folderu do drugiego.

std::string nazwaPliku(const std::string& sciezka)
{
    return filesys::path(sciezka).filename();
}

void skopiujPlik(const std::string& sciezka, const std::string& sciezkaDocelowa)
{
    try {
        filesys::copy_file(sciezka, sciezkaDocelowa + filesys::path::preferred_separator + nazwaPliku(sciezka),
            filesys::copy_options::overwrite_existing);
    } catch (filesys::filesystem_error& e) {
        std::cout << e.what() << std::endl;
    }
}

std::string znajdzRozszerzenie(std::string sciezka)
{

    filesys::path obiekt(sciezka);

    if (obiekt.has_extension())
        return obiekt.extension().string();

    return "";
}

void skopiujPliki(const std::string& sciezka, const std::string& sciezkaDocelowa)
{

    for (const auto plik : filesys::directory_iterator(sciezka)) {
        if (znajdzRozszerzenie(plik.path()) == ".png")
            skopiujPlik(plik.path(), sciezkaDocelowa);
    }
}

int main()
{

    const std::string sciezka = "folder/";
    const std::string sciezkaDocelowa = "folder2/";
    skopiujPliki(sciezka, sciezkaDocelowa);

    return 0;
}
