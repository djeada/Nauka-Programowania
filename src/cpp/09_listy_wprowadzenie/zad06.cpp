/*
ZAD-06 — Średnia w liście
*/
#include <iostream>
#include <vector>

int main() {
  int n;
  std::cin >> n;
  
  std::vector<int> lista;
  int suma = 0;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
    suma += liczba;
  }
  
  double srednia = (double)suma / n;
  
  bool znaleziono = false;
  for (int i = 0; i < n; i++) {
    if (lista[i] == srednia) {
      znaleziono = true;
      break;
    }
  }
  
  std::cout << (znaleziono ? "Tak" : "Nie") << std::endl;

  return 0;
}
