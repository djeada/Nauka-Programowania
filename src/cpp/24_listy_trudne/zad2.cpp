/*
Tytul: Przesun zera.
Tresc: Otrzymujesz liste liczb calkowitych. Przesun wszystkie zera na koniec
listy. Dane wejsciowe: Lista liczb calkowitych. Dane wyjsciowe: Lista liczb
calkowitych. Przyklad: Dla otrzymanej listy: [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0],
powinna zostac zwrocona lista: [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0].

*/
#include <cassert>
#include <vector>

void zeraV1(std::vector<int> &lista) {

  auto N = lista.size();

  for (unsigned int i = 0; i < N; i++) {
    if (lista[i] == 0) {
      auto j = i + 1;

      while (lista[j] == 0 && j < N)
        j++;

      std::iter_swap(lista.begin() + i, lista.begin() + j);
    }
  }
}

// Testy Poprawnosci
void test1() {
  std::vector<int> lista{0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0};
  std::vector<int> wynik{1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0};

  zeraV1(lista);
  assert(lista == wynik);
}

void test2() {
  std::vector<int> lista{0, 0, 0, 0};
  std::vector<int> wynik{0, 0, 0, 0};

  zeraV1(lista);
  assert(lista == wynik);
}

void test3() {
  std::vector<int> lista{1, 2, 3, 4, 5, 6};
  std::vector<int> wynik{1, 2, 3, 4, 5, 6};

  zeraV1(lista);
  assert(lista == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}

