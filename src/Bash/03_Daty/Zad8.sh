/*
#Niech data bedzie dana w formacie DD/MM/CCYY :
#DD - dzien
#MM - miesiac
#CC - stulecie
#YY - rok

#A = CC/4 - 2*CC - 1
#B = 5*YY/4
#C = 26*(MM + 1)/10

#Dzien = (A + B + C + DD) mod 7

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
