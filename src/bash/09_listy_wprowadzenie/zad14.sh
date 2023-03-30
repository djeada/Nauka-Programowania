# Tytul: Czy srednia elementow znajduje sie w liscie?
# Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby calkowitej jako klucza, usun pierwsze wystapienie klucza w liscie.
# Dane wejsciowe: Lista liczb calkowitych i liczba calkowita jako klucz.
# Dane wyjsciowe: Lista liczb calkowitych bez pierwszego wystapienia klucza.
# Przyklad:
# Dla otrzymanej listy [6, 2, 1, 4, 27] oraz 4 powinna zostac zwrocona lista [6, 2, 1, 27].

source ../assert.sh

element_bez_pary() {
    wynik=0

    for liczba in "${lista[@]}"; do
        wynik=$((wynik ^ liczba))
    done

    return $wynik
}

test1() {
    local lista=(1 3 1 7 3 1 1)
    local wynik=7
    element_bez_pary
    assertEqual "$?" "$wynik" $LINENO
}

test2() {
    local lista=(2 2 3 3 5 5 4)
    local wynik=4
    element_bez_pary
    assertEqual "$?" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

