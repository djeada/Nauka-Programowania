#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>

namespace filesys = std::experimental::filesystem;

//Otrzymujesz dwa napisy. Pierwszy reprezentuje sciezke pliku tekstowego.
//Drugi wiersz tekstu. Dodaj wiersz na poczatku pliku.

void skopiujPlik(const std::string& sciezka, const std::string& sciezkaDocelowa)
{

    try {
        filesys::copy_file(sciezka, sciezkaDocelowa, filesys::copy_options::overwrite_existing);
    } catch (filesys::filesystem_error& e) {
        std::cout << e.what() << std::endl;
    }
}

void zamienPliki(const std::string& sciezkaA, const std::string& sciezkaB)
{

    std::string tempSciezka(sciezkaB);

    while (filesys::exists(tempSciezka))
        tempSciezka = std::string(filesys::path(tempSciezka).parent_path()) + filesys::path::preferred_separator
            + "x" + std::string(filesys::path(tempSciezka).filename());

    skopiujPlik(sciezkaA, tempSciezka);
    skopiujPlik(sciezkaB, sciezkaA);
    skopiujPlik(tempSciezka, sciezkaB);
    filesys::remove(tempSciezka);
}

int main()
{

    const std::string sciezkaA = "folder/test.txt";
    const std::string sciezkaB = "folder2/test2.txt";
    zamienPliki(sciezkaA, sciezkaB);

    return 0;
}
