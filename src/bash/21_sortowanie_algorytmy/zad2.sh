# Tytul: Sortowanie przez wybieranie.
# Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania przez wybieranie. Znajdz najwiekszy element w liscie i zapisz go do zmiennej. Nastepnie znajdz najmniejszy element w pozostalej czesci listy i zamien go z pierwszym elementem nieposortowanej czesci. Powtarzaj operacje, az lista bedzie posortowana.
# Dane wejsciowe: Lista liczb calkowitych.
# Dane wyjsciowe: Posortowana lista liczb calkowitych.
# Przyklad:
# Dla listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

source ../assert.sh

sortuj(){
    local -n _tablica_ref=$1

    for (( i=0; i<${#_tablica_ref[@]}-1; i++ )); do
        min=$i
        for (( j=i+1; j<${#_tablica_ref[@]}; j++ )); do
            if [[ ${_tablica_ref[j]} -lt ${_tablica_ref[min]} ]]; then
                min=$j
            fi
        done
        if [[ $min -ne $i ]]; then
            local tmp=${_tablica_ref[i]}
            _tablica_ref[i]=${_tablica_ref[min]}
            _tablica_ref[min]=$tmp
        fi
    done
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

