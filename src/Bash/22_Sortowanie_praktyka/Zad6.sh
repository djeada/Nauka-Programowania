#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste liczb, skladajaca sie wylacznie z zer i jedynek. Posortuj liste.

sortuj_liste_binarna() {
    # Sortuj liste binarna.
    local -n _lista_ref="$1"

    local zera=()
    local jedynki=()
    for i in "${_lista_ref[@]}"; do
        if [[ $i == 0 ]]; then
            zera+=("$i")
        else
            jedynki+=("$i")
        fi
    done

    _lista_ref=("${zera[@]}" "${jedynki[@]}")
}

test_sortuj_liste_binarna() {
    local lista=(0 1 1 0 1 0)
    local oczekiwane=(0 0 0 1 1 1)
    sortuj_liste_binarna lista
    assertArrayEqual lista oczekiwane $LINENO
}

main() {
    test_sortuj_liste_binarna
}


main "$@"

