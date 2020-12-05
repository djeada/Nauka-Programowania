/*
Znajdz i zamien wszystkie wystapienia slowa w zdaniu na inne podane slowo.
*/

#include <iostream>
#include <cassert>
#include <experimental/filesystem>

namespace filesys = std::experimental::filesystem;

bool czyPlik(std::string sciezka) {
    try {
        filesys::path pathObj(sciezka);
        if (filesys::exists(pathObj) && filesys::is_regular_file(pathObj))
            return true;
    }
    
    catch (filesys::filesystem_error& e) {
       std::cerr << e.what() << std::endl;
    }
    
    return false;
}

bool czyFolder(std::string sciezka) {
    try {
        filesys::path pathObj(sciezka);
        if (filesys::exists(pathObj) && filesys::is_directory(pathObj))
            return true;
    }
    
    catch (filesys::filesystem_error& e) {
        std::cerr << e.what() << std::endl;
    }
    
    return false;
}

int main() {
    std::string sciezkaPliku = "/home/Nauka-programowania/src/Cpp/20.Operacje_na_plikach/Zad1.cpp";
    std::string sciezkaFolderu = "/home/adam/Documents/Programming";
   	
   	assert(czyPlik(sciezkaPliku));
    assert(!czyFolder(sciezkaPliku));
    
   	assert(!czyPlik(sciezkaFolderu));
    assert(czyFolder(sciezkaFolderu));
   
    return 0;
}

