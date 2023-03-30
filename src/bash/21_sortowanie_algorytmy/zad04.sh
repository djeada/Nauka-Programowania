# Tytul: Sortowanie przez scalanie.
# Tresc: Dla danej listy liczb calkowitych zaimplementuj algorytm sortowania przez scalanie.
# 1. Jesli dlugosc listy jest mniejsza niz 2, zwroc liste.
# 2. Podziel liste na dwie rowne (lub prawie rowne) czesci.
# 3. Wywolaj rekurencyjnie sortowanie przez scalanie dla obu czesci listy.
# 4. Scal obie posortowane czesci listy w jedna posortowana liste.
# Dane wejsciowe: Lista liczb calkowitych.
# Dane wyjsciowe: Posortowana lista liczb calkowitych.
# Przyklad:
# Dla danej listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

source ../assert.sh

scalaj() {
    local dane=("$@")
    local dane=("$@")
    local _tablica_a=( ${dane[@]:0:${#dane[@]}/2} )
    local _tablica_b=( ${dane[@]:${#dane[@]}/2} )
    local _tablica_c=()

    local i=0
    local j=0
    while [ $i -lt ${#_tablica_a[@]} ] && [ $j -lt ${#_tablica_b[@]} ]; do
        if [ ${_tablica_a[$i]} -lt ${_tablica_b[$j]} ]; then
            _tablica_c+=("${_tablica_a[$i]}")
            i=$((i+1))
        else
            _tablica_c+=("${_tablica_b[$j]}")
            j=$((j+1))
        fi
    done

    while [ $i -lt ${#_tablica_a[@]} ]; do
        _tablica_c+=("${_tablica_a[$i]}")
        i=$((i+1))
    done

    while [ $j -lt ${#_tablica_b[@]} ]; do
        _tablica_c+=("${_tablica_b[$j]}")
        j=$((j+1))
    done

    echo "${_tablica_c[@]}"
}

sortuj(){
    local _tablica_ref=("$@")
    local _tablica_ref=("$@")

    if [ ${#_tablica_ref[@]} -gt 1 ]; then
        local _lewo=( ${_tablica_ref[@]:0:${#_tablica_ref[@]}/2} )
        local _prawo=( ${_tablica_ref[@]:${#_tablica_ref[@]}/2} )

        echo "$(scalaj "$(sortuj "${_lewo[@]}")" "$(sortuj "${_prawo[@]}")")"
        return
    fi

    echo "${_tablica_ref[@]}"
}

test_sortuj() {
    local tablica=(4 2 5 3 1)
    local wynik=($(sortuj ${tablica[@]}))
    local oczekiwane=(1 2 3 4 5)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_sortuj
}

main "$@"

