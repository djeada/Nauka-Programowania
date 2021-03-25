#include <cassert>
#include <utility>
#include <vector>

//Dla otrzymanych dwoch list, stworz dwu-kolumnowa macierz,
//ktorej pierwsza kolumna sklada się z elementow pierwszej
//listy, a druga drugiej. Jesli otrzymane listy nie sa rownej
//dlugosci zwroc pusta macierz.

std::vector<std::pair<int, int>> macierz(std::vector<int> listaA, std::vector<int> listaB)
{

    std::vector<std::pair<int, int>> macierz;

    if (listaA.size() != listaB.size())
        return macierz;

    int n = listaA.size();
    macierz.reserve(n);

    for (int i = 0; i < n; i++)
        macierz.push_back(std::pair<int, int>(listaA[i], listaB[i]));

    return macierz;
}

void test1()
{
    std::vector<std::pair<int, int>> wynik{ { 3, 2 }, { 5, 8 }, { 2, 1 } };
    std::vector<int> listaA{ 3, 5, 2 };
    std::vector<int> listaB{ 2, 8, 1 };
    assert(macierz(listaA, listaB) == wynik);
}

int main()
{
    test1();
    return 0;
}
