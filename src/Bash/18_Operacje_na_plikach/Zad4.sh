#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujący ścieżkę pliku tekstowego.
# Wczytaj i wypisz treść pliku.

wypisz_plik() {
    local plik="$1"
    cat "$plik"
}

main() {

    # stworz folder testowy
    mkdir 'test'

    # stworz plik testowy z treścią test
    echo 'test' > 'test/test.txt'

    # wypisz treść pliku testowego
    wypisz_plik 'test/test.txt'

    # usuń folder testowy
    rm -rf 'test'
}

main "$@"