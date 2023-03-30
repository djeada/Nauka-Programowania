# Tytul: Sortowanie szybkie.
# Tresc: Dla danej listy liczb calkowitych zaimplementuj algorytm sortowania szybkiego.
# 1. Jesli dlugosc listy jest mniejsza niz 2, zwroc liste.
# 2. Wybierz element rozdzielajacy, nazywany pivotem.
# 3. Podziel liste na trzy czesci: elementy mniejsze od pivota, pivot oraz elementy wieksze od pivota.
# 4. Wywolaj rekurencyjnie sortowanie szybkie dla czesci z elementami mniejszymi od pivota i wiekszymi od pivota.
# 5. Scal posortowane czesci listy w jedna posortowana liste.
# Dane wejsciowe: Lista liczb calkowitych.
# Dane wyjsciowe: Posortowana lista liczb calkowitych.
# Przyklad:
# Dla danej listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

partycja() {
    local i=$1
    local j=$2
    j=$((j-2))
    local klucz=${_tablica_ref[j+1]}

    while [ $i -le $j ]; do
        if [ ${_tablica_ref[i]} -le $klucz ]; then
            i=$((i+1))
        elif [ ${_tablica_ref[j]} -ge $klucz ]; then
            j=$((j-1))
        else
            local tmp=${_tablica_ref[i]}
            _tablica_ref[i]=${_tablica_ref[j]}
            _tablica_ref[j]=$tmp
            i=$((i+1))
            j=$((j-1))
        fi
    done
    j=$2
    j=$((j-1))

    local tmp=${_tablica_ref[i]}
    _tablica_ref[i]=${_tablica_ref[j]}
    _tablica_ref[j]=$tmp

    return $i
}

_sortuj() {
    local start=$1
    local stop=$2

    if [ $((stop-start)) -lt 2 ]; then
        return
    fi

    local i=$((start+RANDOM%(stop-start)))

    local tmp=${_tablica_ref[i]}
    _tablica_ref[i]=${_tablica_ref[stop-1]}
    _tablica_ref[stop-1]=$tmp
    partycja $start $stop
    i=$?

    _sortuj $start $i
    _sortuj $((i+1)) $stop
}

sortuj() {
    local -n _tablica_ref=$1
    _sortuj 0 ${#_tablica_ref[@]}
}

test_sortuj() {
    local tablica=(4 2 5 3 1)
    local oczekiwane=(1 2 3 4 5)
    sortuj tablica
    assertArrayEqual tablica oczekiwane $LINENO
}

main() {
    test_sortuj
}

main "$@"

