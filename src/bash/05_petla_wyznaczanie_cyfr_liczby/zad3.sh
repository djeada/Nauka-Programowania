# Tytul: Tresc: Dla otrzymanej liczby naturalnej wypisz sume cyfr tej liczby.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla otrzymanej liczby 129, powinna zostac wypisana liczba 12.

main() {

    echo "Podaj liczbe: "
    read a

    suma=0

    while [ $a -gt 0 ]
    do
        suma=$(($suma + $a % 10))
        a=$(( $a / 10 ))
    done

    echo "Suma cyfr podanej liczby wynosi $suma."
}

main "$@"

