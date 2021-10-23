#!/usr/bin/env bash

# Otrzymujesz rekord z bazy danych reprezentujacy dane pracownika.
# Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki.
# Informacje rozdzielone sa srednikami. Zapisz je w osobnych zmiennych
# i wypisz wraz z komunikatem.

wypisz_dane() {
    IFS='; ' read -ra wynik <<< "$1"
    echo "Imie: ${wynik[0]}"
    echo "Nazwisko: ${wynik[1]}"
    echo "Miejsce urodzenia: ${wynik[2]}"
    echo "Zawod: ${wynik[3]}"
    echo "Zarobki: ${wynik[4]}"
}

main() {
    local napis="Jan; Kowalski; Warszawa; Programista; 1000"
    wypisz_dane "$napis"
}

main "$@"

