# Tytul: Suma elementow dwoch list.
# Tresc: Dla otrzymanych dwoch list, zwroc liste, ktorej elementy sa suma odpowiadajacych sobie elementow obu list. Jesli listy nie sa tej samej dlugosci, zaloz, ze brakujace elementy krotszej listy sa rowne 0.
# Dane wejsciowe: Dwie listy.
# Dane wyjsciowe: Lista.
# Przyklad:
# Dla otrzymanych list [3, 1, 2, 5] oraz [2, 8, 6, 5], zostanie zwrocona lista: [5, 9, 8, 10].

source ../assert.sh

dostaw() {
    wynik=("${lista_a[@]}" "${lista_b[@]}")
}

podmien() {
    local n=${#lista_a[@]}
    wynik=("${lista_a[@]}")

    for (( i = 0; i < n; i+=2)); do
        wynik[$i]=${lista_b[$i]}
    done
}

test1() {
    local lista_a=(-2 8 3 6)
    local lista_b=(7 5 0)
    local oczekiwane=(-2 8 3 6 7 5 0)
    dostaw
    assertArrayEqual oczekiwane wynik $LINENO
}

test2() {
    local lista_a=(-2 8 3 6)
    local lista_b=(7 5 0)
    local oczekiwane=(7 8 0 6)
    podmien
    assertArrayEqual oczekiwane wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"

