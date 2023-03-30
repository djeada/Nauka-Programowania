# Tytul: Pierwiastek metoda Newtona
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej zwroci jej pierwiastek.
# Dane wejsciowe: liczba naturalna
# Dane wyjsciowe: liczba naturalna
# Przyklad:
# Dla otrzymanej liczby 16, funkcja powinna zwrocic liczbe 4.

source ../assert.sh

pierwiastek() {

    a=$1
    wynik="${a}.0"

    while [ 1 -eq $(echo "$wynik*$wynik - $a > 0.0001" | bc -l) ]; do
        wynik=$(echo "scale=5; ($wynik + $a/$wynik)/2" | bc -l)
    done

    echo ${wynik/.*}
}

test1() {
    test1() {
        a=16
        wynik=4
        assert "$wynik -eq $(pierwiastek $a $b)" $LINENO
    }

    main() {
        test1
    }

    main "$@"

