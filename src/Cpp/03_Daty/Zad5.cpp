#include <iostream>

int main()
{

    //Dla pobranej liczby, wyswietl liczbe dni miesiaca odpowiadajacemu danej liczbie.

    std::cout << "Podaj numer miesiaca:" << std::endl;

    int numer;
    std::cin >> numer;

    switch (numer) {
    case 1:
        std::cout << "Styczen ma 31 dni" << std::endl;
        break;

    case 2:
        std::cout << "Luty ma 28 lub 29 dni" << std::endl;
        break;

    case 3:
        std::cout << "Marzec ma 31 dni" << std::endl;
        break;

    case 4:
        std::cout << "Kwiecien ma 30 dni" << std::endl;
        break;

    case 5:
        std::cout << "Maj ma 31 dni" << std::endl;
        break;

    case 6:
        std::cout << "Czerwiec ma 30 dni" << std::endl;
        break;

    case 7:
        std::cout << "Lipiec ma 31 dni" << std::endl;
        break;

    case 8:
        std::cout << "Sierpien ma 31 dni" << std::endl;
        break;

    case 9:
        std::cout << "Wrzesien ma 30 dni" << std::endl;
        break;

    case 10:
        std::cout << "Pazdziernik ma 31 dni" << std::endl;
        break;

    case 11:
        std::cout << "Listopad ma 30 dni" << std::endl;
        break;

    case 12:
        std::cout << "Grudzien ma 31 dni" << std::endl;
        break;

    default:
        std::cout << "Podano niepoprawny numer miesiaca" << std::endl;
    }

    return 0;
}
