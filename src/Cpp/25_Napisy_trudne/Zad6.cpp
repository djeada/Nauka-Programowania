#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

/*
Czy slowo A jest rotacja slowa B?
*/

bool czyRotacjaV1(string& s1, string& s2)
{
    int N = s1.length();
    int M = s2.length();

    if (N != M)
        return false;

    string pom = s1 + s1;
    return (pom.find(s2) != string::npos);
}

int main()
{

    //Testy Poprawnosci
    string slowoA = "malpka";
    string slowoB = "pkamal";

    assert(czyRotacjaV1(slowoA, slowoB));

    slowoB = "kamapl";

    assert(!czyRotacjaV1(slowoA, slowoB));

    return 0;
}
