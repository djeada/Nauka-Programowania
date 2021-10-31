#!/usr/bin/env bash

#Zamien jednostki:
#a) Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.
#b) Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.
#c) Pobierz liczbe sekund i przelicz na godziny.
#d) Pobierz liczbe w euro i wypisz ilu zlotowkom odpowiada. 
#e) Pobierz miare kata w stopniach i wypisz ilu radianom odpowiada.
#f) Pobierz temperature w stopniach Fahrenheita i wypisz ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada. 

main() {

    echo "Podaj liczbe kg: "
    read kg

    echo "$kg kg to  $(($kg * 1000)) g"

    echo "Podaj liczbe cali: "
    read cal

    echo "$cal cali to  $(bc -l <<< $cal/2.54) cm"

    echo "Podaj liczbe sekund: "
    read s

    echo "$s s to  $(($kg / 3600)) h"

    echo "Podaj liczbe euro: "
    read stopnie
    rad=$(echo "$stopnie*0.0174532" | bc)

    echo "$stopnie stopni to $rad radianow"

    echo "Podaj temperature w Fahrenheitach "
    read F

    C=$((($F - 32) * 5 / 9))
    K=$(($C - 273))

    echo "$F to Farenheitow to $C C i $K K"
}

main "$@"

