# Tytul: Sortowanie slow w zdaniu.
# Tresc: Masz dany napis reprezentujacy zdanie. Podziel to zdanie na slowa, posortuj je alfabetycznie i zapisz w liscie. Znaki interpunkcyjne nie sa liczone jako slowa.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla napisu "Lemur wygina smialo cialo" powinno zostac zwrocone ["Lemur", "cialo", "smialo", "wygina"].

source ../assert.sh

sortuj_slowa_w_zdaniu() {
    local zdanie="$1"
    local zdanie="$1"
    zdanie="${zdanie//[,.:;?!]/}"
    echo "$zdanie" | tr " "	"\n"  | sort -V | tr "\n" " "
}

test_sortuj_slowa_w_zdaniu() {
    local wynik=($(sortuj_slowa_w_zdaniu "Lemur wygina smialo cialo"))
    local oczekiwane=(Lemur cialo smialo wygina)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_sortuj_slowa_w_zdaniu
}

main "$@"

