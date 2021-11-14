#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwa napisy reprezentujace sciezki plikow. 
# Podmien tresci obu plikow.

podmien_tresci() {
    local plik_1="$1"
    local plik_2="$2"
    local tmp="$(mktemp)"
    cat "$plik_1" > "$tmp"
    cat "$plik_2" > "$plik_1"
    cat "$tmp" > "$plik_2"
    rm "$tmp"
}

test_podmien_tresci() {

    # stworz folder testowy
    mkdir -p 'test'

    # stworz pliki testowe
    echo 'test1' > 'test/plik_1'	
    echo 'test2' > 'test/plik_2'

    # podmien tresci
    podmien_tresci 'test/plik_1' 'test/plik_2'

    # sprawdz czy pliki zostaly zamienione
    assertEqual $(cat 'test/plik_1') 'test2' $LINENO
    assertEqual $(cat 'test/plik_2') 'test1' $LINENO

    # usun foldery
    rm -rf 'test'

}

main() {
    test_podmien_tresci
}

main "$@"
