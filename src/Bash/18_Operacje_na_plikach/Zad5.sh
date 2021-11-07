#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujący ścieżkę pliku tekstowego. 
# Każdy wiersz pliku reprezentuje adres ip. Posortuj adresy ip 
# i zapisz je w liście.

wczytaj_plik() {
    local plik="$1"
    local lista=()
    while read -r wiersz; do
        lista+=("$wiersz")
    done < "$plik"
    echo "${lista[@]}"
}

sortuj_adresy_ip() {
    local lista_posortowana=()
    # rozdziel kazdy adres ip z listy za pomoca '.'
    IFS='.' 
    read -r -a adresy <<< "$lista"
    IFS=' '
    # zamien kazdy adres ip na liczbe
    for adres in "${adresy[@]}"; do
        lista_posortowana+=("$(echo "$adres" | sed 's/[^0-9]//g')")
    done
    # sortuj liczby
    lista_posortowana=($(for liczba in "${lista_posortowana[@]}"; do echo "$liczba"; done | sort))
    # zamien liczby na adresy ip
    for liczba in "${lista_posortowana[@]}"; do
        lista_posortowana+=("$(echo "$liczba" | sed 's/^0*//')")
    done
    # zamien adresy ip na napisy
    for adres in "${lista_posortowana[@]}"; do
        lista_posortowana+=("$(echo "$adres" | sed 's/^0*//')")
    done
    echo "${lista_posortowana[@]}"
}

test_sortuj_adresy_ip() {

    # stworz folder testowy
    mkdir 'test'

    # stworz plik testowy
    touch 'test/test.txt'
    echo "123.4.245.23\n104.244.253.29\n1.198.3.93\n32.183.93.40\n104.30.244.2\n104.244.4.1" > 'test/test.txt'

    # wcztaj plik
    IFS=":"
    read -a lista <<< $(wczytaj_plik 'test/test.txt')
    IFS=":"
    read -a wynik <<< sortuj_adresy_ip
    IFS=" "

    # sprawdz czy adresy ip sa posortowane
    oczekiwane=(1.198.3.93 32.183.93.40 104.30.244.2 104.30.244.2 104.244.253.29 123.4.245.23)
    assert_array_equal lista wynik

    # usun folder testowy
    rm -rf 'test'
}

main() {
    test_sortuj_adresy_ip
}

main "$@"