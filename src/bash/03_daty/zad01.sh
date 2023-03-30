# Tytul: Czy liczba jest poprawnym numerem dnia tygodnia lub miesiaca?
# Tresc: Wypisz pobrana od uzytkownika liczbe naturalna, jesli jest ona poprawnym numerem dnia tygodnia lub miesiaca.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# * Dla pobranej liczby: 10, powinna zostac wypisana liczba: 10.
# * Dla pobranej liczby: 15, nie powinna byc wypisana zadna liczba.

main() {

    echo "Podaj liczbe:"
    read a

    if [[ $a -ge 1 ]] && [[ $a -le 7 ]]; then
        echo "Liczba jest poprawnym numerem tygodnia"

    else
        echo "Liczba nie jest poprawnym numerem tygodnia"
    fi

    if [[ $a -ge 1 ]] && [[ $a -le 12 ]]; then
        echo "Liczba jest poprawnym numerem miesiaca"
    else
        echo "Liczba nie jest poprawnym numerem miesiaca"
    fi
}

main "$@"

