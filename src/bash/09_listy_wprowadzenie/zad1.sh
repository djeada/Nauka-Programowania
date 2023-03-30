# Tytul: Wczytaj i wypisz.
# Tresc: Dla podanej liczby naturalnej N, wczytaj N liczb calkowitych do listy, a nastepnie:
# a) Wypisz liste od poczatku do konca, z kazdym elementem w osobnym wierszu.
# b) Wypisz liste od konca, z elementami oddzielonymi przecinkami i wypisanymi w jednym wierszu.
# Dane wejsciowe: N liczb calkowitych.
# Dane wyjsciowe: N liczb.
# Przyklad:
# Dla N rownego 3 oraz pobranych liczb: 8, 12, 7, w drugim podpunkcie powinno zostac wypisane: 7, 12, 8.

wczytaj() {

    for (( i=0; i<$1; i++ ))
    do
        read liczba
        lista+=("$liczba")
    done

}

wypisz_od_poczatku() {

    for liczba in "${lista[@]}"
    do
        echo "$liczba"
    done
}

wypisz_od_konca() {

    local n=$(( ${#lista[@]} -1 ))

    for (( i=n; i>=0; i-- ))
    do
        echo "${lista[$i]}"
    done
}

main() {

    declare -a lista
    echo "podaj liczbe n:"
    read n

    echo "podaj $n liczb:"
    wczytaj $n

    echo -e "\nliczby w kolejnosci wczytania:"
    wypisz_od_poczatku

    echo -e "\nliczby wypisane od konca:"
    wypisz_od_konca

}

main "$@"

