# Tytul: Ile dni ma miesiac?
# Tresc: Napisz program, ktory dla pobranej liczby naturalnej bedzie wypisywal liczbe dni w miesiacu odpowiadajacemu tej liczbie. Jesli pobrana liczba nie jest poprawnym numerem miesiaca, program powinien poinformowac o tym uzytkownika.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla pobranej liczby 1, program powinien zwrocic liczbe 31.

main() {

    echo "Podaj numer miesiaca:"
    read dzien

    if [[ dzien -eq 1 ]]; then
        echo "Styczen ma 31 dni"

    elif [[ dzien -eq 2 ]]; then
        echo "Luty ma 28 lub 29 dni"

    elif [[ dzien -eq 3 ]]; then
        echo "Marzec ma 31 dni"

    elif [[ dzien -eq 4 ]]; then
        echo "Kwiecien ma 30 dni"

    elif [[ dzien -eq 5 ]]; then
        echo "Maj ma 31 dni"

    elif [[ dzien -eq 6 ]]; then
        echo "Czerwiec ma 30 dni"

    elif [[ dzien -eq 7 ]]; then
        echo "Lipiec ma 31 dni"

    elif [[ dzien -eq 8 ]]; then
        echo "Sierpien ma 31 dni"

    elif [[ dzien -eq 9 ]]; then
        echo "Wrzesien ma 30 dni"

    elif [[ dzien -eq 10 ]]; then
        echo "Pazdziernik ma 31 dni"

    elif [[ dzien -eq 11 ]]; then
        echo "Listopad ma 30 dni"

    elif [[ dzien -eq 12 ]]; then
        echo "Grudzien ma 31 dni"

    else
        echo "Podano niepoprawny numer miesiaca"
    fi
}

main "$@"

