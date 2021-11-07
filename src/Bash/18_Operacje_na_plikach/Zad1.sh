#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujący ścieżkę. 
# a) Sprawdź, czy jest to ścieżka pliku.
# b) Sprawdź, czy jest to ścieżka folderu.

czy_sciezka_pliku() {
    if [ -f "$1" ]; then
        echo true
    else
        echo false
    fi
}

czy_sciezka_folderu() {
    if [ -d "$1" ]; then
        echo true
    else
        echo false
    fi
}

test_czy_sciezka_pliku() {
    
    # stworz folder testowy
    mkdir 'test'

    # stworz plik testowy
    touch 'test/test.txt'

    # sprawdz czy jest to sciezka pliku
    assertTrue "$(czy_sciezka_pliku test/test.txt)" $LINENO
    assertFalse "$(czy_sciezka_pliku test)" $LINENO

    # usun folder testowy
    rm -rf 'test'
}

test_czy_sciezka_folderu() {
    
    # stworz folder testowy
    mkdir 'test'

    # sprawdz czy jest to sciezka folderu
    assertTrue "$(czy_sciezka_folderu test)" $LINENO

    # usun folder testowy
    rm -rf 'test'
}

main() {
    test_czy_sciezka_pliku
    test_czy_sciezka_folderu
}

main "$@"