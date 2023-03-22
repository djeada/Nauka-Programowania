#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy sciezke folderu. Usun 
# wszystkie pliki o rozmiarach wiekszych niz 10 kB znajdujace 
# sie w podanym folderze oraz jego podfolderach.

usun_pliki_wieksze_niz_10k() {
    local folder=$1
    find $folder -type f -size +10k-exec rm -f {} \;
}

test_usun_pliki_wieksze_niz() {

    # stworz foldery testowe
    mkdir -p 'test/test1'
    mkdir -p 'test/test2'

    # stworz pliki testowe
    sciezki=('test/test1/test1.txt' 'test/test1/test2.txt' 'test/test2/test1.txt' 'test/test2/test2.txt')
    for plik in ${sciezki[@]}; do
        touch $plik
        for i in {1..10000}; do
            echo 'test' >> $plik
        done
    done

    # usun pliki
    usun_pliki_wieksze_niz_10k 'test'

    # sprawdz czy pliki zostaly usuniete
    for plik in ${sciezki[@]}; do
        assertTrue $(if [[ -f $plik ]]; then echo "true"; else echo "false"; fi) $LINENO
    done

    # usun foldery
    rm -rf 'test'

}

main() {
    test_usun_pliki_wieksze_niz
}

main "$@"
