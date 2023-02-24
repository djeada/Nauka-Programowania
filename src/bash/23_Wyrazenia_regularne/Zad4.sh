#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwa napisy. Sprawdz czy drugi napis wystepuje w pierwszym napisie.


czy_podnapis() {
    local napis_a="$1"
    local napis_b="$2"

    if [[ $napis_a =~ $napis_b ]]; then
        echo "true"
    else
        echo "false"
    fi
}


test_czy_podnapis() {
    assertTrue $(czy_podnapis "abcdef" "cde") $LINENO
    assertTrue $(czy_podnapis "abcdef" "cdef") $LINENO
    assertFalse $(czy_podnapis "abcdef" "cdefg") $LINENO
    assertFalse $(czy_podnapis "abcdef" "abca") $LINENO
}

main() {
    test_czy_podnapis
}


main "$@"

