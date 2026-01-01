# Tytul: Choinka.
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N trojkatow ustawionych w kolumnie, jeden na drugim. Wysokosc pierwszego trojkata to 1, a kazdego nastepnego jest rowna wysokosci poprzedniego powiekszonej o 1.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat.
# Przyklad:
# Dla otrzymanej liczby 3 powinno zostac wypisane:
# *
# *
# **
# *
# **
# ***

trojkat() {

    a=$1

    for ((i = 0; i < $a; i++)); do
        for ((j = 0; j <= $i; j++)); do
            echo -n "x"
        done
        echo ""
    done

}

choinka() {

    n=$1

    for ((i = 1; i <= $n; i++)); do
        trojkat $i
    done

}

main() {

    choinka 5

}

main "$@"
