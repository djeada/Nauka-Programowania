# Tytul: Litera Z.
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze litere Z o wysokosci rownej tej liczbie.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat.
# Przyklad:
# Dla otrzymanej liczby 5 powinno zostac wypisane:
# *****
# *
# *
# *
# *****

literaZ() {

    a=$1

    for (( i=0; i<$a; i++ )); do
        for (( j=0; j<$a; j++ )); do
            if [ $i -eq 0 ] || [ $i -eq $(($a - 1)) ]; then
                echo -n "*"
            elif [ $j -eq $(($a - $i - 1)) ]; then
                echo -n "*"
            else
                echo -n " "
            fi
        done
        echo ""
    done

}

main() {

    literaZ 5

}

main "$@"

