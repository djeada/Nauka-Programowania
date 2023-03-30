/*
Tytul: Sortowanie babelkowe.
Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania
babelkowego. Porownaj sasiednie liczby z listy i zamien je miejscami, jesli
pierwsza jest wieksza od drugiej. Powtarzaj operacje, az przejdziesz przez cala
liste bez dokonywania zmian. Dane wejsciowe: Lista liczb calkowitych. Dane
wyjsciowe: Posortowana lista liczb calkowitych. Przyklad: Dla listy: [6, 2, 1,
4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/

#include <cassert>
#include <vector>

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void sortuj(std::vector<int> &lista) {
  for (long unsigned int i = 0; i < lista.size(); i++) {
    for (long unsigned int j = i + 1; j < lista.size(); j++) {
      if (lista[i] > lista[j])
        swap(&lista[i], &lista[j]);
    }
  }
}

void test1() {
  std::vector<int> lista({4, 2, 5, 3, 1});
  std::vector<int> wynik({1, 2, 3, 4, 5});

  sortuj(lista);

  assert(lista == wynik);
}

int main() {

  test1();

  return 0;
}

// Kompilowano z uzyciem komendy: g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra
// -pedantic -o main.out Zad1.cpp

