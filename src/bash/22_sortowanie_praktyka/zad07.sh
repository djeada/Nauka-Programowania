# Tytul: Sortowanie listy binarnej.
# Tresc: Otrzymujesz liste liczb skladajacych sie tylko z zer i jedynek. Posortuj te liste.
# Dane wejsciowe: Lista liczb naturalnych.
# Dane wyjsciowe: Posortowana lista liczb naturalnych.
# Przyklad:
# Dla listy: [1, 0, 1, 0, 1, 1], powinna zostac zwrocona lista: [0, 0, 1, 1, 1, 1].

source ../assert.sh

sortuj_liste() {
    local -n _lista_ref="$1"
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

