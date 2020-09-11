/*
Wypisz nazwy plikow znajdujacych sie w folderze.
*/

#include <iostream>
#include <cassert>
#include <experimental/filesystem>

using namespace std;
namespace filesys = std::experimental::filesystem;

vector<string> plikiWFolderze(const string& sciezka) {
    
	vector<string> pliki;
	
	for (const auto plik: filesys::directory_iterator(sciezka))
		pliki.push_back(plik.path());
    
    return pliki;
}

int main() {
    string sciezka = "/home/adam/Documents";
    vector<string> wynik = plikiWFolderze(sciezka);

    return 0;
}

