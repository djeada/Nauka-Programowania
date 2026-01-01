/*
ZAD-02 — Wczytaj, zmodyfikuj i wypisz
*/
#include <iostream>
#include <vector>

void wypisz(const std::vector<int>& lista) {
  for (size_t i = 0; i < lista.size(); i++) {
    if (i > 0) std::cout << ",";
    std::cout << lista[i];
  }
  std::cout << std::endl;
}

int main() {
  int n;
  std::cin >> n;
  
  std::vector<int> original;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    original.push_back(liczba);
  }
  
  // a) Zwiększ każdy element o 1
  std::vector<int> lista_a(n);
  for (int i = 0; i < n; i++) {
    lista_a[i] = original[i] + 1;
  }
  wypisz(lista_a);
  
  // b) Pomnóż każdy element przez jego indeks
  std::vector<int> lista_b(n);
  for (int i = 0; i < n; i++) {
    lista_b[i] = original[i] * i;
  }
  wypisz(lista_b);
  
  // c) Zastąp wszystkie elementy wartością pierwszego elementu
  std::vector<int> lista_c(n);
  int pierwszy = original[0];
  for (int i = 0; i < n; i++) {
    lista_c[i] = pierwszy;
  }
  wypisz(lista_c);

  return 0;
}
