# Tytul: Maks i min
# Napisz funkcje, ktora:
# a) Dla otrzymanych dwoch liczb zwroci mniejsza.
# b) Dla otrzymanych dwoch liczb zwroci wieksza.
# c) Dla otrzymanych trzech liczb zwroci najmniejsza.
# d) Dla otrzymanych trzech liczb zwroci najwieksza.
# Dane wejsciowe:
# a) Dwie liczby naturalne.
# b) Dwie liczby naturalne.
# c) Trzy liczby naturalne.
# d) Trzy liczby naturalne.
# Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.
# Przyklad:
# a) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 1.
# b) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrocic liczbe 3.
# c) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 1.
# d) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrocic liczbe 3."

min2() {

    if [[ $1 -lt $2 ]] ; then
        return $1
    else
        return $2
    fi
}

maks2() {

    if [[ $1 -gt $2 ]] ; then
        return $1
    else
        return $2
    fi
}

min3() {
    if [[ $1 -le $2 && $1 -le $3 ]]; then
        return $1
    elif [[ $2 -le $1 && $2 -le $3 ]]; then
        return $2
    else
        return $3
    fi
}

maks3() {
    if [[ $1 -ge $2 && $1 -ge $3 ]]; then
        return $1
    elif [[ $2 -ge $1 && $2 -ge $3 ]]; then
        return $2
    else
        return $3
    fi
}

main() {
    echo "Podaj dwie liczby: "
    read a
    read b

    min2 $a $b
    wynik=$?
    echo "mniejsza liczba to $wynik"

    maks2 $a $b
    wynik=$?
    echo "wieksza liczba to $wynik"

    echo "Podaj trzy liczby: "
    read a
    read b
    read c

    min3 $a $b $c
    wynik=$?
    echo "najmniejsza liczba to $wynik"

    maks3 $a $b $c
    wynik=$?
    echo "najwieksza liczba to $wynik"

}

main "$@"

