/*
Tytul: Sortowanie przez wybieranie.
Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania przez
wybieranie. Znajdz najwiekszy element w liscie i zapisz go do zmiennej.
Nastepnie znajdz najmniejszy element w pozostalej czesci listy i zamien go z
pierwszym elementem nieposortowanej czesci. Powtarzaj operacje, az lista bedzie
posortowana. Dane wejsciowe: Lista liczb calkowitych. Dane wyjsciowe:
Posortowana lista liczb calkowitych. Przyklad: Dla listy: [6, 2, 1, 4, 27],
powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/

#include <cassert>
#include <vector>

void sortuj(std::vector<int> &lista) {
  auto it = lista.begin();

  while (it != lista.end()) {

    auto it_min = it;

    for (auto i = it + 1; i != lista.end(); i++) {

      if (*i < *it_min)
        it_min = i;
    }

    std::iter_swap(it, it_min);
    it++;
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
// -pedantic -o main.out Zad2.cpp

