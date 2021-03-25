#include <cassert>
#include <utility>
#include <vector>

//Wieza Hanoi.

void hanoiWew(int n, char a, char b, char c, std::vector<std::pair<char, char>>& wynik)
{

    if (n == 1) {
        wynik.emplace_back(a, b);
        return;
    }

    hanoiWew(n - 1, a, c, b, wynik);
    wynik.emplace_back(a, b);
    hanoiWew(n - 1, c, b, a, wynik);
}

std::vector<std::pair<char, char>> hanoi(int n)
{
    std::vector<std::pair<char, char>> wynik;
    hanoiWew(n, 'A', 'B', 'C', wynik);
    return wynik;
}

void test1()
{
    int n = 3;
    std::vector<std::pair<char, char>> wynik = { { 'A', 'B' }, { 'A', 'C' }, { 'B', 'C' },
        { 'A', 'B' }, { 'C', 'A' }, { 'C', 'B' }, { 'A', 'B' } };

    assert(hanoi(n) == wynik);
}

int main()
{

    test1();

    return 0;
}
