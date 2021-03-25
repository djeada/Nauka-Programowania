#include <iostream>

int main()
{

    //Czy rok jest przestepny?

    std::cout << "Podaj rok:" << endl;

    int rok;
    std::cin >> rok;

    if (rok % 4 == 0) {

        if (rok % 100 == 0) {
            if (rok % 400 == 0)
                std::cout << "rok jest przestepny" << std::endl;
            else
                std::cout << "rok nie jest przestepny" << endl;
        }

        else
            std::cout << "rok jest przestepny" << endl;
    }

    else
        std::cout << "rok nie jest przestepny" << endl;

    return 0;
}
