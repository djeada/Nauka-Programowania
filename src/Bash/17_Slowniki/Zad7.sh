#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz tekst w postaci napisu. Znajdz czestosc wystepowania kazdego 
# ze slow w tekscie. Zignoruj roznice miedzy malymi i wielkimi literami. 
# Pamietaj, slowa skladaja sie wylacznie z liter.

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

histogram_slow_w_tekscie() {
    local tekst="$1"
    local -A histogram=()
    for slowo in $(wypisz_slowa "$tekst"); do
        ((histogram["$slowo"]++))
    done
    for slowo in ${!histogram[@]}; do
        echo "$slowo: ${histogram[$slowo]};"
    done
}

test_histogram_slow_w_tekscie() {
    local tekst="Ala ma kota."
    local wynik=($(histogram_slow_w_tekscie "$tekst"))
    local oczekiwane=('ala: 1;' 'ma: 1;' 'kota: 1;')
    assertIdenticalElements wynik oczekiwane $LINENO
}

main() {
    test_histogram_slow_w_tekscie
}


main "$@"

