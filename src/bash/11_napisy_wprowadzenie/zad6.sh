# Tytul: Slowa ze zdania jako osobne elementy listy.
# Tresc: Otrzymujesz napis reprezentujacy zdanie. Zwroc liste slow zdania. Znaki interpunkcyjne nie sa liczone jako slowa.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanego napisu: “Ala ma kota”, powinna zostac zwrocona lista: [“Ala”, “ma”, “kota”].

source ../assert.sh

zamien() {
    sed -r 's/[a]+/?/g' <<< "$1"
}

test1() {
    local napis="pacZka!"
    local wynik="p?cZk?!"
    assertEqual "$(zamien "$napis")" "$wynik" $LINENO
}

main() {
    test1
}

main "$@"

