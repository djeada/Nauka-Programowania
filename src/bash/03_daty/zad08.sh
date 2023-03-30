# Tytul: Ile dni minelo od poczatku roku?
# Tresc: Dla trzech pobranych liczb: reprezentujacych date wypisz, ile dni minelo od poczatku roku. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.
# Dane wejsciowe: Liczba naturalna.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad: Dla pobranych liczb: 14, 2 oraz 1482, powinna zostac zwrocona liczba 45. **

main() {

    echo "Podaj dzien:"
    read DD

    echo "Podaj miesiac:"
    read MM

    echo "Podaj rok:"
    read rok

    CC=$(($rok/100))
    YY=$(($rok % 100))

    A=$((($CC/4) - 2*$CC - 1))
    B=$((5*$YY/4))
    C=$((26*($MM+1)/10))

    wynik=$((($A + $B + $C + $DD) % 7))

    if [[ $wynik -eq 1 ]]; then
        echo "poniedzialek"

    elif [[ $wynik -eq 2 ]]; then
        echo "wtorek"

    elif [[ $wynik -eq 3 ]]; then
        echo "sroda"

    elif [[ $wynik -eq 4 ]]; then
        echo "czwartek"

    elif [[ $wynik -eq 5 ]]; then
        echo "piatek"

    elif [[ $wynik -eq 6 ]]; then
        echo "sobota"

    elif [[ $wynik -eq 7 ]]; then
        echo "niedziela"

    else
        echo "bledne dane"

    fi
}

main "$@"

