#include <algorithm>
#include <cassert>
#include <string>
#include <unordered_map>
#include <vector>

//Otrzymujesz tekst w postaci napisu. Znajdz czestosc wystepowania kazdego ze slow w tekscie.
//Zignoruj roznice miedzy malymi i wielkimi literami. Pamietaj, slowa skladaja sie wylacznie z liter!

void wyczysc(std::string& napis)
{
    auto it = napis.begin();

    while (it != napis.end()) {
        if (ispunct(*it))
            napis.erase(it);
        else
            it++;
    }
}

void naMale(std::string& slowo)
{
    transform(slowo.begin(), slowo.end(), slowo.begin(), ::tolower);
}

std::vector<std::string> rozdzielSlowa(const std::string& napis)
{
    std::vector<std::string> wynik;
    int pocz = 0;
    int konc = 0;
    while ((konc = napis.find(' ', pocz)) != std::string::npos) {
        if (konc != pocz) {
            auto slowo = napis.substr(pocz, konc - pocz);
            wyczysc(slowo);
            naMale(slowo);
            if (!slowo.empty())
                wynik.push_back(slowo);
        }
        pocz = konc + 1;
    }
    if (konc != pocz) {
        auto slowo = napis.substr(pocz);
        wyczysc(slowo);
        naMale(slowo);
        if (!slowo.empty())
            wynik.push_back(slowo);
    }

    return wynik;
}

std::unordered_map<std::string, int> budujSlownik(const std::string& tekst)
{
    std::unordered_map<std::string, int> slownik;

    std::vector<std::string> slowa = rozdzielSlowa(tekst);

    for (const auto& slowo : slowa)
        slownik[slowo]++;

    return slownik;
}

void test1()
{
    std::string slowo = "Here,,,, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, "
                        "perhaps a bit; in particular since my tricksy corpus will not match the pattern you EXPECT from it; nor "
                        "will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise "
                        "a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now.";

    std::unordered_map<std::string, int> wynik{ { "here", 1 }, { "a", 12 }, { "tricksy", 4 }, { "corpus", 5 }, { "will", 6 }, { "exist", 1 }, { "very", 2 },
        { "strange", 1 }, { "sometimes", 1 }, { "cryptic", 1 }, { "dumbfound", 1 }, { "you", 2 }, { "maybe", 1 },
        { "perhaps", 1 }, { "bit", 1 }, { "in", 1 }, { "particular", 1 }, { "since", 1 }, { "my", 1 }, { "not", 1 },
        { "match", 1 }, { "the", 2 }, { "pattern", 1 }, { "expect", 1 }, { "from", 2 }, { "it", 2 }, { "nor", 1 },
        { "look", 1 }, { "like", 1 }, { "fish", 1 }, { "boat", 1 }, { "sunflower", 1 }, { "or", 3 },
        { "handsome", 1 }, { "kitten", 1 }, { "surprise", 1 }, { "user", 1 }, { "named", 1 }, { "ami", 1 },
        { "tavory", 1 }, { "this", 1 }, { "be", 1 }, { "fun", 1 }, { "to", 1 }, { "follow", 1 }, { "year", 1 },
        { "month", 1 }, { "minute", 1 }, { "now", 1 } };

    assert(budujSlownik(slowo) == wynik);
}

void test2()
{
    std::string slowo = "The most intelligent people disguise the fact that they are intelligent. Wise men do not wear name tags., "
                        "The more people talk about their own skills, the more desperate they are--their work should speak for itself.";

    std::unordered_map<std::string, int> wynik{ { "itself", 1 }, { "should", 1 }, { "desperate", 1 }, { "aretheir", 1 }, { "own", 1 }, { "their", 1 },
        { "tags", 1 }, { "name", 1 }, { "wear", 1 }, { "the", 4 }, { "work", 1 }, { "most", 1 }, { "they", 2 },
        { "intelligent", 2 }, { "for", 1 }, { "speak", 1 }, { "skills", 1 }, { "not", 1 }, { "people", 2 },
        { "fact", 1 }, { "about", 1 }, { "do", 1 }, { "talk", 1 }, { "more", 2 }, { "disguise", 1 }, { "that", 1 },
        { "are", 1 }, { "wise", 1 }, { "men", 1 } };

    assert(budujSlownik(slowo) == wynik);
}

int main()
{

    test1();
    test2();

    return 0;
}
