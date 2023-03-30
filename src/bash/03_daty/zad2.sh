# Tytul: Czy osoba jest pelnoletnia?
# Tresc: Dla pobranych szesciu liczb: dnia urodzenia osoby, miesiaca urodzenia osoby, roku urodzenia osoby oraz aktualnego dnia, aktualnego miesiaca i aktualnego roku, sprawdz czy dana osoba jest pelnoletnia.
# Dane wejsciowe: 6 liczb.
# Dane wyjsciowe: Komunikat.
# Przyklad:
# Dla pobranych liczb: 5, 12, 1999, 20, 11, 2020, powinna zostac wypisana informacja o pelnoletnosci osoby.

main() {

    echo "Podaj trzy liczby reprezentujace dzien, miesiac i rok urodzenia osoby:"
    read dzien
    read miesiac
    read rok

    echo "Podaj trzy liczby reprezentujace dzisiejsza date:"
    read dzienAktualny
    read miesiacAktualny
    read rokAktualny

    roznicaLata=$(($rokAktualny - $rok))
    roznicaMiesiace=$(($miesiacAktualny - $miesiac))
    roznicaDni=$(($dzienAktualny - $dzien))

    echo $roznicaLata

    if [[ $roznicaLata -gt 18 ]]; then
        echo "osoba jest pelnoletnia"

    elif [[ $roznicaLata -eq 18 ]]; then
        if [[ $roznicaMiesiace -gt 0 ]]; then
            echo "osoba jest pelnoletnia"
        elif [[ $roznicaMiesiace -eq 0 ]]; then
            if [[ $roznicaDni -ge 0 ]]; then
                echo "osoba jest pelnoletnia"
            else
                echo "osoba nie jest pelnoletnia"
            fi
        else
            echo "osoba nie jest pelnoletnia"
        fi
    else
        echo "osoba nie jest pelnoletnia"
    fi
}

main "$@"

