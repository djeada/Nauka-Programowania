#!/usr/bin/env bash

#Dla pobranych trzech liczb, sprawdz czy reprezentuja one poprawna date.
#Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.

main() {

    echo "Podaj dzien, miesiac i rok: "
    read dzien
    read miesiac
    read rok

    if [[ $rok -ge 1 ]]; then
        if [ $miesiac -eq 1 ] || [ $miesiac -eq 3 ] || [ $miesiac -eq 5 ] || [ $miesiac -eq 7 ] || [ $miesiac -eq 8 ] || [ $miesiac -eq 10 ] || [ $miesiac -eq 12 ]; then
            if [ $dzien -ge 1 ] && [ $dzien -le 31 ]; then
                echo "Podana data jest poprawna"
            else
                echo "Podano niepoprawna date"
            fi
        elif [ $miesiac -eq 4 ] ||[ $miesiac -eq 6 ] || [ $miesiac -eq 9 ] || [ $miesiac -eq 11 ]; then
            if [ $dzien -ge 1 ] && [ $dzien -le 30 ]; then
                echo "Podana data jest poprawna"
            else
                echo "Podano niepoprawna date"
            fi
        elif [ $miesiac -eq 2 ]; then
            if [[ $(($rok % 4)) -eq 0 ]]; then
                if [[ $(($rok % 100)) -eq 0 ]]; then
                    if [ $(($rok % 400)) -eq 0 ] && [ $dzien -ge 1 ] && [ $dzien -le 29 ]; then
                        echo "Podana data jest poprawna"
                    elif [ $dzien -ge 1 ] && [ $dzien -le 28 ]; then
                        echo "Podana data jest poprawna"
                    else
                        echo "Podano niepoprawna date"
                    fi
                elif [ $dzien -ge 1 ] && [ $dzien -le 29 ]; then
                    echo "Podana data jest poprawna"
                else
                    echo "Podano niepoprawna date"
                fi
            elif [ $dzien -ge 1 ] && [ $dzien -le 28 ]; then
                echo "Podana data jest poprawna"
            else
                echo "Podano niepoprawna date"
            fi
        else
            echo "Podano niepoprawna date"
        fi
    fi
}

main "$@"

