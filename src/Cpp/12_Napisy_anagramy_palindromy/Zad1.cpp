#include <algorithm>
#include <cassert>
#include <string>

//Sprawdz czy slowo jest palindromem.

bool palindrom(std::string& slowo)
{
    int N = slowo.length() - 1;
    for (int i = 0; i <= N / 2; i++) {
        if (slowo[i] != slowo[N - i])
            return false;
    }

    return true;
}

void test1()
{
    std::string slowo = "kajak";
    assert(palindrom(slowo));
}

void test2()
{
    std::string slowo = "Pan";
    assert(!palindrom(slowo));
}

int main()
{

    test1();
    test2();

    return 0;
}
