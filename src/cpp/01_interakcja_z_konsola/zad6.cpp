/*
Tytul: Konwersja jednostek.
Tresc zadania: Napisz program, ktory bedzie konwertowac jednostki zgodnie z
nastepujacymi instrukcjami: a) Pobierz wielkosc w kilogramach i wypisz, ile
gramow odpowiada. b) Pobierz wielkosc w calach i wypisz, ile centymetrow
odpowiada. c) Pobierz liczbe sekund i przelicz na godziny. d) Pobierz liczbe w
euro i wypisz, ile zlotowek odpowiada. e) Pobierz miare kata w stopniach i
wypisz, ile radianow odpowiada. f) Pobierz temperature w stopniach Fahrenheita i
wypisz ile stopni Celsjusza oraz ile stopni Kelvina odpowiada. Dane wejsciowe:
Liczba naturalna we wszystkich podpunktach. Dane wyjsciowe:
* Liczba naturalna dla podpunktow 1 i 3.
* Liczba zmiennoprzecinkowa dla pozostalych podpunktow.
Przyklad:
a) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 2000.
b) Dla pobranej liczby: 12, powinna zostac wypisana liczba: 4.724.
c) Dla pobranej liczby: 3600, powinna zostac wypisana liczba: 1.
d) Dla pobranej liczby: 4, powinna zostac wypisana liczba: 17.6.
e) Dla pobranej liczby: 120, powinna zostac wypisana liczba:  2.094.
f) Dla pobranej liczby: 100, powinny zostac wypisane liczby: 37.777 i -235.222.

*/
#include <iostream>

int main() {

  std::cout << "podaj wielkosc w kilogramach:" << std::endl;

  int kilogramy;
  std::cin >> kilogramy;
  int gramy = kilogramy * 1000;

  std::cout << kilogramy << " kg to " << gramy << " g." << std::endl;

  std::cout << "podaj wielkosc w calach:" << std::endl;

  float cal;
  std::cin >> cal;
  float cm = cal / 2.54;

  std::cout << cal << " cal to " << cm << " cm." << std::endl;

  std::cout << "podaj ilosc sekund:" << std::endl;

  float sekundy;
  std::cin >> sekundy;
  float godziny = sekundy / 3600;

  std::cout << sekundy << " sekund to " << godziny << " godzin" << std::endl;

  std::cout << "podaj liczbe w euro:" << std::endl;

  float euro;
  std::cin >> euro;
  float zloty = euro * 4.40;

  std::cout << euro << " euro to " << zloty << " zlotych" << std::endl;

  std::cout << "podaj miare kata w stopniach:" << std::endl;

  float katStopnie;
  std::cin >> katStopnie;
  float katRad = katStopnie * 0.0174532;

  std::cout << katStopnie << " stopni to " << katRad << " radianow."
            << std::endl;

  std::cout << "podaj temperature w Farenheitach:" << std::endl;

  float tempF;
  std::cin >> tempF;
  float tempC = (tempF - 32) * 5 / 9;
  float tempK = tempC - 273;

  std::cout << tempF << " F to " << tempC << " C i " << tempK << " K"
            << std::endl;

  return 0;
}

