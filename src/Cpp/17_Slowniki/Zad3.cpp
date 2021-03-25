#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

//Zbuduj prosta baze danych dla biblioteki oparta o slownik w ktorym kluczami
//sa imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek.
//Baza danych powinna umozliwiac:
//a) dodanie wypozyczonej ksiazki do danego czytelnika;
void dodajKsiazke(std::unordered_map<std::string, std::vector<std::string>>& lista, const std::string& uzytkownik, const std::string& ksiazka)
{
    if (lista.count(uzytkownik)) {

        if (find(lista[uzytkownik].begin(), lista[uzytkownik].end(), ksiazka) == lista[uzytkownik].end())
            lista[uzytkownik].push_back(ksiazka);

        else
            cout << "Uzytkownik juz wypozyczyl ta ksiazke." << endl;
    }

    else {
        std::vector<std::string> ksiazki{ ksiazka };
        lista[uzytkownik] = ksiazki;
    }
}

//b) usuniecie wypozyczonej ksiazki z listy odpowiadajacej czytelnikowi;
void usunKsiazke(std::unordered_map<std::string, std::vector<std::string>>& lista, const std::string& uzytkownik, const std::string& ksiazka)
{

    if (!lista.count(uzytkownik)) {
        cout << "Podany uzytkownik nie znajduje sie w liscie." << endl;
        return;
    }

    if (find(lista[uzytkownik].begin(), lista[uzytkownik].end(), ksiazka) != lista[uzytkownik].end())
        lista[uzytkownik].erase(remove(lista[uzytkownik].begin(), lista[uzytkownik].end(), ksiazka), lista[uzytkownik].end());

    else
        cout << "Uzytkownik nie wypozyczyl tej ksiazki." << endl;
}

//c) wyswietlenie aktualnej listy ksiazek dla konkretnego czytelnika oraz
//dla wszystkich czytelnikow;
void wyswietlKsiazki(std::unordered_map<std::string, std::vector<std::string>>& lista, const std::string& uzytkownik)
{

    if (!lista.count(uzytkownik)) {
        cout << "Podany uzytkownik nie znajduje sie w liscie." << endl;
        return;
    }

    cout << "Uzytkownik " << uzytkownik << " wypozyczyl nastepujace ksiazki: " << endl;

    for (const auto& ksiazka : lista[uzytkownik])
        cout << ksiazka << endl;
}

void wyswietlWszystkieKsiazki(std::unordered_map<std::string, std::vector<std::string>>& lista)
{

    for (auto it = lista.begin(); it != lista.end(); it++) {
        wyswietlKsiazki(lista, it->first);
        cout << endl;
    }
}

int main()
{

    std::unordered_map<std::string, std::vector<std::string>> lista;

    dodajKsiazke(lista, "Pan T", "Duma i uprzedzenie – Jane Austen");
    dodajKsiazke(lista, "Pan T", "Zabić drozdad – Harper Lee");
    dodajKsiazke(lista, "Pan T", "Biblia");
    dodajKsiazke(lista, "Pan T", "Buszujący w zbożu – JD Salinger");
    dodajKsiazke(lista, "Pan T", "Rok 1984 – George Orwell");
    dodajKsiazke(lista, "Pan T", "Wedy");

    dodajKsiazke(lista, "Elzbieta", "Wielkie nadzieje – Charles Dickens");
    dodajKsiazke(lista, "Elzbieta", "Hobbit – JRR Tolkien");
    dodajKsiazke(lista, "Elzbieta", "Harry Potter – JK Rowling");

    wyswietlWszystkieKsiazki(lista);

    usunKsiazke(lista, "Elzbieta", "Hobbit – JRR Tolkien");
    usunKsiazke(lista, "Pan T", "Zabić drozdad – Harper Lee");
    usunKsiazke(lista, "Pan T", "Rok 1984 – George Orwell");

    wyswietlWszystkieKsiazki(lista);

    return 0;
}
