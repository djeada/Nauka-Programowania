#!/usr/bin/env bash

source ../assert.sh

# Znajdz wszystkie wyjatkowe palindromy jakie mozna utworzyc ze znakow w slowie 
# (bez zmiany kolejnosci wystepowania). Nie uwzgledniaj duplikatow w liscie.
# 
# Wyjatkowy palindrom musi spelniac jeden z dwoch warunkow:
# 1. Wszystkie znaki sa identyczne, np. “xxx”.
# 2. Wszystkie znaki poza srodkowym znakiem sa identyczne, np. “ccdcc”.
# 
# Pojedynczy znak jest rowniez uznawany za wyjatkowy palindrom.

wyjatkowy_palindrom() {
    # Funkcja sprawdza czy podany napis jest wyjatkowym palindromem. 
    local slowo="$1"
    
    # sprawdz, czy dlugosc slowa jest rowna 1
    if [ ${#slowo} -eq 1 ]; then
        echo true
        return
    fi 

    # sprawdz czy dlugosc slowa jest nieparzysta
    if [ $((${#slowo} % 2)) -eq 1 ]; then
        local srodek=$(( ${#slowo} / 2 ))
        local slowo="${slowo:0:$srodek}${slowo:$((srodek+1)):$(( ${#slowo} - $srodek - 1 ))}"
    fi

    # sprawdz czy wszystkie litery sa identyczne
    for (( i=1; i<${#slowo}; i++ )); do
        if [ "${slowo:0:1}" != "${slowo:$i:1}" ]; then
            echo false
            return
        fi
    done

    echo true
}

wyjatkowe_palindromy(){
    # Funkcja zwraca wszystkie wyjatkowe palindromy, ktore mozna utworzyc z podnapisow danego napisu. 
    local slowo="$1"

    if [ ${#slowo} -eq 1 ]; then
        echo "$slowo"
        return
    fi

    # znajdz wszystkie podnapisy danego napisu i sprawdz czy sa wyjatkowymi palindromami
    local wynik=()
    for (( i=0; i<${#slowo}; i++ )); do
        for (( j=1; j<=${#slowo}; j++ )); do
            if [ $(wyjatkowy_palindrom ${slowo:$i:$j}) == true ]; then
                if ! [[ " ${wynik[@]} " =~ " ${slowo:$i:$j} " ]]; then
                    wynik+=(${slowo:$i:$j})
                fi
            fi
        done
    done

    echo "${wynik[@]}"
}

test_wyjatkowe_palindromy(){
    local wynik=($(wyjatkowe_palindromy "abc"))
    local oczekiwane=(a b c)
    assertIdenticalElements wynik oczekiwane $LINENO

    local wynik=($(wyjatkowe_palindromy "xxxx"))
    local oczekiwane=(x xx xxx xxxx)
    assertIdenticalElements wynik oczekiwane $LINENO
}

main() {
    test_wyjatkowe_palindromy
}


main "$@"

