#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste napisow. Posortuj wzgledem dlugosci napisy w liscie.

sortuj_wzgledem_dlugosci() {
    local -n _lista_ref="$1"
    echo "${_lista_ref[@]}" | tr " "	"\n"  | awk '{print length($0), $0}' | sort -n -k1,1 | cut -d' ' -f2- | tr "\n" " "	
}

test_sortuj_wzgledem_dlugosci() {
    local lista=(Ala ma kota a kot ma Ale)
    local oczekiwane=(a ma ma Ala Ale kot kota)
    local wynik=$(sortuj_wzgledem_dlugosci lista)
    assertArrayEqual lista oczekiwane wynik
}


main() {
    test_sortuj_wzgledem_dlugosci
}


main "$@"

