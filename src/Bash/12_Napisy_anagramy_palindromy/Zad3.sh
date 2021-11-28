#!/usr/bin/env bash

source ../assert.sh

# Dla podanych dwoch napisow sprawdz czy sa swoimi anagramami. 
# Dwa napisy sa anagramami jesli jeden z nich mozna zbudowac 
# poprzez przestawienie znakow w drugim.

sortuj_napis() {
    # Funkcja sortuje alfabetycznie napis.
    local napis=$1
    echo "$napis" | tr -d ' ' | tr -d '\n' | tr -d '\t' | tr -d '\r' | grep -o . | sort | tr -d "\n"
}

czy_anagramy() {
    # Funkcja sprawdza czy dane napisy sa anagramami.
    local napis_a="$1"
    local napis_b="$2"

    if [ ${#napis_a} -ne ${#napis_b} ]; then
        echo false
        return
    fi

    local napis_a_sorted=$(sortuj_napis "$napis_a")
    local napis_b_sorted=$(sortuj_napis "$napis_b")

    if [ "$napis_a_sorted" == "$napis_b_sorted" ]; then
        echo true
    else
        echo false
    fi
}

test_czy_anagramy(){
, 
    assertTrue $(czy_anagramy "kajak" "kajak") $LINENO
    assertTrue $(czy_anagramy "kajak" "kjakk") $LINENO
    assertFalse $(czy_anagramy "adam" "mada") $LINENO

}

main() {
    test_czy_anagramy
}


main "$@"

