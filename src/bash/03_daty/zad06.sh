# Tytul: Poprawnosc daty.
# Tresc: Napisz program, ktory dla pobranych trzech liczb naturalnych sprawdzi, czy reprezentuja one poprawna date. Pierwsza liczba jest dniem, druga miesiacem, trzecia rokiem.
# Podpowiedz: Wszystkie liczby nie moga byc mniejsze od 1. Druga liczba nie moze byc wieksza niz 12 itd.
# Dane wejsciowe: Trzy liczby naturalne.
# Dane wyjsciowe: Komunikat o poprawnosci lub niepoprawnosci daty.
# Przyklad:
# Dla pobranych liczb 2, 1 i 4, program powinien wypisac informacje o poprawnosci daty.

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

