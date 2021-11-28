#!/usr/bin/env bash

source ../assert.sh

# Zbuduj prosta baze danych dla biblioteki oparta o slownik w ktorym kluczami sa 
# imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek. 
# Baza danych powinna umozliwiac:
# a) Dodanie wypozyczonej ksiazki do danego czytelnika.
# b) Zwrocenie wypozyczonej ksiazki przez czytelnika.
# c) Wypisanie aktualnej listy wypozyczonych ksiazek dla danego czytelnika.

dodaj_ksiazke_do_czytelnika() {
    local czytelnik=$1
    local ksiazka=$2
    baza_danych[$czytelnik]="${baza_danych[$czytelnik]} $ksiazka;"
}

zwroc_ksiazke_czytelnika(){
    local czytelnik=$1
    local ksiazka=$2

    baza_danych[$czytelnik]=${baza_danych[$czytelnik]//" $ksiazka;"/}
}

wypisz_liste_wypozyczonych_ksiazek() {
    local czytelnik=$1

    echo "Czytelnik: $czytelnik wypozyczyl nastepujace ksiazki:"
    for ksiazka in "${baza_danych[$czytelnik]}"; do
        echo "$ksiazka"
    done
}

main() {

    declare -A baza_danych
    dodaj_ksiazke_do_czytelnika "Jan Kowalski" "Opowiesci z Narnii"
    dodaj_ksiazke_do_czytelnika "Jan Kowalski" "Robinson Crusoe"
    dodaj_ksiazke_do_czytelnika "Ewa Nowak" "Opowiesci z Narnii"
    dodaj_ksiazke_do_czytelnika "Ewa Nowak" "Ogniem i mieczem"
    dodaj_ksiazke_do_czytelnika "Tymon Nowak" "Wladca Pierscieni"

    wypisz_liste_wypozyczonych_ksiazek "Jan Kowalski"
    wypisz_liste_wypozyczonych_ksiazek "Ewa Nowak"
    wypisz_liste_wypozyczonych_ksiazek "Tymon Nowak"

    zwroc_ksiazke_czytelnika "Jan Kowalski" "Opowiesci z Narnii"
    wypisz_liste_wypozyczonych_ksiazek "Jan Kowalski"

}


main "$@"
