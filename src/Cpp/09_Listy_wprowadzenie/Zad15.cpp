#include <algorithm>
#include <cassert>
#include <unordered_map>
#include <vector>

/*
Dla otrzymanej listy liczb naturalnych, znajdź element dominujący. 
Element dominujący to element, którego liczba wystąpień w liście 
jest większa niż połowa długości listy. Jeśli lista nie ma 
elementu dominującego, zwróć -1.
*/

int elementDominujacyV1(std::vector<int> &lista) {
  int n = lista.size();

  for (int i = 0; i <= n / 2; i++) {
    int licznik = 1;
    for (int j = i + 1; j < n; j++) {
      if (lista[j] == lista[i])
        licznik++;
    }

    if (licznik > n / 2)
      return lista[i];
  }

  return -1;
}

int elementDominujacyV2(std::vector<int> &lista) {

  std::unordered_map<int, int> histo;

  int n = lista.size();

  for (int i = 0; i < n; i++)
    histo[lista[i]]++;

  for (auto para : histo) {
    if (para.second > n / 2)
      return para.first;
  }

  return -1;
}

void test1() {
  std::vector<int> lista{4, 7, 4, 4, 2};
  int wynik = 4;
  assert(elementDominujacyV1(lista) == wynik);
  assert(elementDominujacyV2(lista) == wynik);
}

void test2() {
  std::vector<int> lista{1, 2, 4, 5, 6};
  int wynik = -1;
  assert(elementDominujacyV1(lista) == wynik);
  assert(elementDominujacyV2(lista) == wynik);
}

int main() {

  test1();
  test2();

  return 0;
}
