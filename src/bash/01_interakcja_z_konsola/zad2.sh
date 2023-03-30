# Tytul: Zamiana kolejnosci liczb.
# Tresc zadania: Napisz program, ktory pobierze od uzytkownika dwie liczby naturalne i wypisze je w odwroconej kolejnosci.
# Dane wejsciowe: Dwie liczby naturalne.
# Dane wyjsciowe: Dwie liczby naturalne.
# Przyklad:
# Jesli uzytkownik poda liczby -7 oraz 4, program powinien wypisac liczby: 4 i -7.

main() {
    echo "Wpisz dwie liczby."
    read a
    read b
    echo "Liczby w odwrotnej kolejnosci to: "
    echo "${b}"
    echo "${a}"
}

main "$@"

