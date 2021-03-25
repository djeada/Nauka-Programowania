#include <cassert>
#include <regex>
#include <sstream>
#include <string>
#include <vector>

//Otrzymujesz dwa napisy. Pierwszy napis reprezentuje tekst, a drugi zakazane
//slowo. Jesli w danym wierszu tekstu wystepuje zakazane slowo, to usun czesc
//wiersza od wystapienia zakazanego slowa do konca.

std::string wektorNaString(std::vector<std::string>& lista)
{
    std::ostringstream oss;

    if (!lista.empty()) {
        std::copy(lista.begin(), lista.end() - 1, std::ostream_iterator<std::string>(oss, ""));
        oss << lista.back();
    }

    return oss.str();
}

std::vector<std::string> rozdziel(const std::string& napis)
{
    std::vector<std::string> wynik;
    std::string wiersz;
    std::istringstream strumien(napis);
    while (std::getline(strumien, wiersz, '\n'))
        wynik.push_back(wiersz);

    return wynik;
}

std::string wczyscTekst(std::string& tekst, std::string& napis)
{
    std::vector<std::string> wynik;
    std::regex wzorzec(std::string(napis + "(.*)"));

    auto _wiersze = rozdziel(tekst);

    for (auto& wiersz : _wiersze) {
        wynik.push_back(std::regex_replace(wiersz, wzorzec, "\n"));
    }

    return wektorNaString(wynik);
}

void test1()
{
    std::string tekst = "Turned it up should no valley cousin he.\nSpeaking numerous ask did horrible packages set.\nAshamed herself has distant can studied mrs.\nLed therefore its middleton perpetual fulfilled provision frankness.\nSmall he drawn after among every three no.\nAll having but you edward genius though remark one.\nRooms oh fully taken by worse do.\nPoints afraid but may end law lasted.\nWas out laughter raptures returned outweigh.\nLuckily cheered colonel me do we attacks on highest enabled.\nTried law yet style child.\nBore of true of no be deal.\nFrequently sufficient in be unaffected.\nThe furnished she concluded depending procuring concealed.";
    std::string napis = "a";
    std::string wynik = "Turned it up should no v\nSpe\nAsh\nLed therefore its middleton perpetu\nSm\nAll h\nRooms oh fully t\nPoints \nW\nLuckily cheered colonel me do we \nTried l\nBore of true of no be de\nFrequently sufficient in be un\nThe furnished she concluded depending procuring conce\n";

    assert(wczyscTekst(tekst, napis) == wynik);
}

int main()
{

    test1();

    return 0;
}
