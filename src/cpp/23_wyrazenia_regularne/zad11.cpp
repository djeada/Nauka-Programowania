/*
ZAD-11 — Nazwa pliku bez rozszerzenia

**Poziom:** ★★☆
**Tagi:** `regex`, `string`, `ścieżki`

### Treść

Otrzymujesz napis reprezentujący pełną ścieżkę do pliku. Wyodrębnij nazwę pliku
(bez katalogów) i usuń rozszerzenie (część po ostatniej kropce). Zwróć samą
nazwę bez rozszerzenia.

Ścieżka może zawierać separator `\` lub `/`.

### Wejście

Jedna linia:

* `sciezka`

### Wyjście

Jedna linia:

* `nazwa_pliku_bez_rozszerzenia`

### Przykład

**Wejście:**

```
C:\my-long\path_directory\file.html
```

**Wyjście:**

```
file
```

*/

#include <cassert>
#include <regex>
#include <string>

std::string nazwaPliku(std::string &sciezka) {
  const std::regex wzorzec("(.*[\\\\/]+)?([^\\.]*)(.*)?");
  std::smatch wynik;

  if (std::regex_match(sciezka, wynik, wzorzec) && wynik.size() > 1)
    return wynik[2].str();

  return "";
}

void test1() {
  std::string sciezka = "C:\\Windows\\explorer.exe";
  std::string wynik = "explorer";

  assert(nazwaPliku(sciezka) == wynik);
}

void test2() {
  std::string sciezka = "/home/user/var/log/syslog";
  std::string wynik = "syslog";
  assert(nazwaPliku(sciezka) == wynik);
}

void test3() {
  std::string sciezka = "test.jpg.png.mp3.mp5.html.txt";
  std::string wynik = "test";
  assert(nazwaPliku(sciezka) == wynik);
}

void test4() {
  std::string sciezka = "test";
  std::string wynik = "test";
  assert(nazwaPliku(sciezka) == wynik);
}

int main() {
  test1();
  test2();
  test3();
  test4();

  return 0;
}
