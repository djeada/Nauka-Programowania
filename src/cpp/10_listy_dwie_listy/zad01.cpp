/*
ZAD-01 — Wypisanie elementów dwóch list na przemian
*/
#include <iostream>
#include <vector>
#include <sstream>
#include <string>

std::vector<int> parseList(const std::string& line) {
  std::vector<int> result;
  std::string cleaned;
  for (char c : line) {
    if (c != '[' && c != ']' && c != ' ') {
      cleaned += c;
    }
  }
  std::stringstream ss(cleaned);
  std::string token;
  while (std::getline(ss, token, ',')) {
    if (!token.empty()) {
      result.push_back(std::stoi(token));
    }
  }
  return result;
}

int main() {
  std::string line1, line2;
  std::getline(std::cin, line1);
  std::getline(std::cin, line2);
  
  std::vector<int> listaA = parseList(line1);
  std::vector<int> listaB = parseList(line2);
  
  size_t n = std::min(listaA.size(), listaB.size());
  bool first = true;
  
  for (size_t i = 0; i < n; i++) {
    if (!first) std::cout << ",";
    std::cout << listaA[i];
    first = false;
    if (!first) std::cout << ",";
    std::cout << listaB[i];
  }
  
  for (size_t i = n; i < listaA.size(); i++) {
    if (!first) std::cout << ",";
    std::cout << listaA[i];
    first = false;
  }
  
  for (size_t i = n; i < listaB.size(); i++) {
    if (!first) std::cout << ",";
    std::cout << listaB[i];
    first = false;
  }
  
  std::cout << std::endl;

  return 0;
}
