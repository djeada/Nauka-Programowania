/*
Tytul: Liczby z okreslonego przedzialu.
Tresc: Dla otrzymanych dwoch liczb naturalnych wypisz:
a) Wszystkie liczby naturalne wieksze od mniejszej otrzymanej liczby i jednoczesnie mniejsze od wiekszej otrzymanej liczby.
b) Wszystkie liczby naturalne podzielne przez 3 wieksze od mniejszej otrzymanej liczby i jednoczesnie mniejsze od wiekszej otrzymanej liczby.
Dane wejsciowe: Dwie liczby naturalne.
Dane wyjsciowe: Kilka liczb naturalnych.
Przyklad:
Dla otrzymanych liczb 9 i 5 powinny zostac wypisane liczby 6, 7 i 8.

*/
#include <iostream>

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

