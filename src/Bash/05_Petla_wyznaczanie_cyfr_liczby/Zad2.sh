#!/usr/bin/env bash

#Dla pobranej od uzytkownika liczby, zwroc liczbe cyfr pobranje liczby.

main() {
    
    echo "Podaj liczbe: "    
    read a


    while [ $a -gt 0 ] 
    do
        echo $(($a % 10))
        a=$(( $a / 10 )) 
    done

}

main "$@"

