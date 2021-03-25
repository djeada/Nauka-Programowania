#include <cassert>
#include <string>
#include <vector>

//Otrzymujesz liste liczb, kierunek przesuniec (1 odpowiada przesunieciu
//w prawo, a 0 w lewo) oraz liczbę miejsc o jaka maja zostac przesuniete
//elementy. Przykladowo dla przesuwania w prawo pierwszy element trafia
//na miejsce drugiego, drugi trzeciego, a ostatni na miejsce pierwszego.
//Przesun elementy listy w danym kierunku.

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(n)
void rotacjaV1(std::vector<int>& lista, const std::string& kierunek, int liczba)
{

    if (kierunek == "prawo") {
        for (int i = 0; i < liczba; i++) {
            lista.insert(lista.begin(), lista.back());
            lista.erase(std::prev(lista.end()));
        }
    }

    else {
        for (int i = 0; i < liczba; i++) {
            lista.push_back(lista.front());
            lista.erase(lista.begin());
        }
    }
}

void test1()
{

    std::vector<int> lista{ 5, 27, 6, 2, 1, 10, 8 };
    std::vector<int> wynik{ 6, 2, 1, 10, 8, 5, 27 };
    std::string kierunek = "lewo";
    int liczba = 2;

    rotacjaV1(lista, kierunek, liczba);
    assert(lista == wynik);
}

void test2()
{

    std::vector<int> lista{ 9, 9, 42, 47, 5, 6, 19, 7 };
    std::vector<int> wynik{ 6, 19, 7, 9, 9, 42, 47, 5 };
    std::string kierunek = "prawo";
    int liczba = 3;

    rotacjaV1(lista, kierunek, liczba);
    assert(lista == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
