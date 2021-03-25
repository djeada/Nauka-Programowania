#include <iostream>
#include <string>

//Napisz dwie funkcje. Pierwsza powinna porsic uzytkownika o podanie
//nazwy i hasla oraz zwracac otrzymane dane.

void inicjalizacjaDanych(std::string& nazwa, std::string& haslo)
{
    std::cout << "podaj nazwe oraz haslo do zapamietania" << std::endl;
    std::cin >> nazwa >> haslo;
}

//Druga powinna otrzymywac dane od pierwszej i ponownie prosic o
//podanie nazwy oraz hasla, dopoki dane nie beda identyczne z tymi
//podanymi za pierwszym razem.

void czyDanePoprawne(std::string& nazwa, std::string& haslo)
{

    std::string nowaNazwa;
    std::string noweHaslo;

    while (nowaNazwa != nazwa || noweHaslo != haslo) {
        std::cout << "Aby zalogowac sie do systemu: podaj nazwe oraz haslo" << std::endl;
        std::cin >> nowaNazwa >> noweHaslo;
    }

    std::cout << "Logowanie do systemu przebieglo pomyslnie" << std::endl;
}

int main()
{
    std::string nazwa;
    std::string haslo;
    inicjalizacjaDanych(nazwa, haslo);
    czyDanePoprawne(nazwa, haslo);

    return 0;
}
