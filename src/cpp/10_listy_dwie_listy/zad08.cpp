/*
ZAD-08 — Łączenie posortowanych list
*/
#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

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
  size_t i = 0, j = 0;
  
  while (i < listaA.size() && j < listaB.size()) {
    if (listaA[i] < listaB[j]) {
      wynik.push_back(listaA[i++]);
    } else {
      wynik.push_back(listaB[j++]);
    }
  }
  
  while (i < listaA.size()) {
    wynik.push_back(listaA[i++]);
  }
  
  while (j < listaB.size()) {
    wynik.push_back(listaB[j++]);
  }
  
  printList(wynik);
  return 0;
}
