/*
Tytul: Sortowanie szybkie.
Tresc: Dla danej listy liczb calkowitych zaimplementuj algorytm sortowania
szybkiego.
1. Jesli dlugosc listy jest mniejsza niz 2, zwroc liste.
2. Wybierz element rozdzielajacy, nazywany pivotem.
3. Podziel liste na trzy czesci: elementy mniejsze od pivota, pivot oraz
elementy wieksze od pivota.
4. Wywolaj rekurencyjnie sortowanie szybkie dla czesci z elementami mniejszymi
od pivota i wiekszymi od pivota.
5. Scal posortowane czesci listy w jedna posortowana liste.
Dane wejsciowe: Lista liczb calkowitych.
Dane wyjsciowe: Posortowana lista liczb calkowitych.
Przyklad:
Dla danej listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6,
27].

*/

#include <cassert>
#include <functional>
#include <vector>

int rozdziel(std::vector<int> &lista, int indeksPocz, int indeksKonc) {
  int wartosc = lista[indeksKonc];
  int i = indeksPocz - 1;
  for (int j = indeksPocz; j < indeksKonc; j++) {
    if (lista[j] <= wartosc) {
      i++;
      std::swap(lista[i], lista[j]);
    }
  }

  std::swap(lista[i + 1], lista[indeksKonc]);

  return i + 1;
}

void sortuj(std::vector<int> &lista) {
  std::function<void(std::vector<int> &, int, int)> _sortuj;
  _sortuj = [&_sortuj](std::vector<int> &lista, int p, int r) {
    if (p < r) {
      int q = rozdziel(lista, p, r);
      _sortuj(lista, p, q - 1);
      _sortuj(lista, q + 1, r);
    }
  };

  _sortuj(lista, 0, lista.size() - 1);
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
// -pedantic -o main.out Zad5.cpp

