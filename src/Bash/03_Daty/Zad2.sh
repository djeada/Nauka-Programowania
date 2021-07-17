#!/usr/bin/env bash

#Czy osoba jest pelnoletnia?

main() {
    
    echo "Podaj trzy liczby reprezentujace dzien, miesiac i rok urodzenia osoby:"
    read dzien
    read miesiac
    read rok

    echo "Podaj trzy liczby reprezentujace dzisiejsza date:"
    read dzienAktualny
    read miesiacAktualny
    read rokAktualny

    roznicaLata=$(($rokAktualny - $rok))
    roznicaMiesiace=$(($miesiacAktualny - $miesiac))
    roznicaDni=$(($dzienAktualny - $dzien))

    echo $roznicaLata

    if [[ $roznicaLata -gt 18 ]]; then
        echo "osoba jest pelnoletnia"
    
    elif [[ $roznicaLata -eq 18 ]]; then
        if [[ $roznicaMiesiace -gt 0 ]]; then
            echo "osoba jest pelnoletnia"
        elif [[ $roznicaMiesiace -eq 0 ]]; then
            if [[ $roznicaDni -ge 0 ]]; then
                echo "osoba jest pelnoletnia"
            else
                echo "osoba nie jest pelnoletnia"
            fi
        else
            echo "osoba nie jest pelnoletnia"
        fi
    else
        echo "osoba nie jest pelnoletnia"
    fi
}

main "$@"

