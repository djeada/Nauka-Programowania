# Tytul: Maks z czterech liczb.
# Tresc: Dla czterech pobranych liczb naturalnych, wypisz najwieksza z nich.
# Dane wejsciowe: Cztery liczby naturalne.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla pobranych liczb: 2, 5, 1 i 4, powinna zostac wypisana liczba: 5.

main() {

    echo "Podaj cztery liczby."
    read a
    read b
    read c
    read d

    maxAB=$([ $a -gt $b ] && echo "$a" || echo "$b")
    maxCD=$([ $c -gt $d ] && echo "$c" || echo "$d")
    max=$([ $maxAB -gt $maxCD ] && echo "$maxAB" || echo "$maxCD")

    echo $max
}

main "$@"

