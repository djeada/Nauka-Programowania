# Tytul: Srednia dlugosc slow w zdaniu.
# Tresc: Otrzymasz napis reprezentujacy zdanie. Oblicz srednia dlugosc slow w zdaniu. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla otrzymanego napisu: "Zepsuty rower.", powinna zostac zwrocona liczba: 6.

source ../assert.sh

policz_znak_v1() {

    local slowo=$1
    local szukany_znak=$2
    local licznik=0

    while IFS= read -n 1 znak ; do
        if [[ "$znak" == "$szukany_znak" ]]; then
            local licznik=$((licznik+1))
        fi
    done <<< "$1"

    echo $licznik

}

policz_znak_v2() {

    local slowo=$1
    local szukany_znak=$2

    grep -o "$szukany_znak" <<<"$slowo" | grep -c .

}

test1() {
    local napis="adam"
    local znak="a"
    local wynik=2
    assertEqual "$(policz_znak_v1 $napis $znak)" "$wynik" $LINENO
}

test2() {
    local napis="adam"
    local znak="a"
    local wynik=2
    assertEqual "$(policz_znak_v2 $napis $znak)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

