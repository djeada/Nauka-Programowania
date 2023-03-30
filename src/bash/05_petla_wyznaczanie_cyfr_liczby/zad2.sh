# Tytul: Cyfry liczby.
# Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry, z ktorych sie sklada, zaczynajac od cyfry jednosci.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczby.
# Przyklad:
# Dla otrzymanej liczby 8214, powinny zostac wypisane cyfry 4, 1, 2 i 8.

main() {

    echo "Podaj liczbe: "
    read a

    while [ $a -gt 0 ]
    do
        echo $(($a % 10))
        a=$(( $a / 10 ))
    done

}

main "$@"

