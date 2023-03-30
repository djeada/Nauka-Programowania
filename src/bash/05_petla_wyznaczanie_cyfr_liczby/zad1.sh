# Tytul: Liczba cyfr.
# Tresc: Dla otrzymanej od uzytkownika liczby naturalnej wypisz liczbe cyfr, z ktorych sie sklada.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla otrzymanej liczby 342, powinna zostac wypisana liczba 3.

main() {

    echo "Podaj liczbe: "
    read a

    licznik=0

    while [ $a -gt 0 ]
    do
        a=$(( $a / 10 ))
        licznik=$(($licznik + 1))
    done

    echo "Podana cyfra sklada sie z $licznik cyfr."

}

main "$@"

