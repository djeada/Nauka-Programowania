#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy zdanie. Znajdz wszystkie palindromy 
# w zdaniu. Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

czy_palindrom() {
    # Funkcja sprawdza czy podany napis jest palindromem.
    local slowo="$1"
    local slowo_odwrocone=$(echo "$slowo" | rev)
    if [ "$slowo" == "$slowo_odwrocone" ]; then
        echo "true"
    else
        echo "false"
    fi
}

wypisz_slowa() {
    # Funkcja rozdziela zdanie na slowa. 
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

palindromy_w_zdaniu() {
    # Funkcja zwraca wszystkie palindromy w zdaniu.
    local zdanie="$1"
    local slowa=$(wypisz_slowa "$zdanie")
    for slowo in $slowa; do
        if [ "$(czy_palindrom "$slowo")" == "true" ]; then
            echo "$slowo"
        fi
    done
}

test_palindromy_w_zdaniu(){
    local wynik=$(palindromy_w_zdaniu "Tata zbaral kajak na wycieczke i uderzyl sie w oko.")
    local oczekiwane=(kajak i w oko)
    assertIdenticalElements wynik oczekiwane $LINENO
}

main() {
    test_palindromy_w_zdaniu
}


main "$@"

