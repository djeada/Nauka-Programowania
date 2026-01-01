/*
ZAD-10 — Mediana dwóch posortowanych list
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

int main() {
  std::string line1, line2;
  std::getline(std::cin, line1);
  std::getline(std::cin, line2);
  
  std::vector<int> listaA = parseList(line1);
  std::vector<int> listaB = parseList(line2);
  
  std::vector<int> polaczony;
  for (int a : listaA) polaczony.push_back(a);
  for (int b : listaB) polaczony.push_back(b);
  
  std::sort(polaczony.begin(), polaczony.end());
  
  double mediana;
  int n = polaczony.size();
  if (n % 2 == 0) {
    mediana = (polaczony[n/2 - 1] + polaczony[n/2]) / 2.0;
  } else {
    mediana = polaczony[n/2];
  }
  
  std::cout << mediana << std::endl;
  return 0;
}
