# Tytul: Czy punkty moga stanowic wierzcholki trojkata?
# Tresc: Otrzymujesz dokladnie 6 liczb calkowitych, ktore odpowiadaja wspolrzednym punktow A, B, C w kolejnosci: xA, yA, xB, yB, xC, yC. Sprawdz, czy punkty A, B, C moga stanowic wierzcholki trojkata.
# Dane wejsciowe: Lista liczb calkowitych reprezentujaca wspolrzedne punktow A, B, C.
# Dane wyjsciowe: Wartosc logiczna okreslajaca, czy punkty A, B, C moga stanowic wierzcholki trojkata.
# Przyklad:
# Dla otrzymanej listy [-3, -2, -3, 1, -3, 0], powinna zostac zwrocona wartosc logiczna: Falsz.

source ../assert.sh

suma_dwoch() {
    local n=$((${#lista[@]}-1))

    for (( i=0; i<n; i++ )); do
        if [ ${lista[$i]} -gt ${lista[$i+1]} ]; then
            return $((i+1))
        fi
    done

    return 0
}

test1() {
    local lista=(7 8 -1 4 5)
    local wynik=2
    suma_dwoch
    assertEqual "$?" "$wynik" $LINENO
}

test2() {
    local lista=(2 3 4 5 6)
    local wynik=0
    suma_dwoch
    assertEqual "$?" "$wynik" $LINENO
}

test3() {
    local lista=(8 9 10 11 1)
    local wynik=4
    suma_dwoch
    assertEqual "$?" "$wynik" $LINENO
}

main() {
    test1
    test2
    test3
}

main "$@"

