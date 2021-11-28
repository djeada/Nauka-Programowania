#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy zdanie. Znajdz najczesciej wystepujaca litere 
# w zdaniu. Jesli wiecej niz jedna litera wystepuje ta sama liczbe razy, zwroc 
# litere najwczesniej pojawiajaca sie w zdaniu.

najczesciej_wystepujaca_litera() {
    local zdanie="$1"

    # usun znaki interpunkcyjne
    local zdanie=$(echo "$zdanie" | tr -d ' .,:;!?\n')

    # zbuduj histogram wystapien liter w zdaniu
    local -A histogram=()
    for (( i=0; i<${#zdanie}; i++ )); do
        ((histogram["${zdanie:$i:1}"]++))
    done
 
    # znajdz maksymalna ilosc wystapien litery w zdaniu
    local maks=0
    for litera in ${!histogram[@]}; do
        if [[ "${histogram[$litera]}" -gt "$maks" ]]; then
            maks="${histogram[$litera]}"
        fi
    done

    # Przejdz przez litery w zdaniu i sprawdz ktora jako 
    # pierwsza wystepuje maks razy
    for (( i=0; i<${#zdanie}; i++ )); do
        if [[ "${histogram[${zdanie:$i:1}]}" -eq "$maks" ]]; then
            echo "${zdanie:$i:1}"
            break
        fi
    done
}

test_najczesciej_wystepujaca_litera() {

    assertEqual "$(najczesciej_wystepujaca_litera "Ala ma kota")" "a" $LINENO

}

main() {
    test_najczesciej_wystepujaca_litera
}


main "$@"

