# Tytul: Porownanie ze stala.
# Tresc: Pobierz od uzytkownika liczbe naturalna. Jesli ta liczba jest wieksza niz 5, wypisz ja.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba naturalna lub brak danych wyjsciowych.
# Przyklad:
# Dla pobranej liczby: 10, powinna zostac wypisana liczba: 10.

main() {

    echo "Podaj liczbe"
    read x

    if [[ $x -gt 5 ]]; then
        echo $x
    fi
}

main "$@"

