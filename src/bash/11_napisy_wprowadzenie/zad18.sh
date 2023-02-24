#!/usr/bin/env bash

source ../assert.sh

# Odwroc napisy w zdaniu.

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    local wynik=""

    for slowo in "${lista_slow[@]}"; do
        # sparawdz czy napis jest alfanumeryczny
        # i zawiera co najmniej jedna litere
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            local wynik="$wynik$(echo "$slowo" | rev) "
        fi
    done

    if [ ${#wynik} -gt 0 ]; then
        echo "${wynik::-1}"
    else
        echo ""
    fi
}

test1() {
    local napis="Cameron Diaz"
    local wynik="noremaC zaiD"
    assertEqual "$(wypisz_slowa "$napis")" "$wynik" $LINENO
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
