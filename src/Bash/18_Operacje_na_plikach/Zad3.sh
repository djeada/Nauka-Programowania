#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy nazwe pliku. Przeszukaj caly
# system i zapisz w liscie wszystkie sciezki plikow o danej nazwie.

znajdz_pliki_o_nazwie() {
    local nazwa=$1
    local lista=()
    local sciezka
    for sciezka in $(find ~ -type f); do
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

    # znajdz pliki o nazwie test.txt
    IFS=' ' read -r -a wynik <<< $(znajdz_pliki_o_nazwie 'test.txt')

    # sprawdz czy znaleziono wszystkie pliki
    assert_array_contains wynik "$sciezka_pliku_1" $LINENO
    assert_array_contains wynik "$sciezka_pliku_2" $LINENO

    # usun folder testowy
    rm -rf 'test'
}

main() {
    test_znajdz_pliki_o_nazwie
}

main "$@"
