# Tytul: NWW.
# Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych zwroci ich najmniejsza wspolna wielokrotnosc.
# Dane wejsciowe: dwie liczby naturalne
# Dane wyjsciowe: liczba naturalna
# Przyklad:
# Dla otrzymanych liczb 7 i 9, funkcja powinna zwrocic liczbe 63.

source ../assert.sh

nwd() {

    a=$1
    b=$2

    while [ $b -ne $(($a % $b)) ]; do
        c=$b
        b=$(($a % $b))
        a=$c

        if (( $b == 0 )); then
            break;
        fi
    done

    echo $a
}

nww() {
    echo $(($a * $b / $(nwd $a $b)))
}

test1() {
    test1() {
        a=14
        b=21
        wynik=42
        assert "$wynik -eq $(nww $a $b)" $LINENO
    }

    main() {
        test1

    }

    main "$@"

