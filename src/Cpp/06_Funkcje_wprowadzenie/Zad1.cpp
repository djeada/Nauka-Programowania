#include <cassert>
#include <string>

//Napisz funkcje ktora zwroci
//a) liczbe 3

int funkcja1()
{
    return 3;
}

//b) napis "Tak"
std::string funkcja2()
{
    return "Tak";
}

//c) wartosc logiczna prawda
bool funkcja3()
{
    return true;
}

void test1()
{
    assert(funkcja1() == 3);
}

void test2()
{
    assert(funkcja2() == "Tak");
}

void test3()
{
    assert(funkcja3());
}

int main()
{

    test1();
    test2();
    test3();

    return 0;
}
