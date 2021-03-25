#include <cassert>
#include <vector>

//Otrzymujesz liste liczb. Sprwadz czy srednia elementow
//znajduje się w liscie. Dla sredniej nie bedacej liczba
//calkowita, zaokraglij wynik w dol.

int policzSrednia(std::vector<int>& lista)
{

    int suma = 0;

    for (auto liczba : lista)
        suma += liczba;

    return suma / lista.size();
}

bool czySredniaWLiscie(std::vector<int>& lista)
{

    int srednia = policzSrednia(lista);

    for (auto liczba : lista) {
        if (liczba == srednia)
            return true;
    }

    return false;
}

void test1()
{
    std::vector<int> lista{ 3, 5, -7, 4, 9, -11, 2 };
    assert(!czySredniaWLiscie(lista));
}

void test2()
{
    std::vector<int> lista{ 1, 2, 3 };
    assert(czySredniaWLiscie(lista));
}

int main()
{

    test1();
    test2();

    return 0;
}
