#include <cassert>
#include <cmath>
#include <numeric>
#include <vector>

//Otrzymujesz liste liczb, wykonaj nastepujace polecenia:

//a)Zwieksz o 1 wszystkie elementy stojace na parzystych indeksach.
void zwieksz(std::vector<int>& lista)
{

    for (unsigned int i = 0; i < lista.size(); i++) {
        if (i % 2 == 0)
            lista[i]++;
    }
}

//b)Wyzeruj wszystkie wielokrotnosci liczby 3.
void wyzeruj(std::vector<int>& lista)
{

    for (auto& liczba : lista) {
        if (liczba % 3 == 0)
            liczba = 0;
    }
}

//c)Podnies do kwadratu wszystkie elementy mniejsze niz 10.
void kwadrat(std::vector<int>& lista)
{

    for (auto& liczba : lista) {
        if (liczba < 10)
            liczba = pow(liczba, 2);
    }
}

//d)Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace liczbami pierwszymi.
int czyPierwsza(int n)
{

    if ((!(n % 2) && n != 2) || n < 1)
        return false;

    for (int i = 3; i <= std::sqrt((double)n); i += 2) {
        if (!(n % i))
            return false;
    }

    return true;
}

void suma(std::vector<int>& lista)
{
    int suma = accumulate(lista.begin(), lista.end(), 0);

    for (unsigned int i = 0; i < lista.size(); i++) {
        if (czyPierwsza(i))
            lista[i] = suma;
    }
}

//e)Zamien kazdy element na iloczyn wszystkich elementow list poza nim samym.

void zamien(std::vector<int>& lista)
{

    std::vector<int> iloczyny;

    for (unsigned int i = 0; i < lista.size(); i++) {
        int iloczyn = 1;

        for (unsigned int j = 0; j < lista.size(); j++) {
            if (j == i)
                continue;

            iloczyn *= lista[j];
        }

        iloczyny.push_back(iloczyn);
    }

    lista = iloczyny;
}

void test1()
{
    std::vector<int> lista{ 3, 5, -7, 4, 9, -11, 2 };
    std::vector<int> wynik{ 4, 5, -6, 4, 10, -11, 3 };
    zwieksz(lista);
    assert(lista == wynik);
}

void test2()
{
    std::vector<int> lista{ 3, 5, -7, 4, 9, -11, 2 };
    std::vector<int> wynik{ 0, 5, -7, 4, 0, -11, 2 };
    wyzeruj(lista);
    assert(lista == wynik);
}

void test3()
{
    std::vector<int> lista{ 3, 5, -7, 4, 9, -11, 2 };
    std::vector<int> wynik{ 3, 5, 5, 5, 9, 5, 2 };
    suma(lista);
    assert(lista == wynik);
}

void test4()
{
    std::vector<int> lista{ 3, 5, -7, 4, 9, -11, 2 };
    std::vector<int> wynik{ 27720, 16632, -11880, 20790, 9240, -7560, 41580 };
    zamien(lista);
    assert(lista == wynik);
}

int main()
{

    test1();
    test2();
    test3();
    test4();

    return 0;
}
