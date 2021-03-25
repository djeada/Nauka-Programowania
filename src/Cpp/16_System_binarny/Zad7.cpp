#include <cassert>

//Zamien miejscami sasiadujace bity.
int zamienSasiadow(int liczba)
{
    int parzyste = liczba & 0xAAAAAAAA;
    int nieparzyste = liczba & 0x55555555;

    parzyste >>= 1;
    nieparzyste <<= 1;

    return parzyste | nieparzyste;
}

void test1()
{
    int liczba = 9131;
    int wynik = 4951;

    assert(zamienSasiadow(liczba) == wynik);
}

int main()
{

    test1();

    return 0;
}
