#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <cassert>

using namespace std;

/*
Zbuduj prostą bazę danych dla biblioteki opartą o słownik w którym kluczami są 
imiona czytelników, a wartościami listy wypożyczonych książek. 
Baza danych powinna umożliwiać:
a) Dodanie wypożyczonej książki do danego czytelnika.
b) Zwrócenie wypożyczonej książki przez czytelnika.
c) Wypisanie aktualnej listy wypożyczonych książek dla danego czytelnika.
*/

void dodajKsiazke(
  /*
  * Funkcja dodaje ksiazke do listy ksiazek wypozyczonych przez czytelnika w bazie danych.
  */
    std::unordered_map<std::string, std::vector<std::string>> &lista,
    const std::string &uzytkownik, const std::string &ksiazka) {
  if (lista.count(uzytkownik)) {

    if (find(lista[uzytkownik].begin(), lista[uzytkownik].end(), ksiazka) ==
        lista[uzytkownik].end())
      lista[uzytkownik].push_back(ksiazka);

    else
      cout << "Uzytkownik juz wypozyczyl ta ksiazke." << endl;
  }

  else {
    std::vector<std::string> ksiazki{ksiazka};
    lista[uzytkownik] = ksiazki;
  }
}

void usunKsiazke(
    std::unordered_map<std::string, std::vector<std::string>> &lista,
    const std::string &uzytkownik, const std::string &ksiazka) {
  /*
  * Funkcja usuwa ksiazke z listy ksiazek wypozyczonych przez czytelnika w bazie danych.
  */

  if (!lista.count(uzytkownik)) {
    cout << "Podany uzytkownik nie znajduje sie w liscie." << endl;
    return;
  }

  if (find(lista[uzytkownik].begin(), lista[uzytkownik].end(), ksiazka) !=
      lista[uzytkownik].end())
    lista[uzytkownik].erase(
        remove(lista[uzytkownik].begin(), lista[uzytkownik].end(), ksiazka),
        lista[uzytkownik].end());

  else
    cout << "Uzytkownik nie wypozyczyl tej ksiazki." << endl;
}

void wyswietlKsiazki(
  /*
  * Funkcja wypisuje liste wypozyczonych ksiazek dla danego czytelnika.
  */
    std::unordered_map<std::string, std::vector<std::string>> &lista,
    const std::string &uzytkownik) {

  if (!lista.count(uzytkownik)) {
    cout << "Podany uzytkownik nie znajduje sie w liscie." << endl;
    return;
  }

  cout << "Uzytkownik " << uzytkownik
       << " wypozyczyl nastepujace ksiazki: " << endl;

  for (const auto &ksiazka : lista[uzytkownik])
    cout << ksiazka << endl;
}

void wyswietlWszystkieKsiazki(
  /*
  * Funkcja wypisuje liste wszystkich wypozyczonych ksiazek.
  */
    std::unordered_map<std::string, std::vector<std::string>> &lista) {

  for (auto it = lista.begin(); it != lista.end(); it++) {
    wyswietlKsiazki(lista, it->first);
    cout << endl;
  }
}

void testDodajKsiazke() {

  std::unordered_map<std::string, std::vector<std::string>> lista;

  dodajKsiazke(lista, "Jan Kowalski", "W pustyni i w puszczy");
  assert(lista["Jan Kowalski"].size() == 1);
  assert(lista["Jan Kowalski"][0] == "W pustyni i w puszczy");
  dodajKsiazke(lista, "Jan Kowalski", "W pustyni i w puszczy");
  assert(lista["Jan Kowalski"].size() == 1);
  assert(lista["Jan Kowalski"][0] == "W pustyni i w puszczy");
  dodajKsiazke(lista, "Jan Kowalski", "Władca Pierścieni");
  assert(lista["Jan Kowalski"].size() == 2);
  assert(lista["Jan Kowalski"][1] == "Władca Pierścieni");
}

void testUsunKsiazke() {

  std::unordered_map<std::string, std::vector<std::string>> lista {{"Jan Kowalski", {"W pustyni i w puszczy", "Władca Pierścieni"}}, {"Janina Kowalska", {"W pustyni i w puszczy"}}};

  usunKsiazke(lista, "Jan Kowalski", "W pustyni i w puszczy");
  assert(lista["Jan Kowalski"].size() == 1);
  assert(lista["Jan Kowalski"][0] == "Władca Pierścieni");
  usunKsiazke(lista, "Jan Kowalski", "Władca Pierścieni");
  assert(lista["Jan Kowalski"].size() == 0);

}

int main() {

  testDodajKsiazke();
  testUsunKsiazke();

  return 0;
}
