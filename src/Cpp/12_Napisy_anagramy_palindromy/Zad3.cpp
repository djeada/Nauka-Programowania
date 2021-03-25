#include <cassert>
#include <string>

/*
Dla podanych dwóch napisów sprawdź czy są swoimi anagramami. 
Dwa napisy są anagramami jesli jeden z nich można zbudować 
poprzez przestawienie znakow w drugim.
*/

//Zlozonosc czasowa O(n)
//Zlozonosc pamieciowa O(1)
bool anagram(std::string s1, std::string s2)
{

    int N = s1.length();
    int M = s2.length();

    if (N != M)
        return false;

    int pom[256] = { 0 };

    for (const auto& znak : s1)
        pom[znak]++;

    for (const auto& znak : s2)
        pom[znak]--;

    for (const auto& x : pom) {
        if (x != 0)
            return false;
    }

    return true;
}

void test1()
{
    std::string s1 = "adam";
    std::string s2 = "mada";
    assert(anagram(s1, s2));
}

void test2()
{
    std::string s1 = "adam";
    std::string sw = "dame";
    assert(!anagram(s1, sw));
}

int main()
{
    test1();
    test2();
    return 0;
}
