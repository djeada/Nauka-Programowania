# Tytul: Sortowanie listy miast.
# Tresc: Klasa Miasto ma dwie wlasciwosci: nazwa (napis) oraz liczba_mieszkancow (liczba naturalna). Posortuj liste miast wzgledem nazwy oraz wzgledem liczby mieszkancow.
# Dane wejsciowe: Lista miast.
# Dane wyjsciowe: Posortowana lista miast.
# Przyklad:
# Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostac zwrocona lista: [Miasto("Berlin", 3800000), Miasto("New York", 8400000), Miasto("Paris", 2150000)].
# Dla listy miast: [Miasto("Paris", 2150000), Miasto("Berlin", 3800000), Miasto("New York", 8400000)], powinna zostac zwrocona lista: [Miasto("Berlin", 3800000), Miasto("Paris", 2150000), Miasto("New York", 8400000)].

source ../assert.sh

sortuj_liste_binarna() {
    local -n _lista_ref="$1"
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

