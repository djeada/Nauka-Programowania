#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

/*
Przesun zera na koniec listy.
*/

void swap(vector<int>& lista, int i, int j)
{
    int temp = lista[j];
    lista[j] = lista[i];
    lista[i] = temp;
}

void zeraV1(vector<int>& lista)
{

    int N = lista.size();

    for (int i = 0; i < N; i++) {
        if (lista[i] == 0) {
            int j = i + 1;

            while (lista[j] == 0 && j < N)
                j++;

            swap(lista, i, j);
        }
    }
}

//Testy Poprawnosci
void test1()
{
    vector<int> lista{ 0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0 };
    vector<int> wynik{ 1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0 };

    zeraV1(lista);
    assert(lista == wynik);
}

int main()
{

    test1();

    return 0;
}
