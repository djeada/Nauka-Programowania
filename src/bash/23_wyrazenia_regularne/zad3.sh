#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis. Sprawdz, czy napis sklada sie wylacznie z cyfr.


wylacznie_cyfry() {
    local napis=$1
    
    if [[ $napis =~ ^[0-9]+$ ]]; then
        echo "true"
    else
        echo "false"
    fi
}

test_wylacznie_cyfry() {
    assertTrue $(wylacznie_cyfry "123") $LINENO
    assertTrue $(wylacznie_cyfry "12345") $LINENO
    assertFalse $(wylacznie_cyfry "123a") $LINENO
    assertFalse $(wylacznie_cyfry "a123") $LINENO
}

main() {
    test_wylacznie_cyfry
}


main "$@"

