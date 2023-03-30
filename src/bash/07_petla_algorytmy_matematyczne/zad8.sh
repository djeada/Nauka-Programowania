# Tytul: Naiwny test pierwszosci
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej sprawdzi, czy jest ona liczba pierwsza.
# Dane wejsciowe: liczba naturalna
# Dane wyjsciowe: wartosc logiczna
# Przyklad:
# Dla otrzymanej liczby 7, funkcja powinna zwrocic wartosc logiczna prawda. Dla otrzymanej liczby 2, funkcja powinna zwrocic wartosc logiczna prawda.

source ../assert.sh

czyPierwsza() {

    a=$1

    if [[ $a -lt 2 ]]; then
        echo false
        return
    fi

    if [[ $a -eq 2 ]] || [[ $a -eq 3 ]]; then
        echo true
        return
    fi

    if [[ $(($a % 2)) -eq 0 ]] || [[ $(($a % 3)) -eq 0 ]]; then
        echo false
        return
    fi

    i=3

    while [[ $((i * i)) -le $a ]]; do

        if [[ $(($a % i)) -eq 0 ]]; then
            echo false
            return
        fi

        i=$((i + 2))
    done

    echo true
    return
}

test1() {
    test1() {
        a=7
        assertTrue "$(czyPierwsza $a)" $LINENO
    }

    test2() {
        a=4
        assertFalse "$(czyPierwsza $a)" $LINENO
    }

    test3() {
        a=1
        assertTrue "$(czyPierwsza $a)" $LINENO
    }

    main() {
        test1
        test2
        test3
    }

    main "$@"

