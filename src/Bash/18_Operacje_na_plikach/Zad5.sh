#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujący ścieżkę pliku tekstowego.
# Każdy wiersz pliku reprezentuje adres ip. Posortuj adresy ip
# i zapisz je w liście.

sortuj_adresy_ip() {
    sort -t . -g -k1,1 -k2,2 -k3,3 -k4,4 $1
}

test_sortuj_adresy_ip() {

    # stworz folder testowy
    mkdir -p 'test'

    # stworz plik testowy
    local plik='test/test.txt'
    touch $plik
    echo "123.4.245.23"  > $plik
    echo "104.244.253.29"  >> $plik
    echo "1.198.3.93" >> $plik
    echo "32.183.93.40" >> $plik
    echo "104.30.244.2" >> $plik
    echo "104.244.4.1" >> $plik

    # sortuj adresy ip
    IFS=$'\n' 
    wynik=($(sortuj_adresy_ip 'test/test.txt'))

    # sprawdz czy adresy ip sa posortowane
    local oczekiwane=(1.198.3.93 32.183.93.40 104.30.244.2 104.244.4.1 104.244.253.29 123.4.245.23)
    assertArrayEqual wynik oczekiwane $LINENO

    # usun folder testowy
    rm -rf 'test'
}

main() {
    test_sortuj_adresy_ip
}

main "$@"
