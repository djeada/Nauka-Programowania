#!/usr/bin/env bash

source ../assert.sh

# Znajdz permutacje danego slowa bedace palindromami.

permutacje() {
    # Funkcja znajduje wszystkie permutacje dla podanego napisu.
    local napis=$1
    if [ ${#napis} -eq 1 ]; then
        echo "$napis"
        return
    fi

    local permutacje=()

    for ((i=0; i<${#napis}; i++)); do
        for permutacja in $(permutacje ${napis:0:$i}${napis:$((i+1)):${#napis}}); do
            local permutacja="${napis:$i:1}$permutacja"
            if [[ ! " ${permutacje[@]} " =~ " $permutacja " ]] && [ ${#permutacja} -eq ${#napis} ]; then
                permutacje+=("$permutacja")
            fi
        done
    done

    echo "${permutacje[@]}"
}

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

permutacje_palindromiczne(){
    local napis=$1
    for permutacja in $(permutacje "$napis"); do
        if [ $(czy_palindrom "$permutacja") == "true" ]; then
            echo "$permutacja"
        fi
    done
}

test_permutacje_palindromiczne(){
    local wynik=($(permutacje_palindromiczne "adamm"))
    local oczekiwane=("madam" "amdma")
    assertIdenticalElements oczekiwane wynik $LINENO
}

main() {
    test_permutacje_palindromiczne
}


main "$@"

