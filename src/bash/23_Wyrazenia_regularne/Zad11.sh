#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz napis reprezentujacy sciezke pliku. Odfiltruj nazwe pliku ze sciezki.
# Zwroc sama nazwe pliku, bez rozszerzen.

nazwa_pliku(){
    local sciezka="$1"
    sciezka="${sciezka//\\//}"
    sciezka="${sciezka%/}"
    sciezka="${sciezka#/}"
    sciezka="${sciezka##*/}"

    while [[ "$sciezka" = *.* ]]; do
        sciezka="${sciezka%.*}"
    done
    
    echo "$sciezka"
}

test_nazwa_pliku() {
    assertEqual $(nazwa_pliku 'C:\\Windows\\explorer.exe') "explorer" $LINENO
    assertEqual $(nazwa_pliku '/home/user/var/log/syslog') "syslog" $LINENO
    assertEqual $(nazwa_pliku 'test.jpg.png.mp3.mp5.html.txt') "test" $LINENO
    assertEqual $(nazwa_pliku 'test') "test" $LINENO
}

main() {
    test_nazwa_pliku
}


main "$@"

