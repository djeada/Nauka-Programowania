#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwa napisy reprezentujace sciezki folderow. Przenies wszystkie pliki 
# csv z pierwszego folderu (oraz wszystkich jego podfolderow) do drugiego folderu.

przenies_pliki() {
    local -r from="$1"
    local -r to="$2"
    local -r from_files=$(find "$from" -name "*.csv")

    for file in $from_files; do
        mv "$file" "$to"
    done
}

test_przenies_pliki() {

    # stworz foldery testowe
    mkdir -p 'test1/test1'
    mkdir -p 'test2/test2'

    # stworz pliki testowe
    sciezki=('test1/test1/test1.csv' 'test1/test1/test2.csv')
    for plik in ${sciezki[@]}; do
        touch $plik
    done

    # przenies pliki
    przenies_pliki 'test1' 'test2'

    # sprawdz czy pliki zostaly przeniesione
    assertTrue $(if [[ -f 'test2/test1/test1.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertTrue $(if [[ -f 'test2/test1/test2.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertFalse $(if [[ -f 'test1/test1/test1.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertFalse $(if [[ -f 'test1/test1/test2.csv' ]]; then echo true; else echo false; fi) $LINENO

    # usun foldery
    rm -rf 'test1' 'test2'

}

main() {
    test_przenies_pliki
}

main "$@"
