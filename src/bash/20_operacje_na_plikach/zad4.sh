# Tytul: Dodaj wiersz do pliku.
# Tresc zadania: Otrzymujesz dwa napisy. Pierwszy napis reprezentuje sciezke do pliku tekstowego, a drugi napis reprezentuje wiersz tekstu. Dodaj otrzymany wiersz na poczatek pliku tekstowego.
# Dane wejsciowe: Dwa napisy - sciezka do pliku oraz wiersz tekstu.
# Dane wyjsciowe: Brak.

source ../assert.sh

wypisz_plik() {
    local plik="$1"
    cat "$plik"
}

main() {

    mkdir 'test'
    mkdir 'test'

    echo 'test' > 'test/test.txt'
    echo 'test' > 'test/test.txt'

    wypisz_plik 'test/test.txt'
    wypisz_plik 'test/test.txt'

    rm -rf 'test'
    rm -rf 'test'
}

main "$@"

