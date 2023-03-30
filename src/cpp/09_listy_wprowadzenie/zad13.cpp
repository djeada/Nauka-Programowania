/*
Tytul: Zmodyfikuj elementy spelniajace warunek.
Tresc: Otrzymujesz liste liczb calkowitych. W wyniku wykonania ponizszych
polecen otrzymasz nowa liste: a) Zwieksz o 1 wszystkie elementy o parzystych
indeksach (indeksy zaczynaja sie od 0). b) Wyzeruj wszystkie elementy bedace
wielokrotnosciami liczby 3. c) Podnies do kwadratu wszystkie elementy mniejsze
niz 10. d) Wstaw sume wszystkich elementow otrzymanej listy na indeksy bedace
liczbami pierwszymi. e) Zamien kazdy element na iloczyn wszystkich elementow
listy poza nim samym. Dane wejsciowe: Lista liczb calkowitych. Dane wyjsciowe:
Lista liczb calkowitych. Przyklad: Dla otrzymanej listy [5, 7, 9, 4, 2]: a)
Wynik: [5, 8, 9, 5, 2] b) Wynik: [5, 0, 0, 5, 2] c) Wynik: [25, 0, 0, 25, 4] d)
Wynik: [37, 0, 0, 25, 4] e) Wynik: [2592, 0, 0, 36, 1080]

*/
#include <algorithm>
#include <cassert>
#include <numeric>
#include <vector>

int sumaCiaguArt(std::vector<int> &lista) {
  int min = *min_element(lista.begin(), lista.end());
  int maks = *max_element(lista.begin(), lista.end());
  return (lista.size() + 1) * (min + maks) / 2;
}

int znajdzBrakujacyElement(std::vector<int> &lista) {

  int sumaListy = accumulate(lista.begin(), lista.end(), 0);
  int sumaPrzedzialu = sumaCiaguArt(lista);

  return sumaPrzedzialu - sumaListy;
}

void test1() {
  std::vector<int> lista{6, 8, 4, 10, 14, 2};
  int wynik = 12;
  assert(znajdzBrakujacyElement(lista) == wynik);
}

void test2() {
  std::vector<int> lista{1, 2, 4, 5, 6};
  int wynik = 3;
  assert(znajdzBrakujacyElement(lista) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}

