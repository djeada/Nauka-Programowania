#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwa napisy. Pierwszy napis reprezentuje sciezke 
# pliku tekstowego. Drugi napis reprezentuje wiersz tekstu. 
# Dostaw otrzymany wiersz tekstu na poczatek pliku tekstowego.

wstaw_na_poczatek_pliku() {
    local plik="$1"
    local wiersz="$2"

    # zapisz tresc pliku do zmiennej
    local tresc_pliku=$(cat "$plik")

    # wstaw wiersz na poczatek pliku
    echo "$wiersz" > "$plik"

    # dodaj zapisana tresc pliku na koniec pliku
    echo "$tresc_pliku" >> "$plik"
}

test_wstaw_na_poczatek_pliku() {

    # stworz folder testowy
    mkdir -p 'test'

    # stworz plik testowy
    local plik='test/plik.txt'
    touch $plik
    local tresc_pliku='testowy plik'
    echo $tresc_pliku > $plik

    # wstaw wiersz na poczatek pliku
    local wiersz='testowy wiersz'
    wstaw_na_poczatek_pliku $plik $wiersz

    # sprawdz czy wiersz zostal dodany na poczatek pliku
    IFS=$'\n' tresc_pliku=($(cat $plik))
    oczekiwane=($wiersz $tresc_pliku)
    assertArrayEqual tresc_pliku oczekiwane $LINENO

    # usun folder testowy
    rm -rf 'test'
}

main() {
    test_wstaw_na_poczatek_pliku
}

main "$@"
