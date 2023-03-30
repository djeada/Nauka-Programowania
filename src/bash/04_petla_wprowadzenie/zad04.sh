# Tytul: Suma liczb mniejszych od podanej.
# Tresc: Dla otrzymanej liczby naturalnej wypisz sume wszystkich liczb naturalnych mniejszych od niej.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba.
# Przyklad:
# Dla otrzymanej liczby 5, powinna zostac wypisana liczba 10.

main() {

    echo "Podaj liczbe:"
    read a
    suma=0

    for (( i=0; i<$a; i++ ))
    do
        echo $i
        suma=$(($suma + $i))
    done

    echo "Suma liczb naturalnych mniejszych od pobranej liczby wynosi $suma"
}

main "$@"

