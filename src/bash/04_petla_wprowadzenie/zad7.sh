# Tytul: Potega liczby Pi.
# Tresc: Dla otrzymanej liczby naturalnej wypisz liczbe Pi podniesiona do potegi rownej tej liczbie. Wynik powinien zostac zaokraglony do dwoch miejsc po przecinku.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad: Dla otrzymanej liczby 1, powinna zostac wypisana liczba 3,14.

main() {

    echo "Podaj liczbe:"
    read x
    pi=$(echo "scale=2; 4*a(1)" | bc -l)
    potega=$pi

    for (( i=1; i<=$x; i++ )); do
        potega=$(echo "scale=2; $potega * $pi" | bc)
    done

    echo "liczbe Pi podniesiona do potegi rownej pobranej liczbie, wynosi $potega"

}

main "$@"

