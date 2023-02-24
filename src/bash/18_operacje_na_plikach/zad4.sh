#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy sciezke pliku tekstowego.
# Wczytaj i wypisz tresc pliku.

wypisz_plik() {
    local plik="$1"
    cat "$plik"
}

main() {

    # stworz folder testowy
    mkdir 'test'

    # stworz plik testowy z trescia test
    echo 'test' > 'test/test.txt'

    # wypisz tresc pliku testowego
    wypisz_plik 'test/test.txt'

    # usun folder testowy
    rm -rf 'test'
}

main "$@"