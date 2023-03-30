# Tytul: Zwroc stala.
# Tresc: Napisz funkcje, ktora zwroci:
# a) Liczbe 3.
# b) Napis "Tak".
# c) Wartosc logiczna Prawda.
# Dane wejsciowe: Brak.
# Dane wyjsciowe:
# a) Liczba 3.
# b) Napis "Tak".
# c) Wartosc logiczna Prawda.

funkcja1() {
    return 3
}

funkcja2() {
    echo "Tak"
}

funkcja3() {
    echo true
}

main() {
    funkcja1
    wynik=$?
    echo $wynik

    wynik=$(funkcja2)
    echo $wynik

    wynik=$(funkcja3)
    echo $wynik
}

main "$@"

