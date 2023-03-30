# Tytul: Znalezienie indeksow pierwszej pary elementow listy o sumie rownej podanej liczbie.
# Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz indeksy pierwszej pary elementow listy, ktorych suma jest rowna x. Jesli taka para nie istnieje, zwroc pare (-1, -1).
# Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.
# Dane wyjsciowe: Para liczb calkowitych.
# Przyklad:
# Dla otrzymanej listy: [1, 3, 4, 5, 2] oraz liczby 5, zostana zwrocone indeksy pierwszej pary elementow o sumie rownej 5: (0, 2).

source ../assert.sh

wieksza() {
    local n=${#lista[@]}

    if [ $n -eq 0 ]; then
        echo "0.00"
        return
    fi

    if [ $n -eq 1 ]; then
        echo $((lista[0]- 1))
        return
    fi

    local maks="$((1<<63))"
    local maks2="$((1<<63))"

    for liczba in "${lista[@]}" ; do

        if [ $liczba -gt $maks ]; then
            maks2=$maks;
            maks=$liczba;
        elif  [ $liczba -gt $maks ]; then
            maks2=$liczba
        fi
    done

    echo $(bc -l <<< "scale=2; ($maks+$maks2)/2")
}

main() {
    local lista=(3 5 -7 4 9 -11 2)
    echo $(wieksza)
}

main "$@"

