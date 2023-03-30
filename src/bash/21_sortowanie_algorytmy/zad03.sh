# Tytul: Sortowanie przez wstawianie.
# Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania przez wstawianie. Stworz nowa, pusta liste i dodaj do niej pierwszy element listy wejsciowej. Dla kazdego kolejnego elementu znajdz odpowiednie miejsce w posortowanej juz czesci listy i wstaw go tam.
# Dane wejsciowe: Lista liczb calkowitych.
# Dane wyjsciowe: Posortowana lista liczb calkowitych.
# Przyklad:
# Dla listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

source ../assert.sh

sortuj(){
    local -n _tablica_ref=$1

    for (( i=1; i<${#_tablica_ref[@]}; i++ )); do
        local tmp=${_tablica_ref[$i]}
        local j=$((i-1))
        while (( j>=0 && _tablica_ref[j]>tmp )); do
            _tablica_ref[$((j+1))]=${_tablica_ref[$j]}
            ((j--))
        done
        _tablica_ref[$((j+1))]=$tmp
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

