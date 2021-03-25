#include <cassert>
#include <vector>

//Otrzymujesz liste oraz klucz. Znajdz indeks odpowiadajacy pierwszemu
//wystapieniu klucza w liscie. Jesli klucz nie wysteþuje w liscie, zwroc -1.
int znajdzKluczV1(std::vector<int>& lista, int klucz)
{

    for (unsigned int i = 0; i < lista.size(); i++) {
        if (lista[i] == klucz)
            return i;
    }

    return -1;
}

void test1()
{
    std::vector<int> lista{ 3, 5, -7, 4, 9, -11, 2 };
    int klucz = 2;
    int wynik = 6;

    assert(znajdzKluczV1(lista, klucz) == wynik);
}

void test2()
{
    std::vector<int> lista{ 3, -2, 4, 9, -3, -40, 8, 5, -7, -1 };
    int klucz = 2;
    int wynik = -1;

    assert(znajdzKluczV1(lista, klucz) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
