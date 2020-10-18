#!/usr/bin/env bash

main() {
	    
	#Pobierz wielkosc w kilogramach i wypisz ilu gramom odpowiada.

    echo "Podaj liczbe kg: "
    read kg

    echo "$kg kg to  $(($kg * 1000)) g"	
    	       
	#Pobierz wielkosc w calach i wypisz ilu centymetrom odpowiada.

    echo "Podaj liczbe cali: "
    read cal

    echo "$cal cali to  $(bc -l <<< $cal/2.54) cm"	
    
        
	#Pobierz ilosc sekund i przelicz na godziny.

    echo "Podaj liczbe sekund: "
    read s

    echo "$s s to  $(($kg / 3600)) h"	
       
	#podaj miare kata w stopniach 

    echo "Podaj liczbe euro: "
    read stopnie
	rad=$(echo "$stopnie*0.0174532" | bc)

    echo "$stopnie stopni to $rad radianow"	
       
	#Pobierz temperature w stopniach Farenheita i wypisz ilu stopniom Celsjusza oraz ilu stopniom Kelwina odpowiada.

    echo "Podaj temperature w Farenheitach "
    read F
    
    C=$((($F - 32) * 5 / 9))
	K=$(($C - 273))

    echo "$F to Farenheitow to $C C i $K K"	
}

main "$@"

