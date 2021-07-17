#!/usr/bin/env bash

main() {
        
    #Pobierz podstawe i wysokosc trojkata i wypisz pole. 

    echo "Podaj podstawe i wysokosc trojkata: "
    read a
    read h

    echo "Pole trojkata o podstawie $a i wysokosci $h jest rowne $(($a*$h/2))"
    
    #Pobierz dlogosci bokow prostokata i wypisz pole. 

    echo "Podaj dlugosci bokow prostokata: "
    read a
    read b

    echo "Pole prostokata o bokach $a i $b jest rowne $(($a*$b))"    
               
}

main "$@"

