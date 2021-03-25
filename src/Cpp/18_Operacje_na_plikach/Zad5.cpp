#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <vector>

//Otrzymujesz napis reprezentujacy sciezke pliku tekstowego.
//Kazdy wiersz pliku reprezentuja adres ip. Posortuj adresy ip i zapisz je w liscie.

std::vector<std::string> wczytajPlik(const std::string& sciezka)
{

    std::vector<std::string> tresc;
    try {
        std::string wiersz;
        std::ifstream plik(sciezka);
        plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit | std::ifstream::badbit);

        while (plik) {
            getline(plik, wiersz);
            tresc.push_back(wiersz);
        }

        plik.close();
    }

    catch (std::exception const& e) {
        std::cout << "Error : " << e.what() << std::endl;
    }

    return tresc;
}

void sortujAdresyIp(std::vector<std::string>& ip)
{
    std::sort(ip.begin(), ip.end(), [](const auto& lhs, const auto& rhs) {
        std::vector<int> oktetA;
        std::vector<int> oktetB;

        auto fun = [&](std::vector<int>& wektor, const std::string& slowo) {
            std::stringstream ss(slowo);

            for (int i; ss >> i;) {
                wektor.push_back(i);
                if (ss.peek() == '.')
                    ss.ignore();
            }
        };

        fun(oktetA, lhs);
        fun(oktetB, rhs);

        if (oktetA == oktetB)
            return false;

        else if (oktetA[0] > oktetB[0])
            return false;

        else if (oktetA[0] < oktetB[0])
            return true;

        else if (oktetA[1] > oktetB[1])
            return false;

        else if (oktetA[1] < oktetB[1])
            return true;

        else if (oktetA[2] > oktetB[2])
            return false;

        else if (oktetA[2] < oktetB[2])
            return true;

        else if (oktetA[3] > oktetB[3])
            return false;

        else if (oktetA[3] < oktetB[3])
            return true;
    });
}

int main()
{

    const std::string sciezka = "folder/adresy_ip.txt";
    auto ip = wczytajPlik(sciezka);
    sortujAdresyIp(ip);

    return 0;
}
