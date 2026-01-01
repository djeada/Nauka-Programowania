/*
ZAD-04 — Iloczyn skalarny i wektorowy
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

int main() {
  std::string line1, line2;
  std::getline(std::cin, line1);
  std::getline(std::cin, line2);
  
  std::vector<int> listaA = parseList(line1);
  std::vector<int> listaB = parseList(line2);
  
  // Iloczyn skalarny
  int iloczyn = 0;
  for (size_t i = 0; i < listaA.size(); i++) {
    iloczyn += listaA[i] * listaB[i];
  }
  
  std::cout << iloczyn << std::endl;
  return 0;
}
