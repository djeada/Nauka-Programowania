# Tytul: Porownanie ze zmienna.
# Tresc: Pobierz od uzytkownika dwie liczby naturalne i sprawdz, czy sa one identyczne. Wypisz odpowiedni komunikat.
# Dane wejsciowe: Dwie liczby naturalne.
# Dane wyjsciowe: Komunikat.
# Przyklad:
# Dla pobranych liczb: 7 i 4, powinien zostac wypisany komunikat, ze liczby sa rozne.

main() {

    echo "Podaj dwie liczby:"
    read x
    read y

    if [[ $x -eq $y ]]; then
        echo "liczby sa jednakowe"
    else
        echo "liczby sa rozne"
    fi
}

main "$@"

