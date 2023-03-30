# Tytul: Wczytaj i wypisz tresc pliku.
# Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego. Wczytaj plik i wypisz jego tresc.
# Dane wejsciowe: Napis reprezentujacy sciezke do pliku.
# Dane wyjsciowe: Napis zawierajacy tresc pliku.

source ../assert.sh

przenies_pliki() {
    local -r from="$1"
    local -r to="$2"
    local -r from_files=$(find "$from" -name "*.csv")

    for file in $from_files; do
        mv "$file" "$to"
    done
}

test_przenies_pliki() {

    mkdir -p 'test1/test1'
    mkdir -p 'test1/test1'
    mkdir -p 'test2/test2'

    sciezki=('test1/test1/test1.csv' 'test1/test1/test2.csv')
    sciezki=('test1/test1/test1.csv' 'test1/test1/test2.csv')
    for plik in ${sciezki[@]}; do
        touch $plik
    done

    przenies_pliki 'test1' 'test2'
    przenies_pliki 'test1' 'test2'

    assertTrue $(if [[ -f 'test2/test1/test1.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertTrue $(if [[ -f 'test2/test1/test1.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertTrue $(if [[ -f 'test2/test1/test2.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertFalse $(if [[ -f 'test1/test1/test1.csv' ]]; then echo true; else echo false; fi) $LINENO
    assertFalse $(if [[ -f 'test1/test1/test2.csv' ]]; then echo true; else echo false; fi) $LINENO

    rm -rf 'test1' 'test2'
    rm -rf 'test1' 'test2'

}

main() {
    test_przenies_pliki
}

main "$@"

