# Tytul: Podnies a do b.
# Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb obliczy ile wynosi a podniesione do b, przy pomocy petli.
# Dane wejsciowe: dwie liczby naturalne
# Dane wyjsciowe: liczba naturalna
# Przyklad:
# Dla pobranych liczb 3 i 5, funkcja powinna zwrocic liczbe 243.

source ../assert.sh

potega() {

    a=$1
    b=$2
    wynik=1

    for (( i=0; i<$b; i++ )); do
        wynik=$(($wynik * $a))
    done

    echo $wynik
}

main() {
    a=2
    b=3
    wynik=8
    assert "$wynik -eq $(potega $a $b)" $LINENO
}

main "$@"

