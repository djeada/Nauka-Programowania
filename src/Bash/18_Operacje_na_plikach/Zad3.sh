#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujący nazwę pliku. Przeszukaj cały 
# system i zapisz w liście wszystkie ścieżki plików o danej nazwie.

znajdz_pliki_o_nazwie() {
    local nazwa=$1
    local lista=()
    local sciezka
    for sciezka in $(find . -type f); do
        if [[ $sciezka == *"$nazwa"* ]]; then
            lista+=("$sciezka")
        fi
    done
    echo "${lista[@]}"
}

test_znajdz_pliki_o_nazwie() {

    # stworz folder testowy
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    # stworz pliki
    touch 'test/test1/test.txt'
    touch 'test/test2/test.txt'

    # zapisz sciezke absolutna do pliku
    local sciezka_pliku_1=$(pwd)/test/test1/test.txt
    local sciezka_pliku_2=$(pwd)/test/test2/test.txt

    # znajdz pliki z rozszerzeniem .txt
    IFS=":"
    read -a wynik <<< $(znajdz_pliki_o_nazwie 'test.txt')
    IFS=" "

    # sprawdz czy znaleziono wszystkie pliki
    assert_array_contains wynik "$sciezka_pliku_1"
    assert_array_contains wynik "$sciezka_pliku_2"

    # usun folder testowy
    rm -rf 'test'
}

main() {
    test_znajdz_pliki_o_nazwie
}

main "$@"