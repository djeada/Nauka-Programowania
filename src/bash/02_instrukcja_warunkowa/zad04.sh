# Tytul: Maksimum i minimum z dwoch liczb.
# Tresc: Pobierz od uzytkownika dwie liczby naturalne i wypisz najpierw wieksza, a potem mniejsza.
# Dane wejsciowe: Dwie liczby naturalne.
# Dane wyjsciowe: Dwie liczby naturalne.
# Przyklad:
# Dla pobranych liczb: 1 oraz 4, powinny zostac wypisane liczby: 4 i 1.

main() {

    echo "Podaj dwie liczby:"
    read x
    read y

    if [[ $x -gt $y ]]; then
        echo $x
        echo $y
    else
        echo $y
        echo $x
    fi
}

main "$@"

