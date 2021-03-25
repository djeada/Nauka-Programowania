#include <iostream>

int main()
{

    /*Niech data bedzie dana w formacie DD/MM/CCYY :
	DD - dzien
	MM - miesiac
	CC - stulecie
	YY - rok 

	A = CC/4 - 2*CC - 1 
	B = 5*YY/4
	C = 26*(MM + 1)/10

	Dzien = (A + B + C + DD) mod 7
	*/

    std::cout << "Podaj dzien:" << std::endl;
    int DD;
    std::cin >> DD;

    std::cout << "Podaj miesiac:" << std::endl;
    int MM;
    std::cin >> MM;

    std::cout << "Podaj rok:" << std::endl;
    int rok;
    std::cin >> rok;

    int CC = rok / 100;
    int YY = rok % 100;

    int A = (CC / 4) - 2 * CC - 1;
    int B = 5 * YY / 4;
    int C = 26 * (MM + 1) / 10;

    int wynik = (A + B + C + DD) % 7;

    switch (wynik) {
    case 1:
        std::cout << "pierwszym dniem tygodnia jest poniedzialek" << std::endl;
        break;

    case 2:
        std::cout << "drugim dniem tygodnia jest wtorek" << std::endl;
        break;

    case 3:
        std::cout << "trzecim dniem tygodnia jest sroda" << std::endl;
        break;

    case 4:
        std::cout << "czwartym dniem tygodnia jest czwartek" << std::endl;
        break;

    case 5:
        std::cout << "piatym dniem tygodnia jest piatek" << std::endl;
        break;

    case 6:
        std::cout << "szostym dniem tygodnia jest sobota" << std::endl;
        break;

    case 7:
        std::cout << "siodmym dniem tygodnia jest niedziela" << std::endl;
        break;

    default:
        std::cout << "bledne dane" << std::endl;
    }

    return 0;
}
