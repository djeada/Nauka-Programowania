/*
ZAD-03 — Dodawanie list element po elemencie
*/
#include <iostream>
#include <vector>
#include <sstream>
#include <string>

std::vector<int> parseList(const std::string& line) {
  std::vector<int> result;
  std::string cleaned;
  for (char c : line) {
    if (c != '[' && c != ']' && c != ' ') cleaned += c;
  }
  std::stringstream ss(cleaned);
  std::string token;
  while (std::getline(ss, token, ',')) {
    if (!token.empty()) result.push_back(std::stoi(token));
  }
  return result;
}

void printList(const std::vector<int>& lista) {
  std::cout << "[";
  for (size_t i = 0; i < lista.size(); i++) {
    if (i > 0) std::cout << ", ";
    std::cout << lista[i];
  }
  std::cout << "]" << std::endl;
}

int main() {
  std::string line1, line2;
  std::getline(std::cin, line1);
  std::getline(std::cin, line2);
  
  std::vector<int> listaA = parseList(line1);
  std::vector<int> listaB = parseList(line2);
  
  std::vector<int> wynik;
  size_t maxSize = std::max(listaA.size(), listaB.size());
  for (size_t i = 0; i < maxSize; i++) {
    int suma = 0;
    if (i < listaA.size()) suma += listaA[i];
    if (i < listaB.size()) suma += listaB[i];
    wynik.push_back(suma);
  }
  
  printList(wynik);
  return 0;
}
