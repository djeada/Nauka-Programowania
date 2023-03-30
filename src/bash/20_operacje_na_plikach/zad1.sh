# Tytul: Sprawdzenie, czy sciezka nalezy do pliku/folderu
# Tresc: Otrzymujesz napis reprezentujacy sciezke. Sprawdz, czy jest to sciezka do pliku lub folderu.
# Dane wejsciowe: Napis
# Dane wyjsciowe: Wartosc logiczna

source ../assert.sh

czy_sciezka_pliku() {
    if [ -f "$1" ]; then
        echo true
    else
        echo false
    fi
}

czy_sciezka_folderu() {
    if [ -d "$1" ]; then
        echo true
    else
        echo false
    fi
}

test_czy_sciezka_pliku() {

    mkdir 'test'
    mkdir 'test'

    touch 'test/test.txt'
    touch 'test/test.txt'

    assertTrue "$(czy_sciezka_pliku test/test.txt)" $LINENO
    assertTrue "$(czy_sciezka_pliku test/test.txt)" $LINENO
    assertFalse "$(czy_sciezka_pliku test)" $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

test_czy_sciezka_folderu() {

    mkdir 'test'
    mkdir 'test'

    assertTrue "$(czy_sciezka_folderu test)" $LINENO
    assertTrue "$(czy_sciezka_folderu test)" $LINENO

    rm -rf 'test'
    rm -rf 'test'
}

main() {
    test_czy_sciezka_pliku
    test_czy_sciezka_folderu
}

main "$@"

