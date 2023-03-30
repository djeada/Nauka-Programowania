# Tytul: Cyfry liczby
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby obliczy sume jej cyfr.
# Dane wejsciowe: liczba naturalna
# Dane wyjsciowe: liczba naturalna
# Przyklad:
# Dla pobranej liczby 13231, funkcja powinna zwrocic liczbe 10.

sumaCyfr() {

    a=$1
    suma=0

    while [ $a -gt 0 ]
    do
        suma=$(($suma + $a % 10))
        a=$(( $a / 10 ))
    done

    return $suma
}

main() {
    echo "Podaj liczbe: "
    read a

    sumaCyfr $a
    wynik=$?

    echo "Suma cyfr twojej liczby: $wynik"

}

main "$@"

