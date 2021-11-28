#!/usr/bin/env bash

source ../assert.sh

# Sprawdz czy slowo jest palindromem. Palindrom to slowo brzmiace tak samo 
# czytane od lewej do prawej i od prawej do lewej.

czy_palindrom() {
    # Funkcja sprawdza czy podany napis jest palindromem.
    local slowo="$1"
    local slowo_odwrocone=$(echo "$slowo" | rev)
    if [ "$slowo" == "$slowo_odwrocone" ]; then
        echo "true"
    else
        echo "false"
    fi
}

test_czy_palindrom(){
    assertTrue "czy_palindrom 'kajak'"
    assertFalse "czy_palindrom 'kot'"
}

main() {
    test_czy_palindrom
}


main "$@"

