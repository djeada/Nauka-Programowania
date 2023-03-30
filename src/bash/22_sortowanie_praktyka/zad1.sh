# Tytul: Sortowanie znakow w napisie.
# Tresc: Otrzymujesz napis. Posortuj alfabetycznie jego znaki.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Napis.
# Przyklad:
# Dla napisu "Ala ma kota" powinno zostac zwrocone " Aaaaklmot".

source ../assert.sh

sortuj_napis() {
    local napis="$1"
    local napis="$1"
    echo "$napis" |  grep -o . | sort -V | tr -d "\n"
    echo
}

test_sortuj_napis() {
    assertEquals "$(sortuj_napis "Ala ma kota")" "Aaaaklmot  " $LINENO
    assertEquals "$(sortuj_napis "kot ma Ale")" "Aaeklmot  " $LINENO
}

main() {
    test_sortuj_napis
}

main "$@"

