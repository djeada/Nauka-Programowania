# Tytul: Znalezienie elementu dominujacego w liscie liczb naturalnych.
# Tresc: Dla dostarczonej listy liczb naturalnych, znajdz element, ktory wystepuje w niej wiecej niz polowa jej dlugosci. Jesli taki element nie istnieje, zwroc -1.
# Dane wejsciowe: Lista liczb naturalnych.
# Dane wyjsciowe: Liczba naturalna.
# Przyklad:
# Dla otrzymanej listy: [4, 7, 4, 4, 2] zostanie zwrocona liczba: 4.

source ../assert.sh

srednia() {
    local suma=$(IFS=+; echo "$((${lista[*]}))")
    local n=${#lista[@]}
    echo $((suma/n))
}

czy_srednia_w_liscie() {

    local srednia_wartosc=$(srednia)
    for elem in "${lista[@]}"; do
        if [ $elem -eq $srednia_wartosc ]; then
            echo true
            return
        fi
    done

    echo false
}

test1() {
    local lista=(3 5 -7 4 9 -11 2)
    assertFalse "$(czy_srednia_w_liscie)" $LINENO
}

test2() {
    local lista=(1 2 3)
    assertTrue "$(czy_srednia_w_liscie)" $LINENO
}

main() {
    test1
    test2
}

main "$@"

