#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz liste liczb, skladajaca sie wylacznie z zer, 
# jedynek i dwojek. Posortuj liste.

sortuj_liste() {
    # Sortuj liste skladajaca sie z zer, jedynek i dwojek.
    local -n _lista_ref="$1"

    local zera=()
    local jedynki=()
    local dwojki=()
    for i in "${_lista_ref[@]}"; do
        if [[ $i == 0 ]]; then
            zera+=("$i")
        elif [[ $i == 1 ]]; then
            jedynki+=("$i")
        else
            dwojki+=("$i")
        fi
    done

    _lista_ref=("${zera[@]}" "${jedynki[@]}" "${dwojki[@]}")
}

sortuj_liste() {
    local lista=(0 1 1 2 2 0 1 0 2)
    local oczekiwane=(0 0 0 1 1 1 2 2 2)
    sortuj_liste lista
    assertArrayEqual lista oczekiwane $LINENO
}

main() {
    test_sortuj_liste_binarna
}


main "$@"
