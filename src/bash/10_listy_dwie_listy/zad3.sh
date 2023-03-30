# Tytul: Mnozenie wektorowe.
# Tresc: Tresc: Otrzymujesz dwie listy liczb calkowitych reprezentujace dwa wektory trojwymiarowej przestrzeni euklidesowej. Zaimplementuj mnozenie wektorowe (zdefiniowane jedynie dla wektorow 3-wymiarowej przestrzeni euklidesowej).
# Dane wejsciowe: Dwie listy liczb calkowitych o dlugosci 3.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla otrzymanych list [1, 2, 3] oraz [3, 1, 2], powinno zostac zwrocone: 5.

source ../assert.sh

suma() {

    local n=$(( ${#lista_a[@]} ))
    local m=$(( ${#lista_b[@]} ))
    local min_dlugosc=$((n<m ? n : m))
    wynik=("${lista_a[@]}")

    for (( i=0; i<min_dlugosc; i++ ))
    do
        wynik[$i]=$((wynik[i] + lista_b[i]))
    done

    for (( i=min_dlugosc; i<m; i++ ))
    do
        wynik+=("{lista_b[$i]}")
    done

}

test1() {
    local lista_a=(3 1 2 5)
    local lista_b=(2 8 6 5)
    local oczekiwane=(5 9 8 10)
    suma
    assertArrayEqual oczekiwane wynik $LINENO
}

test2() {
    local lista_a=(3 1 2 5)
    local lista_b=(2 8)
    local oczekiwane=(5 9 2 5)
    suma
    assertArrayEqual oczekiwane wynik $LINENO
}

test3() {
    local lista_a=(3 1 0 0)
    local lista_b=(2 8 6 5)
    local oczekiwane=(5 9 6 5)
    suma
    assertArrayEqual oczekiwane wynik $LINENO
}

main() {
    test1
    test2
    test3
}

main "$@"

