# Tytul: Trojkat prostokatny rownoboczny
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze trojkat prostokatny rownoboczny o wysokosci rownej tej liczbie.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat.
# Przyklad:
# Dla otrzymanej liczby 3 powinno zostac wypisane:
# *
# **
# ***

trojkat() {

    a=$1

    for (( i=0; i<$a; i++ )); do
        for (( j=0; j<=$i; j++ )); do
            echo -n "x"
        done
        echo ""
    done

}

main() {

    trojkat 5

}

main "$@"

