/*
ZAD-05 — Zmodyfikuj elementy spełniające warunek
*/
#include <iostream>
#include <vector>
#include <cmath>

void wypisz(const std::vector<int>& lista) {
  for (size_t i = 0; i < lista.size(); i++) {
    if (i > 0) std::cout << ",";
    std::cout << lista[i];
  }
  std::cout << std::endl;
}

bool czy_pierwsza(int n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;
  for (int i = 5; i * i <= n; i += 6) {
    if (n % i == 0 || n % (i + 2) == 0) return false;
  }
  return true;
}

int main() {
  int n;
  std::cin >> n;
  
  std::vector<int> lista;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }
  
  // a) Zwiększ o 1 elementy o parzystych indeksach
  for (int i = 0; i < n; i++) {
    if (i % 2 == 0) lista[i]++;
  }
  wypisz(lista);
  
  // b) Ustaw na 0 elementy będące wielokrotnością 3
  for (int i = 0; i < n; i++) {
    if (lista[i] % 3 == 0) lista[i] = 0;
  }
  wypisz(lista);
  
  // c) Podnieś do kwadratu elementy mniejsze niż 10
  for (int i = 0; i < n; i++) {
    if (lista[i] < 10) lista[i] = lista[i] * lista[i];
  }
  wypisz(lista);
  
  // d) Suma na indeksach pierwszych
  int suma = 0;
  for (int i = 0; i < n; i++) {
    suma += lista[i];
  }
  for (int i = 0; i < n; i++) {
    if (czy_pierwsza(i)) lista[i] = suma;
  }
  wypisz(lista);
  
  // e) Każdy element na iloczyn wszystkich pozostałych
  std::vector<int> nowa(n);
  for (int i = 0; i < n; i++) {
    int iloczyn = 1;
    for (int j = 0; j < n; j++) {
      if (i != j) iloczyn *= lista[j];
    }
    nowa[i] = iloczyn;
  }
  wypisz(nowa);

  return 0;
}
