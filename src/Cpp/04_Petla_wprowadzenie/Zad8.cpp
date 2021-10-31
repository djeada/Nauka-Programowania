#include <iostream>

/*
Na farmie mamy a glow i b nog, znajdz liczbe kur oraz liczbe owieczek.
*/

int main() {

  std::cout << "Podaj dwie liczby: " << std::endl;
  int glowy, nogi;
  std::cin >> glowy >> nogi;

  for (int i = 0; i < glowy; i++) {
    int owce = glowy - i;
    if (2 * i + 4 * owce == nogi) {
      std::cout << i << " " << owce << std::endl;
      break;
    }
  }

  return 0;
}
