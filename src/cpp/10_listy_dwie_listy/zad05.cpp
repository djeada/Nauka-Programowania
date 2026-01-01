/*
ZAD-05 — Średnia ważona
*/
#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <iomanip>

std::vector<double> parseDoubleList(const std::string& line) {
  std::vector<double> result;
  std::string cleaned;
  for (char c : line) {
    if (c != '[' && c != ']' && c != ' ') cleaned += c;
  }
  std::stringstream ss(cleaned);
  std::string token;
  while (std::getline(ss, token, ',')) {
    if (!token.empty()) result.push_back(std::stod(token));
  }
  return result;
}

int main() {
  std::string line1, line2;
  std::getline(std::cin, line1);
  std::getline(std::cin, line2);
  
  std::vector<double> wagi = parseDoubleList(line1);
  std::vector<double> wartosci = parseDoubleList(line2);
  
  double suma = 0.0;
  double suma_wag = 0.0;
  for (size_t i = 0; i < wagi.size(); i++) {
    suma += wagi[i] * wartosci[i];
    suma_wag += wartosci[i];
  }
  
  double srednia = suma / suma_wag;
  std::cout << std::fixed << std::setprecision(2) << srednia << std::endl;
  return 0;
}
