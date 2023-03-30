# Tytul: Znalezienie wszystkich permutacji slowa.
# Tresc: Napisz program, ktory dla otrzymanego napisu znajdzie jego wszystkie permutacje.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanego napisu: “abc”, powinna zostac zwrocona lista: [“abc”, “bac”, “cab”, “acb”, “bca”, “cba”].

source ../assert.sh

permutacje() {
    local napis=$1
    local napis=$1
    if [ ${#napis} -eq 1 ]; then
        echo "$napis"
        return
    fi

    local permutacje=()

    for ((i=0; i<${#napis}; i++)); do
        for permutacja in $(permutacje ${napis:0:$i}${napis:$((i+1)):${#napis}}); do
            local permutacja="${napis:$i:1}$permutacja"
            if [[ ! " ${permutacje[@]} " =~ " $permutacja " ]] && [ ${#permutacja} -eq ${#napis} ]; then
                permutacje+=("$permutacja")
            fi
        done
    done

    echo "${permutacje[@]}"
}

test_permutacje() {
    local wynik=($(permutacje "abc"))
    local oczekiwane=(abc acb bac bca cab cba)
    assertIdenticalElements oczekiwane wynik $LINENO
}

main() {
    test_permutacje
}

main "$@"

