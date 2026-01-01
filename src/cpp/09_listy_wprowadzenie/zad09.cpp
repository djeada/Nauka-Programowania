/*
ZAD-09 — Usuń duplikaty
*/
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  int n;
  std::cin >> n;
  
  std::vector<int> lista;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }
  
  std::vector<int> nowa;
  for (int i = 0; i < n; i++) {
    bool juz_jest = false;
    for (size_t j = 0; j < nowa.size(); j++) {
      if (nowa[j] == lista[i]) {
        juz_jest = true;
        break;
      }
    }
    if (!juz_jest) {
      nowa.push_back(lista[i]);
    }
  }
  
  for (size_t i = 0; i < nowa.size(); i++) {
    if (i > 0) std::cout << ",";
    std::cout << nowa[i];
  }
  std::cout << std::endl;

  return 0;
}
