# Tytul: Cyfry liczby spelniajace okreslone warunki.
# Tresc: Dla otrzymanej liczby naturalnej wypisz cyfry tej liczby, ktore sa:
# a) liczbami parzystymi,
# b) mniejsze niz 5,
# c) rozne od 0.
# Dane wejsciowe: Liczba naturalna dla wszystkich podpunktow.
# Dane wyjsciowe: Kilka liczb.
# Przyklad:
# a) Dla otrzymanej liczby 932, powinna zostac wypisana liczba 2.
# b) Dla otrzymanej liczby 101, powinny zostac wypisane liczby 1, 0 i 1.
# c) Dla otrzymanej liczby 650, powinny zostac wypisane liczby 6 i 5.

main() {

    echo "Podaj liczbe: "
    read a

    pom=$a
    echo "Cyfry liczby badace liczbami parzystymi: "

    while [ $pom -gt 0 ]
    do
        cyfra=$(($pom % 10))

        if [[ $(($cyfra % 2)) -eq 0 ]]; then
            echo $cyfra
        fi

        pom=$(( $pom / 10 ))
    done

    pom=$a
    echo "Cyfry liczby mniejsze niz 5: "

    while [ $pom -gt 0 ]
    do
        cyfra=$(($pom % 10))

        if [[ $cyfra -lt 5 ]]; then
            echo $cyfra
        fi

        pom=$(( $pom / 10 ))
    done

    pom=$a
    echo "Cyfry liczby rozne od 0: "

    while [ $pom -gt 0 ]
    do
        cyfra=$(($pom % 10))

        if [[ $cyfra -ne 0 ]]; then
            echo $cyfra
        fi

        pom=$(( $pom / 10 ))
    done

}

main "$@"

