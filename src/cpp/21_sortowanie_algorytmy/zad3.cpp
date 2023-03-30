/*
Tytul: Sortowanie przez wstawianie.
Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania przez
wstawianie. Stworz nowa, pusta liste i dodaj do niej pierwszy element listy
wejsciowej. Dla kazdego kolejnego elementu znajdz odpowiednie miejsce w
posortowanej juz czesci listy i wstaw go tam. Dane wejsciowe: Lista liczb
calkowitych. Dane wyjsciowe: Posortowana lista liczb calkowitych. Przyklad: Dla
listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/

#include <cassert>
#include <vector>

void sortuj(std::vector<int> &lista) {
  for (unsigned int i = 1; i < lista.size(); i++) {
    int klucz = lista[i];
    int j = i - 1;

    while (j >= 0 && lista[j] > klucz) {
      lista[j + 1] = lista[j];
      j--;
    }

    lista[j + 1] = klucz;
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
// -pedantic -o main.out Zad3.cpp

