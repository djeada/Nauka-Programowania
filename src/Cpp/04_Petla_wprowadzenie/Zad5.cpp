#include <iostream>

/*
Dla pobranych dwoch liczb, powinny zostac wypisane:

a) Wszystkie liczby naturalne wieksze od mniejszej pobranej liczby
i jednoczesnie mniejsze od wiekszej pobranej liczby.
b) Wszystkie liczby naturalne podzielne przez 3 wieksze od mniejszej
pobranej liczby i jednoczesnie mniejsze od wiekszej pobranej liczby.
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

  std::cout << "Liczby naturalne wieksze od mniejszej pobranej liczby i "
               "jednoczesnie mniejsze od wiekszej pobranej liczby: "
            << std::endl;

  for (int i = a + 1; i < b; i++)
    std::cout << i << " ";

  std::cout << std::endl;

  std::cout
      << "Liczby naturalne podzielne przez 3 wieksze od mniejszej pobranej "
         "liczby i jednoczesnie mniejsze od wiekszej pobranej liczby: "
      << std::endl;

  for (int i = a + 1; i < b; i++) {
    if (i % 3 == 0)
      std::cout << i << " ";
  }

  return 0;
}
