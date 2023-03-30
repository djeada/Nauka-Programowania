# Tytul: Haslo.
# Tresc: Napisz dwie funkcje:
# * Pierwsza funkcja powinna prosic uzytkownika o podanie nazwy uzytkownika i hasla, a nastepnie zwrocic te dane.
# * Druga funkcja powinna otrzymac dane od pierwszej funkcji i ponownie prosic uzytkownika o podanie nazwy uzytkownika i hasla. Prosba o podanie danych powinna byc umieszczona w petli. Warunkiem zakonczenia petli jest podanie przez uzytkownika danych identycznych z tymi przekazanymi przez pierwsza funkcje.
# Dane wejsciowe: dwie nazwy uzytkownika i hasla (napisy)
# Dane wyjsciowe: komunikat

inicjalizacjaDanych() {
    echo "podaj nazwe oraz haslo do zapamietania"
    read nazwaTemp
    read hasloTemp
    eval "$1=$nazwaTemp $2=$hasloTemp"
}

czyDanePoprawne() {

    staraNazwa=$1
    stareHaslo=$2

    nowaNazwa=""
    noweHaslo=""

    while [[ $nowaNazwa != $staraNazwa ]] || [[ $noweHaslo != $stareHaslo ]]
    do
        echo "Aby zalogowac sie do systemu: podaj nazwe oraz haslo"
        read nowaNazwa
        read noweHaslo
    done

    echo "Logowanie do systemu przebieglo pomyslnie"
}

main() {
    nazwa=""
    haslo=""
    inicjalizacjaDanych nazwa haslo
    czyDanePoprawne $nazwa $haslo
}

main "$@"

