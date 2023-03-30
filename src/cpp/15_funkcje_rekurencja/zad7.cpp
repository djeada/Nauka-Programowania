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

int ciagV1(int n) {
  /**
   *
   */
  if (n == 1)
    return 1;

  return 1 + ciagV1(n - 1) * 2;
}

void test1() {
  int n = 5;
  int wynik = 31;

  assert(ciagV1(n) == wynik);
}

int main() {

  test1();

  return 0;
}

