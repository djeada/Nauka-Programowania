#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis. Znajdz czestosc wystepowania znakow w otrzymanym 
# napisie. Inaczej, zwroc histogram znakow w otrzymanym napisie.


histogram_znakow() {
    local napis=$1
    local -A histogram=()
    for (( i=0; i<${#napis}; i++ )); do
        ((histogram["${napis:$i:1}"]++))
    done
    for znak in ${!histogram[@]}; do
        echo "$znak: ${histogram[$znak]};"
    done
}

test_histogram_znakow() {
    local napis="ala ma kota"
    local wynik=($(histogram_znakow "$napis"))
    local oczekiwane=(a:4; l:1; m:1; k:1; o:1; t:1)
    assertIdenticalElements wynik oczekiwane $LINENO
}

main() {
    test_histogram_znakow
}

main "$@"
