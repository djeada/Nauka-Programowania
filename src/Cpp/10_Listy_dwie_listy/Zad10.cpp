#include <algorithm>
#include <cassert>
#include <vector>

//Otrzymujesz dwie posortowane listy rownej
//dlugosci. Znajdz ich mediane.

//Zlozonosc obliczeniowa O(m + n)
//Zlozonosc pamieciowa O(1)
double mediana(std::vector<int>& listaA, std::vector<int>& listaB)
{
    unsigned int i = 0;
    unsigned int j = 0;
    unsigned int n = listaA.size();
    unsigned int m = listaB.size();
    double m1 = -1, m2 = -1;

    for (unsigned int licznik = 0; licznik <= (n + m) / 2; licznik++) {
        if ((m + n) % 2 == 0)
            m2 = m1;

        if (i != n && j != m)
            m1 = (listaA[i] > listaB[j]) ? listaB[j++] : listaA[i++];

        else if (i < n)
            m1 = listaA[i++];

        else
            m1 = listaB[j++];
    }

    if ((m + n) % 2 == 1)
        return m1;

    return (m1 + m2) / 2.00;
}

void test1()
{
    std::vector<int> listaA({ 2, 4, 7 });
    std::vector<int> listaB({ 3, 5, 9 });

    double wynik = 4.5;
    assert(mediana(listaA, listaB) == wynik);
}

int main()
{

    test1();

    return 0;
}
