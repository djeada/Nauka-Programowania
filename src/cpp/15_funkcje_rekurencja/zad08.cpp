/*
Tytul: Wieza Hanoi.
Tresc: N krazkow o roznych srednicach ulozonych jest na jednym z trzech slupkow
(A, B lub C). Na dole znajduje sie krazek o najwiekszej srednicy. Kazdy nastepny
jest mniejszy od poprzedniego. Znajdz sposob na przelozenie wszystkich krazkow
na inny slupek. Pamietaj, ze nie wolno klasc krazka o wiekszej srednicy na
krazek o mniejszej srednicy, ani przekladac kilku krazkow jednoczesnie. Dane
wejsciowe: Liczba naturalna N. Dane wyjsciowe: Lista par znakow. Przyklad: Dla N
= 3, powinna zostac zwrocona lista: [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A',
'B'), ('C', 'A'), ('C', 'B'), ('A', 'B')]

*/
#include <cassert>
#include <utility>
#include <vector>

std::vector<std::pair<char, char>> hanoi(int n) {
  /**
   *
   */
  auto hanoiWew = [&](int n, char a, char b, char c,
                      std::vector<std::pair<char, char>> &wynik) {
    /**
     *
     */
    if (n == 1) {
      wynik.emplace_back(a, b);
      return;
    }

    hanoiWew(n - 1, a, c, b, wynik);
    wynik.emplace_back(a, b);
    hanoiWew(n - 1, c, b, a, wynik);
  };

  std::vector<std::pair<char, char>> wynik;
  hanoiWew(n, 'A', 'B', 'C', wynik);
  return wynik;
}

void test1() {
  int n = 3;
  std::vector<std::pair<char, char>> wynik = {
      {'A', 'B'}, {'A', 'C'}, {'B', 'C'}, {'A', 'B'},
      {'C', 'A'}, {'C', 'B'}, {'A', 'B'}};

  assert(hanoi(n) == wynik);
}

int main() {
  test1();

  return 0;
}
