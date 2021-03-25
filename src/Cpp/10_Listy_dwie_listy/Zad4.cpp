#include <cassert>
#include <vector>

//Otrzymujesz dwie listy liczb reprezentujacych
//wspolrzedne dwoch wektorow. Zrealizuj:
//a) mnozenie sklarne.
int mnozenieSkalarne(std::vector<int>& listaA, std::vector<int>& listaB)
{

    assert(listaA.size() == listaB.size());

    int wynik = 0;

    for (unsigned int i = 0; i < listaA.size(); i++)
        wynik += listaA[i] * listaB[i];

    return wynik;
}

//b) mnozenie wektorowe.
std::vector<int> mnozenieWektorowe(std::vector<int>& listaA, std::vector<int>& listaB)
{

    assert(listaA.size() == listaB.size() && listaA.size() == 3);

    std::vector<int> wynik;
    wynik.push_back(listaA[1] * listaB[2] - listaA[2] * listaB[1]);
    wynik.push_back(listaA[2] * listaB[0] - listaA[0] * listaB[2]);
    wynik.push_back(listaA[0] * listaB[1] - listaA[1] * listaB[0]);

    return wynik;
}

void test1()
{
    std::vector<int> listaA{ 3, -5, 4 };
    std::vector<int> listaB{ 2, 6, 5 };

    int iloczynSkalar = -4;
    assert(mnozenieSkalarne(listaA, listaB) == iloczynSkalar);
}

void test2()
{
    std::vector<int> listaA{ 3, -5, 4 };
    std::vector<int> listaB{ 2, 6, 5 };

    std::vector<int> iloczynWekt({ -49, -7, 28 });
    assert(mnozenieWektorowe(listaA, listaB) == iloczynWekt);
}

int main()
{

    test1();
    test2();

    return 0;
}
