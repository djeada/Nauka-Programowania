#include <cassert>
#include <experimental/filesystem>
#include <iostream>

namespace filesys = std::experimental::filesystem;

//Otrzymujesz napis reprentujcy sciezke.
//Sprawdz, czy sciezka należy do pliku czy folderu.

bool czyPlik(std::string sciezka)
{
    try {
        filesys::path obiekt(sciezka);
        if (filesys::exists(obiekt) && filesys::is_regular_file(obiekt))
            return true;
    }

    catch (filesys::filesystem_error& e) {
        std::cerr << e.what() << std::endl;
    }

    return false;
}

bool czyFolder(std::string sciezka)
{
    try {
        filesys::path obiekt(sciezka);
        if (filesys::exists(obiekt) && filesys::is_directory(obiekt))
            return true;
    }

    catch (filesys::filesystem_error& e) {
        std::cerr << e.what() << std::endl;
    }

    return false;
}

void test1()
{
    std::string sciezkaPliku = "/home/Nauka-programowania/Zad1.cpp";
    assert(czyPlik(sciezkaPliku));
    assert(!czyFolder(sciezkaPliku));
}

void test2()
{
    std::string sciezkaFolderu = "/home/adam/Documents/Programming";

    assert(!czyPlik(sciezkaFolderu));
    assert(czyFolder(sciezkaFolderu));
}

int main()
{

    test1();
    test2();

    return 0;
}

//Compiling with g++ -std=c++17 Zad1.cpp -lstdc++fs -o exe
