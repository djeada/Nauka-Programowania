#include <iostream>

int main()
{

    //Prawo wylacznego srodka
    std::cout << "Prawo wylacznego srodka" << std::endl;
    bool p = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " wyrazenie p v ~p ma wartosc logiczna " << std::boolalpha << (p || !p) << std::endl;
    p = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " wyrazenie p v ~p ma wartosc logiczna " << std::boolalpha << (p || !p) << std::endl;

    //Zasada niesprzecznosci
    std::cout << "\nZasada niesprzecznosci" << std::endl;
    p = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna " << std::boolalpha << !(p && !p) << std::endl;
    p = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " wyrazenie ~(p Ʌ ~p) ma wartosc logiczna " << std::boolalpha << !(p && !p) << std::endl;

    //Przemiennosc koniunkcji
    std::cout << "\nPrzemiennosc koniunkcji" << std::endl;
    p = false;
    bool q = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna " << std::boolalpha << ((p && q) == (q && p)) << std::endl;
    p = true;
    q = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna " << std::boolalpha << ((p && q) == (q && p)) << std::endl;
    p = false;
    q = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna " << std::boolalpha << ((p && q) == (q && p)) << std::endl;
    p = true;
    q = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie (p Ʌ q) < = > (q Ʌ p) ma wartosc logiczna " << std::boolalpha << ((p && q) == (q && p)) << std::endl;

    //Przemiennosc alternatywy
    std::cout << "\nPrzemiennosc alternatywy" << std::endl;
    p = false;
    q = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna " << std::boolalpha << ((p || q) == (q || p)) << std::endl;
    p = true;
    q = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna " << std::boolalpha << ((p || q) == (q || p)) << std::endl;
    p = false;
    q = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna " << std::boolalpha << ((p || q) == (q || p)) << std::endl;
    p = true;
    q = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie (p v q) < = > (q v p) ma wartosc logiczna " << std::boolalpha << ((p || q) == (q || p)) << std::endl;

    //Pierwsze prawo de Morgana
    std::cout << "\nPierwsze prawo de Morgana" << std::endl;
    p = false;
    q = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna " << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;
    p = true;
    q = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << "wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna " << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;
    p = false;
    q = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna " << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;
    p = true;
    q = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie ~(p Ʌ q) < = > (~p v ~q) ma wartosc logiczna " << std::boolalpha << (!(p && q) == (!q || !p)) << std::endl;

    //Drugie prawo de Morgana
    std::cout << "\nDrugie prawo de Morgana" << std::endl;
    p = false;
    q = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna " << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;
    p = true;
    q = false;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna " << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;
    p = false;
    q = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna " << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;
    p = true;
    q = true;
    std::cout << "dla p majacego wartosc logiczna " << p << " oraz q majacego wartosc logiczna " << q << " wyrazenie ~(p v q) < = > (~p Ʌ ~q) ma wartosc logiczna " << std::boolalpha << (!(p || q) == (!q && !p)) << std::endl;

    return 0;
}
