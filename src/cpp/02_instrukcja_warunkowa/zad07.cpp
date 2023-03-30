/*
Tytul: Dowody praw logicznych.
Tresc: Pokaz za pomoca operacji logicznych nastepujace prawa:
a) Prawo wylaczonego srodka.
b) Prawo niesprzecznosci.
c) Przemiennosc koniunkcji.
d) Przemiennosc alternatywy.
e) Pierwsze prawo de Morgana.
f) Drugie prawo de Morgana.
Dane wejsciowe: Brak.
Dane wyjsciowe: Komunikat.
a) Prawo wylaczonego srodka:
- Dla p majacego wartosc logiczna: `False` wyrazenie p v ~p ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` wyrazenie p v ~p ma wartosc logiczna: `True`.
b) Zasada niesprzecznosci:
- Dla p majacego wartosc logiczna: `False` wyrazenie ~(p Ʌ ~p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` wyrazenie ~(p Ʌ ~p) ma wartosc logiczna: `True`.
c) Przemiennosc koniunkcji:
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna: `True`.
d) Przemiennosc alternatywy:
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie (p v q) < = > (q v p) ma wartosc logiczna: `True`.
e) Pierwsze prawo de Morgana:
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna: `True`.
f) Drugie prawo de Morgana:
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `False` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `False` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.
- Dla p majacego wartosc logiczna: `True` oraz q majacego wartosc logiczna: `True` wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna: `True`.

*/
#include <iostream>

int main() {

  std::cout << "Prawo wylacznego srodka" << std::endl;
  bool p = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " wyrazenie p v ~p ma wartosc logiczna " << std::boolalpha
            << (p || !p) << std::endl;
  p = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " wyrazenie p v ~p ma wartosc logiczna " << std::boolalpha
            << (p || !p) << std::endl;

  std::cout << "\nZasada niesprzecznosci" << std::endl;
  p = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna " << std::boolalpha
            << !(p && !p) << std::endl;
  p = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna " << std::boolalpha
            << !(p && !p) << std::endl;

  std::cout << "\nPrzemiennosc koniunkcji" << std::endl;
  p = false;
  bool q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna "
            << std::boolalpha << ((p && q) == (q && p)) << std::endl;
  p = true;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna "
            << std::boolalpha << ((p && q) == (q && p)) << std::endl;
  p = false;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna "
            << std::boolalpha << ((p && q) == (q && p)) << std::endl;
  p = true;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna "
            << std::boolalpha << ((p && q) == (q && p)) << std::endl;

  std::cout << "\nPrzemiennosc alternatywy" << std::endl;
  p = false;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna "
            << std::boolalpha << ((p || q) == (q || p)) << std::endl;
  p = true;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna "
            << std::boolalpha << ((p || q) == (q || p)) << std::endl;
  p = false;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna "
            << std::boolalpha << ((p || q) == (q || p)) << std::endl;
  p = true;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna "
            << std::boolalpha << ((p || q) == (q || p)) << std::endl;

  std::cout << "\nPierwsze prawo de Morgana" << std::endl;
  p = false;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;
  p = true;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << "wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;
  p = false;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;
  p = true;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;

  std::cout << "\nDrugie prawo de Morgana" << std::endl;
  p = false;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;
  p = true;
  q = false;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;
  p = false;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;
  p = true;
  q = true;
  std::cout << "dla p majacego wartosc logiczna " << p
            << " oraz q majacego wartosc logiczna " << q
            << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna "
            << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;

  return 0;
}

