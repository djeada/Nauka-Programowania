# Tytul: Operacje arytmetyczne.
# Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci:
# a) Ich sume.
# b) Roznice drugiej i pierwszej.
# c) Ich iloczyn.
# d) Iloraz pierwszej przez druga.
# e) Reszte z dzielenia pierwszej przez druga.
# Dane wejsciowe: Dwie liczby naturalne dla wszystkich podpunktow.
# Dane wyjsciowe: Liczba calkowita dla wszystkich podpunktow.
# Przyklad:
# Dla pobranych liczb: 3 i 5, funkcja powinna zwrocic:
# a) Sume: 8
# b) Roznice: 2
# c) Iloczyn: 15
# d) Iloraz: 0
# e) Reszte z dzielenia: 3

suma() {
    return $(($1 + $2))
}

roznica() {
    return $(($2 - $1))
}

iloczyn() {
    return $(($1 * $2))
}

reszta() {
    return $(($2 % $1))
}

main() {
    echo "Podaj dwie liczby: "
    read a
    read b

    suma $a $b
    wynik=$?
    echo "suma liczb to $wynik"

    roznica $a $b
    wynik=$?
    echo "iloczyn liczb to $wynik"

    iloczyn $a $b
    wynik=$?
    echo "suma liczb to $wynik"

    reszta $a $b
    wynik=$?
    echo "reszte z dzielenia pierwszej przez druga to $wynik"
}

main "$@"

