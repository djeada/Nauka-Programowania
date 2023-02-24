#include <cassert>
#include <vector>

/*
Otrzymujesz tablice skladajaca sie wylacznie z zer i jedynek. Znajdz indeks
zera, ktore po zamianie na jedynke daloby najdluzszy nieprzerwany ciag jedynek.
Zachowanie dla otrzymanej tablicy skladajacej sie z samych zer jest
nieokreslone.
*/

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(1)
int znajdzZeroDoPodmianyV1(std::vector<int> &lista) {

  auto licznikJedynek = 0;
  auto licznikZer = 0;

  auto indeksZera = -1;
  auto poprzedniIndeksZera = -1;

  for (unsigned int i = 0; i < lista.size(); i++) {

    if (lista[i] == 1)
      licznikZer++;

    else {
      licznikZer = i - poprzedniIndeksZera;
      poprzedniIndeksZera = i;
    }

    if (licznikZer > licznikJedynek) {
      licznikJedynek = licznikZer;
      indeksZera = poprzedniIndeksZera;
    }
  }

  return indeksZera;
}

// Testy Poprawnosci
void test1() {
  std::vector<int> lista{0, 0, 1, 0, 1, 1, 1, 0, 1, 1};
  int wynik = 7;

  assert(znajdzZeroDoPodmianyV1(lista) == wynik);
}

void test2() {
  std::vector<int> lista{1, 1, 1, 1, 1, 1, 1, 1};
  int wynik = -1;

  assert(znajdzZeroDoPodmianyV1(lista) == wynik);
}

void test3() {
  std::vector<int> lista{1, 0, 1, 1, 1, 1, 1, 1};
  int wynik = 1;

  assert(znajdzZeroDoPodmianyV1(lista) == wynik);
}

int main() {

  test1();
  test2();
  test3();

  return 0;
}
