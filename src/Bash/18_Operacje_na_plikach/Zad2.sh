#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwa napisy. Pierwszy napis reprezentuje ścieżkę folderu.
# Drugi napis reprezentuje rozszerzenie szukanych plików. Znajdź w
# folderze wszystkie pliki z danym rozszerzeniem. Nazwy znalezionych
# plików zapisz w liście.

znajdz_pliki_z_rozszerzeniem() {
    local folder="$1"
    local rozszerzenie="$2"
    local pliki=()
    for plik in $(find $folder -maxdepth 10 -type f); do
        if [[ "$plik" == *"$rozszerzenie" ]]; then
            pliki+=("$plik")
        fi
    done
    echo "${pliki[@]}"
}

test_znajdz_pliki_z_rozszerzeniem() {

    # stworz folder testowy
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    # stworz pliki
    touch 'test/test1/test1.txt'
    touch 'test/test1/test2.txt'
    touch 'test/test2/test1.txt'
    touch 'test/test2/test2.txt'

    # znajdz pliki z rozszerzeniem .txt
    IFS=' ' read -r -a wynik <<< $(znajdz_pliki_z_rozszerzeniem 'test' 'txt')

    # sprawdz czy znaleziono wszystkie pliki
    assert_array_contains wynik 'test/test1/test1.txt' $LINENO
    assert_array_contains wynik 'test/test1/test2.txt' $LINENO
    assert_array_contains wynik 'test/test2/test1.txt' $LINENO
    assert_array_contains wynik 'test/test2/test2.txt' $LINENO

    # usun folder testowy
    rm -rf 'test'
}

main() {
    test_znajdz_pliki_z_rozszerzeniem
}

main "$@"