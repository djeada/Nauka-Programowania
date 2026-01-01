# Tytul: Litera X.
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze litere X o wysokosci rownej tej liczbie.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat.
# Przyklad:
# Dla otrzymanej liczby 4 powinno zostac wypisane:
# *   *
# * *
# * *
# *   *

literaX() {

    a=$1

    for ((i = 0; i < $a; i++)); do
        for ((j = 0; j < $a; j++)); do
            if [ $i -eq $j ] || [ $j -eq $(($a - $i - 1)) ]; then
                echo -n "*"
            else
                echo -n " "
            fi
        done
        echo ""
    done

}

main() {

    literaX 5

}

main "$@"
