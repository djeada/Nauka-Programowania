# Tytul: Wczytaj, zmodyfikuj i wypisz.
# Tresc: Wczytaj liczbe calkowita N oraz N liczb calkowitych i umiesc je w liscie. Nastepnie:
# a) Dodaj 1 do kazdego elementu listy.
# b) Pomnoz kazdy element przez jego indeks w liscie (indeksy zaczynaja sie od 0).
# c) Zastap wszystkie elementy wartoscia pierwszego elementu listy.
# Dla kazdego z powyzszych podpunktow wypisz zmodyfikowana liste. Elementy listy powinny byc oddzielone przecinkami i wypisane w jednym wierszu.
# Dane wejsciowe: N oraz N liczb calkowitych.
# Dane wyjsciowe: N liczb calkowitych.
# Przyklad:
# Dla N rownego 3 oraz pobranych liczb 3, 9, 7 w pierwszym podpunkcie powinno zostac wypisana: 4, 10, 8.

source ../assert.sh

odleglosc() {
    local x1=$1
    local y1=$2
    local x2=$3
    local y2=$4
    local roznica_x=$((x1 - x2))
    local roznica_y=$((y1 - y2))
    local suma_kwadratow=$((roznica_x*roznica_x + roznica_y*roznica_y))
    echo "scale=0;sqrt($suma_kwadratow)" | bc
}

czy_trojkat_v1() {

    local odleglosc_ab=$(odleglosc wspl_x[0] wspl_y[0] wspl_x[1] wspl_y[1])
    local odleglosc_bc=$(odleglosc wspl_x[2] wspl_y[2] wspl_x[1] wspl_y[1])
    local odleglosc_ac=$(odleglosc wspl_x[0] wspl_y[0] wspl_x[2] wspl_y[2])

    if [ $((odleglosc_ab + odleglosc_bc)) -gt $odleglosc_ac ] &&
    [ $((odleglosc_ab + odleglosc_ac)) -gt $odleglosc_bc ] &&
    [ $((odleglosc_ac + odleglosc_bc)) -gt $odleglosc_ac ]; then
        echo true
    else
        echo false
    fi
}

czy_trojkat_v2() {

    local wynik=$((wspl_x[0] * (wspl_y[1] - wspl_y[2]) + wspl_x[1] * (wspl_y[2] - wspl_y[0]) +
    wspl_x[2] * (wspl_y[0] - wspl_y[1])))

    if [ $wynik -ne 0 ]; then
        echo true
    else
        echo false
    fi
}

test1() {
    local wspl_x=(2 7 8)
    local wspl_y=(4 5 -8)

    assertTrue "$(czy_trojkat_v1)" $LINENO
}

test2() {
    local wspl_x=(2 7 8)
    local wspl_y=(4 5 -8)

    assertTrue "$(czy_trojkat_v2)" $LINENO
}

test3() {
    local wspl_x=(0 2 5)
    local wspl_y=(0 -2 -5)

    assertFalse "$(czy_trojkat_v1)" $LINENO
}

test4() {
    local wspl_x=(0 2 5)
    local wspl_y=(0 -2 -5)

    assertFalse "$(czy_trojkat_v2)" $LINENO
}

main() {
    test1
    test2
    test3
    test4
}

main "$@"

