# Tytul: NWD.
# Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych zwroci ich najwiekszy wspolny dzielnik.
# Dane wejsciowe: dwie liczby naturalne
# Dane wyjsciowe: liczba naturalna
# Przyklad:
# Dla otrzymanych liczb 60 i 45, funkcja powinna zwrocic liczbe 15.

source ../assert.sh

nwdV1() {

    a=$1
    b=$2

    if (( $a % $b == 0)); then
        echo $b
    else
        nwdV1 $b $(( $a % $b ))
    fi
}

nwdV2() {

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

test1() {
    test1() {
        a=14
        b=21
        wynik=7
        assert "$wynik -eq $(nwdV1 $a $b)" $LINENO
    }

    test2() {
        a=14
        b=21
        wynik=7
        assert "$wynik -eq $(nwdV2 $a $b)" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

