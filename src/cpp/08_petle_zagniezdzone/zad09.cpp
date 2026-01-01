/*
Tytul: N pierwszych liczb pierwszych.
Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N
pierwszych liczb pierwszych. Dane wejsciowe: Liczba naturalna. Dane wyjsciowe: N
liczb pierwszych. Przyklad: Dla otrzymanej liczby 5 powinno zostac wypisane: 2,
3, 5, 7, 11.

*/
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>

int czyPierwsza(int n) {
  if (!(n % 2) && n != 2) return false;

  for (int i = 3; i <= sqrt(n); i += 2) {
    if (!(n % i)) return false;
  }

  return true;
}

void liczbyPierwszeV1(int n) {
  for (int i = 2; i <= n; i++) {
    if (czyPierwsza(i)) std::cout << i << " ";
  }
}

void sitoEratostenesa(std::vector<int> &pierwsze, int liczba) {
  for (int p = 2; p <= liczba; p++) {
    if (pierwsze[p] == -1) continue;

    int n = 2;

    for (int i = p * n; i <= liczba; n++, i = p * n) pierwsze[i] = -1;
  }
}

void liczbyPierwszeV2(int liczba) {
  std::vector<int> pierwsze(liczba + 1);

  sitoEratostenesa(pierwsze, liczba);

  for (int i = 2; i <= liczba; i++) {
    if (pierwsze[i] == 0) std::cout << i << " ";
  }
}

int main() {
  int a = 15;

  std::cout << "Liczby pierwsze V1: " << std::endl;

  liczbyPierwszeV1(a);

  std::cout << std::endl;

  std::cout << "Liczby pierwsze V2: " << std::endl;
  liczbyPierwszeV2(a);

  return 0;
}
