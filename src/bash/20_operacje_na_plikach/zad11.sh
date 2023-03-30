# Tytul: Znalezienie sciezki pliku o danej nazwie
# Tresc: Otrzymujesz napis reprezentujacy nazwe pliku. Przeszukaj caly system i zapisz w liscie wszystkie sciezki plikow o podanej nazwie.
# Dane wejsciowe: Napis
# Dane wyjsciowe: Lista napisow

source ../assert.sh

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

    mkdir -p 'test'
    mkdir -p 'test'

    echo 'test1' > 'test/plik_1'
    echo 'test1' > 'test/plik_1'
    echo 'test2' > 'test/plik_2'

    podmien_tresci 'test/plik_1' 'test/plik_2'
    podmien_tresci 'test/plik_1' 'test/plik_2'

    assertEqual $(cat 'test/plik_1') 'test2' $LINENO
    assertEqual $(cat 'test/plik_1') 'test2' $LINENO
    assertEqual $(cat 'test/plik_2') 'test1' $LINENO

    rm -rf 'test'
    rm -rf 'test'

}

main() {
    test_podmien_tresci
}

main "$@"

