# Tytul: Kwadrat
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze kwadrat o boku rownym tej liczbie.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat.
# Przyklad:
# Dla otrzymanej liczby 2 powinno zostac wypisane:
# **
# **

kwadrat() {

    a=$1

    for (( i=0; i<$a; i++ )); do
        for (( j=0; j<$a; j++ )); do
            echo -n "x"
        done
        echo ""
    done

}

main() {

    kwadrat 5

}

main "$@"

