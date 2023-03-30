/*
Tytul: Wczytaj i wypisz.
Tresc: Dla podanej liczby naturalnej N, wczytaj N liczb calkowitych do listy, a
nastepnie: a) Wypisz liste od poczatku do konca, z kazdym elementem w osobnym
wierszu. b) Wypisz liste od konca, z elementami oddzielonymi przecinkami i
wypisanymi w jednym wierszu. Dane wejsciowe: N liczb calkowitych. Dane
wyjsciowe: N liczb. Przyklad: Dla N rownego 3 oraz pobranych liczb: 8, 12, 7, w
drugim podpunkcie powinno zostac wypisane: 7, 12, 8.

*/
#include <iostream>
#include <vector>

void wczytaj(std::vector<int> &lista, int n) {
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }
}

void wypiszOdPoczatku(std::vector<int> &lista) {
  for (auto liczba : lista)
    std::cout << liczba << std::endl;
}

void wypiszOdKonca(std::vector<int> &lista) {
  auto it = cend(lista);
  while (it != cbegin(lista))
    std::cout << *(--it) << ", ";

  std::cout << std::endl;
}

int main() {

  std::vector<int> lista;
  int n;

  std::cout << "podaj liczbe n: " << std::endl;
  std::cin >> n;
  wczytaj(lista, n);

  std::cout << std::endl << "liczby w kolejnosci wczytania:" << std::endl;
  wypiszOdPoczatku(lista);

  std::cout << std::endl << "liczby wypisane od konca:" << std::endl;
  wypiszOdKonca(lista);

  return 0;
}

