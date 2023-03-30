/*
Tytul: Znalezienie wszystkich par elementow listy o sumie rownej podanej
liczbie. Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz
wszystkie pary elementow listy, ktorych suma jest rowna x. Dane wejsciowe: Lista
liczb calkowitych oraz liczba calkowita. Dane wyjsciowe: Lista par liczb
calkowitych. Przyklad: Dla otrzymanej listy: [1, 2, 4, 3, 7] oraz liczby 5,
zostana zwrocone wszystkie pary elementow o sumie rownej 5: [(1, 4), (2, 3)].

*/
#include <algorithm>
#include <cassert>
#include <vector>

void usunPierwszeWystapienieV1(std::vector<int> &lista, int klucz) {
  std::vector<int>::iterator it = lista.begin();
  while (it != lista.end()) {
    if (*it == klucz) {
      it = lista.erase(it);
      return;
    } else
      it++;
  }
}

// Zlozonosc Czasowa O(n^2)
// erase przesuwa wszystkie elementy wiec sam ma zlozonosc O(n)
void usunWszystkieWystapieniaV1(std::vector<int> &lista, int klucz) {
  std::vector<int>::iterator it = lista.begin();
  while (it != lista.end()) {
    if (*it == klucz)
      it = lista.erase(it);

    else
      it++;
  }
}

// Zlozonosc Czasowa O(n)
void usunWszystkieWystapieniaV2(std::vector<int> &lista, int klucz) {
  lista.erase(std::remove(lista.begin(), lista.end(), klucz), lista.end());
}

void test1() {
  std::vector<int> lista{6, 7, 2, 1, 8};
  std::vector<int> wynik{6, 7, 1, 8};
  int klucz = 2;

  usunWszystkieWystapieniaV1(lista, klucz);

  assert(lista == wynik);
}

void test2() {
  std::vector<int> lista{1, 1, 1, 1};
  std::vector<int> wynik;
  int klucz = 1;

  usunWszystkieWystapieniaV2(lista, klucz);

  assert(lista == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

