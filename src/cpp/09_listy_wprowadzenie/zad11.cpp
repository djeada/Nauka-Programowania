/*
ZAD-11 — Policz pary A-B
*/
#include <iostream>
#include <string>

int main() {
  int n;
  std::cin >> n;
  
  std::string lista;
  std::cin >> lista;
  
  int licznik = 0;
  for (int i = 0; i < n; i++) {
    if (lista[i] == 'A') {
      for (int j = i + 1; j < n; j++) {
        if (lista[j] == 'B') licznik++;
      }
    }
  }
  
  std::cout << licznik << std::endl;

  return 0;
}
