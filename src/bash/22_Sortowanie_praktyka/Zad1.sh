#!/usr/bin/env bash

source ../assert.sh

# Dla otrzymanego napisu, posortuj alfabetycznie jego znaki.

sortuj_napis() {
    # Funkcja sortuje alfabetycznie napis.
    local napis="$1"
    echo "$napis" |  grep -o . | sort -V | tr -d "\n"
    echo
}

test_sortuj_napis() {
    assertEquals "$(sortuj_napis "Ala ma kota")" "Aaaaklmot  " $LINENO
    assertEquals "$(sortuj_napis "kot ma Ale")" "Aaeklmot  " $LINENO
}

main() {
    test_sortuj_napis
}


main "$@"

