#!/usr/bin/env bash

source ../assert.sh

# Dla otrzymanej listy znajdz indeks najmniejszego elementu.
# Lista jest posortowana rosnaco, ale zostala przesunieta.
# Przykladowo przez przesuniecie w prawo o 1 rozumiemy, ze
# ostatni element trafi na miejsce pierwszego, pierwszy drugiego, itd.

suma_dwoch() {
    local n=$((${#lista[@]}-1))

    for (( i=0; i<n; i++ )); do
        if [ ${lista[$i]} -gt ${lista[$i+1]} ]; then
            return $((i+1))
        fi
    done

    return 0
}

test1() {
    local lista=(7 8 -1 4 5)
    local wynik=2
    suma_dwoch
    assertEqual "$?" "$wynik" $LINENO
}

test2() {
    local lista=(2 3 4 5 6)
    local wynik=0
    suma_dwoch
    assertEqual "$?" "$wynik" $LINENO
}

test3() {
    local lista=(8 9 10 11 1)
    local wynik=4
    suma_dwoch
    assertEqual "$?" "$wynik" $LINENO
}

main() {
    test1
    test2
    test3
  }

main "$@"

