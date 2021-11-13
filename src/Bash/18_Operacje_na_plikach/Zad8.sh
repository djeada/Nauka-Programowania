#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy sciezke folderu.
# a) Dodaj swoje inicjaly na koncu wszystkich plikow tekstowych 
# znajdujacych sie w folderze oraz podfolderach.
# b) Usun srodkowy wiersz z kazdego pliku csv znajdujacego sie 
# w folderze oraz podfolderach.

dodaj_inicjaly_do_plikow_w_folderze() {
    local folder=$1
    local inicjaly=$2
    local pliki=$(find $folder -type f -name "*.txt")
    for plik in $pliki; do
        sed -i "s/^/$inicjaly /" $plik
    done
}

usun_srodkowy_wiersz_z_plikow_w_folderze() {
    local folder=$1
    local pliki=$(find $folder -type f -name "*.csv")
    for plik in $pliki; do
        sed -i '1d' $plik
    done
}

test_dodaj_inicjaly_do_plikow_w_folderze() {

    # stworz folder testowy wraz z podfolderami
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    # stworz pliki testowe
    local sciezki=('test/test1/plik1.txt' 'test/test1/plik2.txt' 'test/test2/plik3.txt' 'test/test2/plik4.txt')
    local tresc='testowy tekst'	

    for plik in ${sciezki[@]}; do
        echo $tresc > $plik
    done

    # dodaj inicjaly
    local inicjaly='A.D.'
    local dodaj_inicjaly_do_plikow_w_folderze 'test' $inicjaly

    # sprawdz czy pliki zostaly zmodyfikowane
    IFS=$'\n'
    local oczekiwane=('A.D.' 'testowy tekst')
    for plik in ${sciezki[@]}; do
        tresc_pliku=($(cat $plik))
        assertArrayEqual tresc_pliku oczekiwane $LINENO
    done
    unset IFS

    # usun folder testowy
    rm -rf 'test'
}

test_usun_srodkowy_wiersz_z_plikow_w_folderze() {

    # stworz folder testowy wraz z podfolderami
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    # stworz pliki testowe
    local sciezki=('test/test1/plik1.csv' 'test/test1/plik2.csv' 'test/test2/plik3.csv' 'test/test2/plik4.csv')
    local tresc='test1; test2;\ntest3; test4;\ntest5; test6;'

    for plik in ${sciezki[@]}; do
        echo $tresc > $plik
    done

    # usun srodkowy wiersz z plikow
    local usun_srodkowy_wiersz_z_plikow_w_folderze 'test'

    # sprawdz czy pliki zostaly zmodyfikowane
    IFS=$'\n'
    local oczekiwane=('test1; test2;\ntest5; test6;')
    for plik in ${sciezki[@]}; do
        tresc_pliku=($(cat $plik))
        assertArrayEqual tresc_pliku oczekiwane $LINENO
    done

    # usun folder testowy
    rm -rf 'test'
}

main() {
    test_dodaj_inicjaly_do_plikow_w_folderze
    test_usun_srodkowy_wiersz_z_plikow_w_folderze
}

main "$@"
