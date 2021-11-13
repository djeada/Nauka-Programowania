#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz dwa napisy reprezentujace sciezki folderow. 
# Skopiuj wszystkie pliki .png z pierwszego folderu do drugiego folderu.

kopiuj_pliki_png() {
    local folder_1="$1"
    local folder_2="$2"

    find "$folder_1" -name "*.png" -exec cp {} "$folder_2" \;
}

test_kopiuj_pliki_png() {

    # stworz foldery testowe
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    # stworz pliki testowe
    touch 'test/test1/plik1.png'
    touch 'test/test1/plik2.png'

    # kopiuj pliki do drugiego folderu
    kopiuj_pliki_png 'test/test1' 'test/test2'

    # sprawdz czy pliki zostaly skopiowane
    assertTrue $(if [[ -f 'test/test2/plik1.png' ]]; then echo 'true'; else echo 'false'; fi) $LINENO
    assertTrue $(if [[ -f 'test/test2/plik2.png' ]]; then echo 'true'; else echo 'false'; fi) $LINENO
    assertTrue $(if [[ -f 'test/test1/plik1.png' ]]; then echo 'true'; else echo 'false'; fi) $LINENO
    assertTrue $(if [[ -f 'test/test1/plik2.png' ]]; then echo 'true'; else echo 'false'; fi) $LINENO

    # usun foldery
    rm -rf 'test'

}

main() {
    test_kopiuj_pliki_png
}

main "$@"
