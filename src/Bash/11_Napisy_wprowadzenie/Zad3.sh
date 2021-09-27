#!/usr/bin/env bash

source ../assert.sh

# Policz z ilu slow sklada sie zdanie.
# Znaki interpunkcyjne nie sa liczone jako slowa.

liczba_slow_v1() {

    local zdanie="$1"
    local licznik=0

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        # sparawdz czy napis jest alfanumeryczny
        # i zawiera co najmniej jedna litere
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            local licznik=$((licznik + 1))
        fi
    done

    echo "$licznik"
}

test1() {
    local zdanie="Ile to   ma :  slow w swoim zdaniu na   koniec?"
    # Lista slow: 'ile', 'to', 'ma', 'slow', 'w', 'swoim', 'zdaniu', 'na', 'koniec'
    local wynik=9
    assertEqual "$(liczba_slow_v1 "$zdanie")" "$wynik" $LINENO
}

test2() {
    local zdanie="to sa cztery slowa"
    # Lista slow: 'to', 'sa', 'cztery', 'slowa'
    local wynik=4
    assertEqual "$(liczba_slow_v1 "$zdanie")" "$wynik" $LINENO
}

test3() {
    local zdanie="31    331 .,,,.,.,brak slow!!!    "
    # Lista slow: 'to', 'sa', 'cztery', 'slowa'
    local wynik=2
    assertEqual "$(liczba_slow_v1 "$zdanie")" "$wynik" $LINENO
}

main() {
    test1
    test2
    test3
}


main "$@"

