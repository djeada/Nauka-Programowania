#include <algorithm>
#include <cassert>
#include <vector>

//Dla otrzymanej listy znajdz indeks najmniejszego elementu.
//Lista jest posortowana rosnaco, ale zostala przesunieta.
//Przykladowo przez przesuniecie w prawo o 1 rozumiemy, ze
//ostatni element trafi na miejsce pierwszego, pierwszy drugiego, itd.

int indeksMin(std::vector<int>& lista)
{
    int n = lista.size();

    for (int i = 0; i < n - 1; i++) {
        if (lista[i] > lista[i + 1])
            return i + 1;
    }

    return 0;
}

void test1()
{
    std::vector<int> lista{ 7, 8, -1, 4, 5 };
    int wynik = 2;
    assert(indeksMin(lista) == wynik);
}

void test2()
{
    std::vector<int> lista{ 2, 3, 4, 5, 6 };
    int wynik = 0;
    assert(indeksMin(lista) == wynik);
}

void test3()
{
    std::vector<int> lista{ 8, 9, 10, 11, 1 };
    int wynik = 4;
    assert(indeksMin(lista) == wynik);
}

int main()
{

    test1();
    test2();
    test3();

    return 0;
}
