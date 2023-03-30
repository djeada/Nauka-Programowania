# Tytul: Liczby mniejsze od podanej liczby.
# Tresc: Dla otrzymanej liczby naturalnej wypisz wszystkie liczby naturalne mniejsze od niej.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczby naturalne.
# Przyklad:
# Dla otrzymanej liczby 3, powinny zostac wypisane liczby 2 i 1.

main() {

    echo "Podaj liczbe:"
    read a

    while [ $a -gt 0 ]; do
        a=$(($a-1))
        echo $a
    done

}

main "$@"

