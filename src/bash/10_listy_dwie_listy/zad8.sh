# Tytul: Usun z pierwszej listy czesc wspolna obu list.
# Tresc: Otrzymujesz dwie listy liczb calkowitych. Usun z pierwszej listy te elementy, ktore wystepuja rowniez w drugiej liscie.
# Dane wejsciowe: Dwie listy liczb calkowitych.
# Dane wyjsciowe: Lista liczb calkowitych.
# Przyklad:
# Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] powinna zostac zwrocona lista: [9, 5].

source ../assert.sh

polacz_v1() {
    wynik=()

    local n=${#lista_a[@]}
    local m=${#lista_b[@]}

    if [ $n -eq 0 ] || [ $m -eq 0 ]; then
        return
    fi

    local i=0
    local j=0

    while [ $i -lt $n ] && [ $j -lt $m ]
    do
        if [ ${lista_a[$i]} -lt ${lista_b[$j]} ]; then
            wynik+=("${lista_a[$i]}")
            i=$((i+1))
        else
            wynik+=("${lista_b[$j]}")
            j=$((j+1))
        fi
    done

    while [ $i -lt $n ]
    do
        wynik+=("${lista_a[$i]}")
        i=$((i+1))
    done

    while [ $j -lt $m ]
    do
        wynik+=("${lista_b[$j]}")
        j=$((j+1))
    done

}

test1() {
    local lista_a=(5 7 11)
    local lista_b=(1 3 8 14)
    local oczekiwane=(1 3 5 7 8 11 14)
    polacz_v1
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test1
}

main "$@"

