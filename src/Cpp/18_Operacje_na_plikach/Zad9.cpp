#include <experimental/filesystem>
#include <string>

namespace filesys = std::experimental::filesystem;

//Otrzymujesz napis reprezentujacy sciezke folderu.
//Usun wszystkie pliki o rozmiarach wiekszych niż 10kB
//znajdujacych sie w folderze oraz podfolderach.

int rozmiarPliku(const std::string& sciezka)
{
    return filesys::file_size(filesys::path(sciezka));
}

void usunPliki(const std::string& sciezka)
{

    for (const auto plik : filesys::directory_iterator(sciezka)) {
        if (rozmiarPliku(plik.path()) > 10000)
            filesys::remove(filesys::path(plik.path()));
    }
}

int main()
{

    const std::string sciezka = "folder/";
    usunPliki(sciezka);

    return 0;
}
