#include <cassert>
#include <iostream>

/*
Liczby naturalne mniejsze rowne N.	
*/

std::string mniejszeLiczbyV1(int n)
{

    if (n < 0)
        return "";

    if (n == 0)
        return std::to_string(n);

    return std::to_string(n) + ", " + mniejszeLiczbyV1(n - 1);
}

int main()
{
    int n = 10;
    std::string wynik = "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0";
    std::cout << mniejszeLiczbyV1(n) << std::endl;

    return 0;
}
