# Tytul: Tabliczka mnozenia.
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N pierwszych wierszy i kolumn tabliczki mnozenia.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Wiersze i kolumny tabliczki mnozenia o wymiarach NxN.
# Przyklad:
# Dla otrzymanej liczby 3 powinno zostac wypisane:
# 1 2 3
# 2 4 6
# 3 6 9

tabliczkaMnozenia() {

    a=$1

    for (( i=1; i<=$a; i++ )); do
        for (( j=1; j<=$a; j++ )); do
            echo -n "$(($i * $j)) "
        done
        echo ""
    done

}

main() {

    tabliczkaMnozenia 5

}

main "$@"

