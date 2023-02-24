#!/usr/bin/env bash

# Otrzymujesz napis. Zwroc napis skladajacy sie z cyfr wystepujacych w otrzymanym napisie.


odfiltruj_cyfry() {
    echo "$1" | grep -o '[0-9]'
}

test_odfiltruj_cyfry() {
    assertEqual $(odfiltruj_cyfry "abc123") "123"
    assertEqual $(odfiltruj_cyfry "abc") ""
    assertEqual $(odfiltruj_cyfry "123") "123"
    assertEqual $(odfiltruj_cyfry "3d4jda2") "342"
}

main() {
    test_odfiltruj_cyfry
}


main "$@"

