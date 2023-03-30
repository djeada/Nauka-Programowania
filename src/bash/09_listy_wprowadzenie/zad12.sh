# Tytul: Minimum oraz maksimum.
# Tresc: Otrzymujesz liste liczb calkowitych. Znajdz najwiekszy i najmniejszy element tej listy i zwroc je jako dwie osobne liczby calkowite.
# Dane wejsciowe: Lista liczb calkowitych.
# Dane wyjsciowe: Dwie liczby calkowite oznaczajace najwiekszy i najmniejszy element z listy.
# Przyklad:
# Dla otrzymanej listy [4, -7, 8, 5, 6, -9, 10, 2, -8] powinny zostac zwrocone liczby 10 oraz -9.

source ../assert.sh

rotacja() {
    local kierunek=$1
    local liczba=$2
    local n=$(($(( ${#lista[@]})) -1))

    if [[ $kierunek == "prawo" ]]; then
        for (( i = 0; i < liczba; i++)); do
            lista=(${lista[$n]}  "${lista[@]}")
            lista=(${lista[$n]}  "${lista[@]}")
            lista=( "${lista[@]:0:n+1}")
        done
    else
        for (( i = 0; i < liczba; i++)); do
            lista=( "${lista[@]}" ${lista[0]} )
            lista=( "${lista[@]}" ${lista[0]} )
            lista=( "${lista[@]:1}")
        done
    fi

}

test1() {
    local lista=(5 27 6 2 1 10 8)
    local wynik=(6 2 1 10 8 5 27)
    local kierunek="lewo"
    local liczba=2
    rotacja $kierunek $liczba
    assertArrayEqual lista wynik $LINENO
}

test2() {
    local lista=(9 9 42 47 5 6 19 7)
    local wynik=(6 19 7 9 9 42 47 5)
    local kierunek="prawo"
    local liczba=3
    rotacja $kierunek $liczba
    assertArrayEqual lista wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"

