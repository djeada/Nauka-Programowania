#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>

namespace filesys = std::experimental::filesystem;

//Otrzymujesz dwa napisy reprezentujace sciezki folderow.
//Przenies wszystkie pliki .csv z pierwszego folderu (oraz jego podfolderow) do drugiego folderu.

std::string nazwaPliku(const std::string& sciezka)
{
    return filesys::path(sciezka).filename();
}

void przeniesPlik(const std::string& sciezka, const std::string& sciezkaDocelowa)
{

    try {
        filesys::copy_file(sciezka, sciezkaDocelowa + filesys::path::preferred_separator + nazwaPliku(sciezka),
            filesys::copy_options::overwrite_existing);
        filesys::remove(sciezka);
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

void przeniesPliki(const std::string& sciezka, const std::string& sciezkaDocelowa)
{

    for (const auto plik : filesys::directory_iterator(sciezka)) {
        if (znajdzRozszerzenie(plik.path()) == ".csv")
            przeniesPlik(plik.path(), sciezkaDocelowa);
    }
}

int main()
{

    const std::string sciezkaA = "folder/";
    const std::string sciezkaB = "folder2/";
    przeniesPliki(sciezkaA, sciezkaB);

    return 0;
}
