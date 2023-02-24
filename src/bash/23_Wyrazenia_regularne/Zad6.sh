#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwa napisy. Znajdz wiersze w pierwszym napisie 
# konczace sie drugim napisem. Wiersz moze byc zakonczony 
# dowolnym znakiem interpunkcyjnym.

wiersze_konczace_sie_napisem() {
    local tekst=$1
    local koniec=$2

    for wiersz in $tekst; do
        if [[ $wiersz == *$koniec ]]; then
            echo $wiersz
        fi
    done

    echo "$tekst" | grep -E ".*$koniec"
}

test_wiersze_konczace_sie_napisem() {
    local tekst="Folgujmy paniom nie sobie, ma rada;
Milujmy wiernie nie jest w nich przysada.
Godnosci trzeba nie za nic tu cnota,
Milosci pragna nie pragna tu zlota."
    local koniec="da"
    local wynik=($(wiersze_konczace_sie_napisem "$tekst" "$koniec"))
    local oczekiwane=('Folgujmy paniom nie sobie, ma rada;' 'Milujmy wiernie nie jest w nich przysada.')

    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_wiersze_konczace_sie_napisem
}


main "$@"

