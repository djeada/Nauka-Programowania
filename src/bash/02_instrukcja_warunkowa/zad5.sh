# Tytul: Posortowanie trzech liczb.
# Tresc: Pobierz od uzytkownika trzy liczby naturalne i wypisz je w kolejnosci rosnacej.
# Dane wejsciowe: Trzy liczby naturalne.
# Dane wyjsciowe: Trzy liczby naturalne.
# Przyklad:
# Dla pobranych liczb: 2, 1 oraz 4, powinny zostac wypisane liczby: 1, 2 i 4.

main() {

    echo "Podaj trzy liczby:"
    read a
    read b
    read c

    if [[ $a -ls $b && $a -ls $c ]]; then
        if [[ $b -ls $c ]]; then
            echo $a
            echo $b
            echo $c
        else
            echo $a
            echo $c
            echo $b
        fi

    elif [[ $b -ls $a && $b -ls $c ]]; then
        if [[ $a -ls $c ]]; then
            echo $b
            echo $a
            echo $c
        else
            echo $b
            echo $c
            echo $a
        fi
    else
        if [[ $a -ls $b ]]; then
            echo $c
            echo $a
            echo $b
        else
            echo $c
            echo $b
            echo $a
        fi
    fi
}

main "$@"

