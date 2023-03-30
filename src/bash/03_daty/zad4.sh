# Tytul: Dzien tygodnia odpowiadajacy danej liczbie.
# Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie wypisywal dzien tygodnia odpowiadajacy tej liczbie. Jesli otrzymano liczbe niedodatnia badz dodatnia wieksza niz 7, program powinien wypisac komunikat informujacy uzytkownika, ze liczba jest niepoprawna.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Komunikat o dniu tygodnia.
# Przyklad:
# Dla pobranej liczby 2, program powinien wypisac napis "Wtorek".

main() {

    echo "Podaj numer dnia tygodnia:"
    read dzien

    if [[ dzien -eq 1 ]]; then
        echo "pierwszym dniem tygodnia jest poniedzialek"

    elif [[ dzien -eq 2 ]]; then
        echo "drugim dniem tygodnia jest wtorek"

    elif [[ dzien -eq 3 ]]; then
        echo "trzecim dniem tygodnia jest sroda"

    elif [[ dzien -eq 4 ]]; then
        echo "czwartym dniem tygodnia jest czwartek"

    elif [[ dzien -eq 5 ]]; then
        echo "piatym dniem tygodnia jest piatek"

    elif [[ dzien -eq 6 ]]; then
        echo "szostym dniem tygodnia jest sobota"

    elif [[ dzien -eq 7 ]]; then
        echo "siodmym dniem tygodnia jest niedziela"

    else
        echo "podano niepoprawna liczbe"
    fi
}

main "$@"

