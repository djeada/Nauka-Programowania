# Tytul: Polacz posortowane listy w posortowana liste.
# Tresc: Dla otrzymanych dwoch posortowanych list, polacz je w jedna posortowana liste.
# Dane wejsciowe: Dwie listy liczb calkowitych.
# Dane wyjsciowe: Lista liczb calkowitych.
# Przyklad:
# Dla otrzymanych list [2, 4, 7] oraz [3, 5, 9] powinna zostac zwrocona lista: [2, 3, 4, 7, 9].

source ../assert.sh

roznica_v1() {
    wynik=()
    for elem_a in "${lista_a[@]}"; do
        for elem_b in "${lista_b[@]}"; do
            local flag=0
            if [ $elem_a -eq $elem_b ]; then
                local flag=1
                break
            fi
        done
        if [ $flag -eq 0 ]; then
            wynik+=( "$elem_a" )
        fi
    done

    for elem_b in "${lista_b[@]}"; do
        for elem_a in "${lista_a[@]}"; do
            local flag=0
            if [ $elem_a -eq $elem_b ]; then
                local flag=1
                break
            fi
        done
        if [ $flag -eq 0 ]; then
            wynik+=( "$elem_b" )
        fi
    done

}

roznica_v2() {
    wynik=(
        $(echo ${lista_a[@]} ${lista_b[@]} | sed 's/ /\n/g' | sort | uniq -d | xargs echo ${lista_b[@]} | sed 's/ /\n/g' | sort | uniq -u)
        $(echo ${lista_a[@]} ${lista_b[@]} | sed 's/ /\n/g' | sort | uniq -d | xargs echo ${lista_a[@]} | sed 's/ /\n/g' | sort | uniq -u)
    )
}

test1() {
    local lista_a=(9 2 5 4)
    local lista_b=(4 2 1)
    local oczekiwane=(9 5 1)
    roznica_v1
    assertSetsEqual wynik oczekiwane $LINENO
}

test2() {
    local lista_a=(9 2 5 4)
    local lista_b=(4 2 1)
    local oczekiwane=(9 5 1)
    roznica_v2
    assertSetsEqual wynik oczekiwane $LINENO
}

main() {
    test1
    test2
}

main "$@"

