# Tytul: Warunek konczacy petle.
# Tresc: Pros uzytkownika o podanie liczby, dopoki nie zostanie podana liczba 7.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat.

main() {

    a=0

    while [ $a -ne 7 ]; do
        echo "Podaj liczbe:"
        read a
    done

}

main "$@"

