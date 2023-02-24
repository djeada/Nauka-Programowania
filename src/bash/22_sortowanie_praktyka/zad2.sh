#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy zdanie. Podziel zdanie na slowa. 
# Posortuj slowa alfabetycznie i zapisz je w liscie. Pamietaj, znaki 
# interpunkcyjne nie sa liczone jako slowa.

sortuj_slowa_w_zdaniu() {
    # Funkcja sortuje alfabetycznie napis.
    local zdanie="$1"
    zdanie="${zdanie//[,.:;?!]/}"
    echo "$zdanie" | tr " "	"\n"  | sort -V | tr "\n" " "	
}

test_sortuj_slowa_w_zdaniu() {
    local wynik=($(sortuj_slowa_w_zdaniu "Lemur wygina smialo cialo"))
    local oczekiwane=(Lemur cialo smialo wygina)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_sortuj_slowa_w_zdaniu
}


main "$@"

