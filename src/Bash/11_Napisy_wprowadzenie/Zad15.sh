#!/usr/bin/env bash

source ../assert.sh

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        # sparawdz czy napis jest alfanumeryczny
        # i zawiera co najmniej jedna litere
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            echo "$slowo" | tr '[:upper:]' '[:lower:]'
        fi
    done

}

test1() {
    local napis="We think in generalities, but we live in details"
    local oczekiwane=('we' 'think' 'in' 'generalities' 'but' 'we' 'live' 'in' 'details')
    readarray -t wynik <<< "$(wypisz_slowa "$napis")"
    assertArrayEqual wynik oczekiwane $LINENO
}

test2() {
    local napis=""
    local wynik=""
    assertEqual "$(wypisz_slowa "$napis")" "$wynik" $LINENO
}

main() {
    test1
    test2
}


main "$@"

