#include <cassert>
#include <string>
#include <unordered_map>

// Otrzymujesz napis reprezentujacy zdanie. Znajdz najczesciej wystepujaca
//litere w zdaniu. Jesli wiecej niz jedna litera wystepuje ta sama liczbe
//razy, zwroc litere wczesniej pojawiajaca sie w zdaniu.

std::unordered_map<char, int> budujSlownik(const std::string& slowo)
{
    std::unordered_map<char, int> slownik;

    for (const auto& znak : slowo)
        if (tolower(isalpha(znak)))
            slownik[znak]++;

    return slownik;
}

char litera(const std::string& slowo)
{
    std::unordered_map<char, int> histogram = budujSlownik(slowo);

    int max = -1;
    char maxLitera = '\0';

    for (auto& litera : slowo) {
        if (histogram[litera] > max) {
            maxLitera = litera;
            max = histogram[litera];
        }
    }

    return maxLitera;
}

void test1()
{
    std::string slowo = "lezy jerzy na wiezy";
    char wynik = 'e';

    assert(litera(slowo) == wynik);
}

void test2()
{
    std::string slowo = "The most intelligent people disguise the fact that they are intelligent. Wise men do not wear name tags., "
                        "The more people talk about their own skills, the more desperate they are--their work should speak for itself.";
    char wynik = 'e';

    assert(litera(slowo) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
