/*
ZAD-15 — Element dominujący
*/
#include <iostream>
#include <vector>
#include <unordered_map>

int main() {
  int n;
  std::cin >> n;
  
  std::unordered_map<int, int> count;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    count[liczba]++;
  }
  
  for (auto& p : count) {
    if (p.second > n / 2) {
      std::cout << p.first << std::endl;
      break;
    }
  }

  return 0;
}
