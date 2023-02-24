#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis. Podziel go wzgledem znakow interpunkcyjnych i 
# zapisz w liscie. Usun spacje wystepujace na poczatku lub koncu 
# otrzymanych napisow.

podziel_na_slowa() {
    local zdanie="$1"
    echo "$zdanie" |  tr '[[:punct:]]' '\n' | awk '{$1=$1};1'
}

test_podziel_na_slowa() {
    local zdanie="hej, pan slimak! tak to ja. chodzcie to zaspiewam wam."
    local wynik=($(podziel_na_slowa "$zdanie"))
    local oczekiwane=(hej pan slimak tak to ja chodzcie zaspiewam wam)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_podziel_na_slowa
}


main "$@"

