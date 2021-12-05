#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy haslo. Sprawdz czy 
# haslo spelnia nastepujace warunki:
# 1. Haslo musi zawierac przynajmniej jedna mala litere [a-z].
# 2. Haslo musi zawierac przynajmniej jedna duza litere [A-Z].
# 3. Haslo musi zawierac przynajmniej jedna cyfre [0-9].
# 4. Haslo musi zawierac przynajmniej jeden znak specjalny 
# [! # $ % & ' * + - / = ? ^ _ ` { | } ~].
# 5. Minimalna dlugosc hasla to 8 znakow.
# 6. Maksymalna dlugosc hasla to 20 znakow.

czy_haslo_poprawne() {
    local haslo=$1
    
    if [[ ${#haslo} -lt 8 || ${#haslo} -gt 20 ]]; then
        echo "false"
        return
    elif [[ ! $(echo $haslo | grep -E '[a-z]') ]]; then
        echo "false"
        return
    elif [[ ! $(echo $haslo | grep -E '[A-Z]') ]]; then
        echo "false"
        return
    elif [[ ! $(echo $haslo | grep -E '[0-9]') ]]; then
        echo "false"
        return
    elif [[ ! $(echo $haslo | grep -E '[! \# $ % & \\'' * + - / = ? ^ _ \` { | } ~]') ]]; then
        echo "false"
        return
    fi

    echo "true"
}

test_czy_haslo_poprawne() {
    assertFalse "$(czy_haslo_poprawne 'Ab1!')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'haslo')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'HASLO')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'HASLO123!@#')" $LINENO
    assertFalse "$(czy_haslo_poprawne '12345678')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'proste_haslo')" $LINENO
    assertFalse "$(czy_haslo_poprawne 'Haslo123')" $LINENO
    assertTrue "$(czy_haslo_poprawne 'Haslo123!')" $LINENO
    assertTrue "$(czy_haslo_poprawne 'Haslo123!#')" $LINENO
    assertTrue "$(czy_haslo_poprawne 'Haslo123!#$')" $LINENO
    assertTrue "$(czy_haslo_poprawne 'Haslo123!#$%&*')" $LINENO
}

main() {
    test_czy_haslo_poprawne
}


main "$@"

