#!/usr/bin/env bash

source ../assert.sh

# Dla dwoch slow, ile minimalnie znakow musimy usunac aby uzyskac anagramy.
# Zwroc -1 dla slow o roznych dlugosciach.

liczba_znakow(){
    local slowo_a="$1"
    local slowo_b="$2"
    if [ ${#slowo_a} -ne ${#slowo_b} ]; then
        echo -1
        return
    fi

    local pom=()
    for ((i=0; i<256; i++)); do
        pom[i]=0
    done

    for (( i=0; i<${#slowo_a}; i++ )); do
        local litera=${slowo_a:$i:1}
        local ascii=$(echo -n "$litera" | od -An -N1 | bc)
        pom[$ascii]=$((${pom[$ascii]} + 1)) 
    done

    for (( i=0; i<${#slowo_b}; i++ )); do
        local litera=${slowo_b:$i:1}
        local ascii=$(echo -n "$litera" | od -An -N1 | bc)
        pom[$ascii]=$((${pom[$ascii]} - 1)) 
    done

    local licznik=0
    for (( i=0; i<256; i++ )); do
        licznik=$(($licznik + ${pom[$i]}))
    done

    echo $licznik
}

test_liczba_znakow() {
    assertEquals "liczba_znakow 'kajak' 'kajak'" 0 $LINENO
    assertEquals "liczba_znakow 'kajak' 'kjakk'" 1 $LINENO
    assertEquals "liczba_znakow 'pan cytryna' 'pan pomarancza'" -1 $LINENO
}

main() {
    test_liczba_znakow
}


main "$@"

