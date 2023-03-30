# Tytul: Znak liczby.
# Tresc: Pobierz liczbe naturalna od uzytkownika i sprawdz, czy liczba jest ujemna, dodatnia, czy jest zerem. Wypisz odpowiedni komunikat.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat.
# Przyklad:
# Dla pobranej liczby: 2, powinien zostac wypisany komunikat, ze liczba jest dodatnia.

main() {

    echo "Podaj liczbe:"
    read x

    if [[ $x -gt 0 ]]; then
        echo "Liczba jest dodatnia."
    elif [[ $x -lt 0 ]]; then
        echo "Liczba jest ujemna."
    else
        echo "Liczba jest zerem."
    fi
}

main "$@"

