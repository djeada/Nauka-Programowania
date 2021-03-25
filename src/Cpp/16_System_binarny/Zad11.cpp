#include <bitset>
#include <cassert>

//Czy liczba jest palindromem?

const int liczbaBitow = 8;

bool czyPalindromV1(int liczba)
{

    std::bitset<liczbaBitow> bity = liczba;

    for (int i = 0; i < liczbaBitow / 2 - 1; i++) {
        if (bity[i] ^ bity[liczbaBitow - 1 - i])
            return false;
    }

    return true;
}

void test1()
{
    int liczba = 231;
    assert(czyPalindromV1(liczba));
}

void test2()
{
    int liczba = 17;
    assert(!czyPalindromV1(liczba));
}

int main()
{

    test1();
    test2();

    return 0;
}
