# Tytul: Wypisanie elementow dwoch list na przemian.
# Tresc: Dla otrzymanych dwoch list, wypisuj na przemian elementy z obu list. Jesli listy nie sa tej samej dlugosci, po wyczerpaniu elementow krotszej listy, wypisuj pozostale elementy dluzszej listy.
# Dane wejsciowe: Dwie listy.
# Dane wyjsciowe: Kilka liczb.
# Przyklad:
# Dla otrzymanych list [5, 3, 7, 2] oraz [1, -2, 3], zostana wypisane: 5, 1, 3, -2, 7, 3, 2.

wypisz() {

    local n=$(( ${#lista_a[@]} ))
    local m=$(( ${#lista_b[@]} ))
    local min_dlugosc=$((n<m ? n : m))

    for (( i=0; i<min_dlugosc; i++ ))
    do
        echo -n "${lista_a[$i]}, "
        echo -n "${lista_b[$i]}, "
    done

    for (( i=min_dlugosc; i<n; i++ ))
    do
        echo -n "${lista_a[$i]}, "
    done

    for (( i=min_dlugosc; i<m; i++ ))
    do
        echo -n "${lista_b[$i]}, "
    done

    echo
}

main() {

    lista_a=(5 3 7 2)
    lista_b=(1 -2 3)

    wypisz

}

main "$@"

