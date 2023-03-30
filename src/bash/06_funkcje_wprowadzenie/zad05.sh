# Tytul: Zamien wartosci miejscami.
# Tresc: Napisz funkcje, ktora zamieni wartosci zmiennych a i b miejscami. Po wykonaniu funkcji zmienna a powinna przechowywac wartosc zmiennej b, a zmienna b powinna przechowywac wartosc zmiennej a.
# Dane wejsciowe: Dwie liczby naturalne.
# Dane wyjsciowe: Dwie liczby naturalne.
# Przyklad:
# Dla otrzymanych liczb: 8 i 5, powinny zostac zwrocone liczby 5 i 8.

swapV1() {

    eval "$1=${!2} $2=${!1}"
}

main() {
    echo "Podaj dwie liczby: "
    read a
    read b

    swapV1 a b

    echo "Liczby zamienione miejscami: $a $b"

}

main "$@"

