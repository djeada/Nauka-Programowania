# Tytul: Roznica miedzy dwoma listami.
# Tresc: Dla otrzymanych dwoch list liczb calkowitych, znajdz elementy, ktore nie sa czescia wspolna obu list.
# Dane wejsciowe: Dwie listy liczb calkowitych.
# Dane wyjsciowe: Lista liczb calkowitych.
# Przyklad:
# Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] powinna zostac zwrocona lista: [9, 5, 1].

source ../assert.sh

czesc_wspolna_v1() {
    wynik=()
    for elem_a in "${lista_a[@]}"; do
        for elem_b in "${lista_b[@]}"; do
            if [ $elem_a -eq $elem_b ]; then
                wynik+=( "$elem_a" )
                break
            fi
        done
    done
}

czesc_wspolna_v2() {
    wynik=($(echo -n $(echo ${lista_a[@]} ${lista_b[@]} | sed 's/ /\n/g' | sort | uniq -d)))
}

test1() {
    local lista_a=(3 6 2 7 9)
    local lista_b=(4 2 3 5 6)
    local oczekiwane=(3 6 2)
    czesc_wspolna_v1
    assertSetsEqual wynik oczekiwane $LINENO
}

test2() {
    local lista_a=(3 6 2 7 9)
    local lista_b=(4 2 3 5 6)
    local oczekiwane=(3 6 2)
    czesc_wspolna_v2
    assertSetsEqual wynik oczekiwane $LINENO
}

main() {
    test1
    test2
}

main "$@"

