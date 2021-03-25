#include <iostream>

int main()
{

    //Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.

    std::cout << "podaj wielkosc w kilogramach:" << std::endl;

    int kilogramy;
    std::cin >> kilogramy;
    int gramy = kilogramy * 1000;

    std::cout << kilogramy << " kg to " << gramy << " g." << std::endl;

    //Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.

    std::cout << "podaj wielkosc w calach:" << std::endl;

    float cal;
    std::cin >> cal;
    float cm = cal / 2.54;

    std::cout << cal << " cal to " << cm << " cm." << std::endl;

    //Pobierz ilosc sekund i przelicz na godziny.

    std::cout << "podaj ilosc sekund:" << std::endl;

    float sekundy;
    std::cin >> sekundy;
    float godziny = sekundy / 3600;

    std::cout << sekundy << " sekund to " << godziny << " godzin" << std::endl;

    //Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada.

    std::cout << "podaj liczbe w euro:" << std::endl;

    float euro;
    std::cin >> euro;
    float zloty = euro * 4.40;

    std::cout << euro << " euro to " << zloty << " zlotych" << std::endl;

    //Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada.

    std::cout << "podaj miare kata w stopniach:" << std::endl;

    float katStopnie;
    std::cin >> katStopnie;
    float katRad = katStopnie * 0.0174532;

    std::cout << katStopnie << " stopni to " << katRad << " radianow." << std::endl;

    //Pobierz temperature w stopniach Farenheita i wypisz
    //ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada.

    std::cout << "podaj temperature w Farenheitach:" << std::endl;

    float tempF;
    std::cin >> tempF;
    float tempC = (tempF - 32) * 5 / 9;
    float tempK = tempC - 273;

    std::cout << tempF << " F to " << tempC << " C i " << tempK << " K" << std::endl;

    return 0;
}
