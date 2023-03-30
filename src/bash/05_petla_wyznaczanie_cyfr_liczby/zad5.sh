# Czy liczba jest palindromem?
# Tresc: Dla otrzymanej liczby naturalnej sprawdz, czy jest ona palindromem, tj. czy nie zmienia sie po zapisaniu cyfr w odwrotnej kolejnosci.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat.
# Przyklad:
# Dla otrzymanej liczby 13231, powinna zostac wypisana informacja o tym, ze liczba jest palindromem.

main() {

    echo "Podaj liczbe: "
    read a

    pom=$a
    odwrocona=0

    while [ $pom -gt 0 ]
    do
        cyfra=$(($pom % 10))

        odwrocona=$(($odwrocona*10 + $cyfra))
        pom=$(($pom / 10 ))
    done

    if [[ $odwrocona -eq $a ]]; then
        echo "podana liczba jest palindromem"
    else
        echo "podana liczba nie jest palindromem"
    fi
}

main "$@"

