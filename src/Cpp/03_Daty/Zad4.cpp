#include <iostream>

int main()
{

    //Dla pobranej liczby, wypisz dzien tygodnia odpowiadajcy tej liczbie.

    std::cout << "Podaj numer dnia tygodnia:" << std::endl;

    int dzien;
    std::cin >> dzien;

    switch (dzien) {
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
        std::cout << "podano niepoprawna liczbe" << std::endl;
    }

    return 0;
}
