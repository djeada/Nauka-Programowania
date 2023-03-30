/*
Tytul: Samochody jadace w przeciwnych kierunkach.
Tresc: Otrzymujesz liste zlozona wylacznie z liter 'A' i 'B', ktore odpowiadaja
samochodom jadacym odpowiednio na wschod ('A') i zachod ('B'). Policz, ile razy
samochody jadace w przeciwnych kierunkach mijaja sie. Dane wejsciowe: Lista
znakow odpowiadajacych samochodom jadacym na wschod ('A') i zachod ('B'). Dane
wyjsciowe: Liczba naturalna oznaczajaca liczbe mijajacych sie samochodow.
Przyklad:
Dla otrzymanej listy ['A', 'B', 'A', 'B', 'B'] powinna zostac zwrocona liczba 5.

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

void zwieksz(std::vector<int> &lista) {
  for (auto &liczba : lista)
    liczba += 1;
}

void pomnoz(std::vector<int> &lista) {
  for (unsigned int i = 0; i < lista.size(); i++)
    lista[i] *= i;
}

void zastap(std::vector<int> &lista) {
  if (lista.empty())
    return;

  for (auto &liczba : lista)
    liczba = lista[0];
}

void wypisz(std::vector<int> &lista) {
  for (auto liczba : lista)
    std::cout << liczba << ", ";
  std::cout << std::endl;
}

int main() {

  std::vector<int> lista;
  int n;

  std::cout << "podaj liczbe n: ";
  std::cin >> n;
  wczytaj(lista, n);

  std::vector<int> kopia(lista);
  zwieksz(kopia);
  wypisz(kopia);

  kopia = lista;
  pomnoz(kopia);
  wypisz(kopia);

  kopia = lista;
  zastap(kopia);
  wypisz(kopia);

  return 0;
}

