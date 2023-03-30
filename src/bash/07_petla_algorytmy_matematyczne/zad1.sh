# Tytul: Srednia z n liczb
# Tresc: Napisz funkcje, ktora dla otrzymanej liczby n, poprosi uzytkownika o podanie n liczb i zwroci ich srednia arytmetyczna.
# Dane wejsciowe: liczba naturalna n oraz n liczb
# Dane wyjsciowe: liczba naturalna
# Przyklad:
# Dla pobranych liczb 2, 4 i 6, funkcja powinna zwrocic liczbe 4.

srednia() {

    n=$1
    suma=0

    for (( i=0; i<$n; i++ )); do
        read x
        suma=$(($suma + $x))
    done

    wynik=$(bc -l <<< "scale=2; $suma/$n")

    echo $wynik
}

main() {
    echo "Podaj liczbe n: "
    read n

    echo "Wprowadz $n liczb: "
    wynik=$(srednia $n)
    echo "srednia arytmetyczna z podanych liczb: $wynik"
}

main "$@"

