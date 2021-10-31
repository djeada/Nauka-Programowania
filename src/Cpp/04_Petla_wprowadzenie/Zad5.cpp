#include <iostream>

/*
Dla pobranych dwóch liczb, powinny zostać wypisane:

a) Wszystkie liczby naturalne większe od mniejszej pobranej liczby
i jednocześnie mniejsze od większej pobranej liczby.
b) Wszystkie liczby naturalne podzielne przez 3 większe od mniejszej
pobranej liczby i jednocześnie mniejsze od większej pobranej liczby.
*/

int main() {

  std::cout << "Podaj dwie liczby: " << std::endl;
  int a, b;
  std::cin >> a >> b;

  if (b < a) {
    int pom = a;
    a = b;
    b = pom;
  }

  std::cout << "Liczby naturalne większe od mniejszej pobranej liczby i "
               "jednocześnie mniejsze od większej pobranej liczby: "
            << std::endl;

  for (int i = a + 1; i < b; i++)
    std::cout << i << " ";

  std::cout << std::endl;

  std::cout
      << "Liczby naturalne podzielne przez 3 większe od mniejszej pobranej "
         "liczby i jednocześnie mniejsze od większej pobranej liczby: "
      << std::endl;

  for (int i = a + 1; i < b; i++) {
    if (i % 3 == 0)
      std::cout << i << " ";
  }

  return 0;
}
