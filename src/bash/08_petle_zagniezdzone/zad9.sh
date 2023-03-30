# Tytul: N pierwszych liczb pierwszych.
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N pierwszych liczb pierwszych.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: N liczb pierwszych.
# Przyklad:
# Dla otrzymanej liczby 5 powinno zostac wypisane: 2, 3, 5, 7, 11.

pascal() {

    for (( i=1; i<=$1; i++ ))
    do
        k=1
        for (( j=1; j<=$(($1-$i)); j++ ))
        do
            echo -n " "
        done

        for (( j=1; j<=$i; j++ ))
        do
            echo -n "$k "
            k=$(($k*($i - $j)/$j))
        done
        echo ""
    done
}

main() {

    pascal 5

}

main "$@"

