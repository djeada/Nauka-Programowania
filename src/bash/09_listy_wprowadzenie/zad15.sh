# Tytul: Liczba mniejsza od najwiekszej i wieksza od wszystkich pozostalych.
# Tresc: Otrzymujesz liste liczb naturalnych. Znajdz najwieksza i druga co do wielkosci liczbe w liscie, a nastepnie oblicz srednia arytmetyczna tych dwoch liczb i zwroc ja jako liczbe zmiennoprzecinkowa.
# Dane wejsciowe: Lista liczb naturalnych.
# Dane wyjsciowe: Liczba zmiennoprzecinkowa oznaczajaca srednia arytmetyczna najwiekszej i drugiej co do wielkosci liczby z listy.
# Przyklad:
# Dla otrzymanej listy [9, 2, 3, 2, 1, 7] powinna zostac zwrocona liczba 8.0.

source ../assert.sh

element_dominujacy() {
    declare -A histo

    local n=${#lista[@]}

    for liczba in "${lista[@]}"; do
        if [[ -z  ${histo["$liczba"]} ]]; then
            histo["$liczba"]=1
        else
            histo["$liczba"]=$((${histo["$liczba"]} + 1))
        fi

    done

    for klucz in "${!histo[@]}"
    do
        if [ ${histo[$klucz]} -gt $((n/2)) ]; then
            unset histo
            echo "$klucz"
            return
        fi
    done

    unset histo
    echo "-1"
}

test1() {
    local lista=(4 7 4 4 2)
    local wynik=4
    assertEqual "$(element_dominujacy)" "$wynik" $LINENO
}

test2() {
    local lista=(1 2 4 5 6)
    local wynik=-1
    assertEqual "$(element_dominujacy)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"

