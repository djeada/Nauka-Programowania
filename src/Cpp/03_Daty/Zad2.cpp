#include <iostream>

int main()
{

    //Czy osoba jest pelnoletnia?

    std::cout << "Podaj trzy liczby reprezentujace dzien, miesiac i rok urodzenia osoby:" << std::endl;

    int dzien;
    int miesiac;
    int rok;

    std::cin >> dzien;
    std::cin >> miesiac;
    std::cin >> rok;

    std::cout << "Podaj trzy liczby reprezentujace dzisiejsza date:" << std::endl;

    int dzienAktualny;
    int miesiacAktualny;
    int rokAktualny;

    std::cin >> dzienAktualny;
    std::cin >> miesiacAktualny;
    std::cin >> rokAktualny;

    int roznicaLata = rokAktualny - rok;
    int roznicaMiesiace = miesiacAktualny - miesiac;
    int roznicaDni = dzienAktualny - dzien;

    if (roznicaLata > 18)
        std::cout << "osoba jest pelnoletnia" << std::endl;

    else if (roznicaLata == 18) {

        if (roznicaMiesiace > 0)
            std::cout << "osoba jest pelnoletnia" << std::endl;

        else if (roznicaMiesiace == 0) {

            if (roznicaDni >= 0)
                std::cout << "osoba jest pelnoletnia" << std::endl;

            else
                std::cout << "osoba nie jest pelnoletnia" << std::endl;
        } else
            std::cout << "osoba nie jest pelnoletnia" << std::endl;
    }

    else
        std::cout << "osoba nie jest pelnoletnia" << std::endl;

    return 0;
}
