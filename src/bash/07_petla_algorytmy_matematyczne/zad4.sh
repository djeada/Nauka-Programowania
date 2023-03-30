# Tytul: Silnia.
# Tresc: Napisz funkcje, ktora obliczy silnie otrzymanej liczby naturalnej, przy pomocy petli.
# Dane wejsciowe: liczba naturalna
# Dane wyjsciowe: liczba naturalna
# Przyklad:
# Dla otrzymanej liczby 3, funkcja powinna zwrocic liczbe 6.

source ../assert.sh

silnia() {

    a=$1
    wynik=1

    while [ $a -gt 0 ]; do
        wynik=$(($wynik * $a))
        a=$(($a - 1))
    done

    echo $wynik
}

test1() {
    test1() {
        a=0
        wynik=1
        assert "$wynik -eq $(silnia $a $b)" $LINENO
    }

    test2() {
        a=4
        wynik=24
        assert "$wynik -eq $(silnia $a $b)" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

