# Tytul: Permutacje slowa, ktore sa palindromami.
# Tresc: Napisz program, ktory znajdzie permutacje danego slowa, ktore sa palindromami.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanego napisu: “taco”, powinna zostac zwrocona lista: ["taco", "toca"].

source ../assert.sh

permutacje() {
    local napis=$1
    local napis=$1
    if [ ${#napis} -eq 1 ]; then
        echo "$napis"
        return
    fi

    local permutacje=()

    for ((i = 0; i < ${#napis}; i++)); do
        for permutacja in $(permutacje ${napis:0:$i}${napis:$((i + 1)):${#napis}}); do
            local permutacja="${napis:$i:1}$permutacja"
            if [[ ! " ${permutacje[@]} " =~ " $permutacja " ]] && [ ${#permutacja} -eq ${#napis} ]; then
                permutacje+=("$permutacja")
            fi
        done
    done

    echo "${permutacje[@]}"
}

czy_palindrom() {
    local slowo="$1"
    local slowo="$1"
    local slowo_odwrocone=$(echo "$slowo" | rev)
    if [ "$slowo" == "$slowo_odwrocone" ]; then
        echo "true"
    else
        echo "false"
    fi
}

permutacje_palindromiczne() {
    local napis=$1
    for permutacja in $(permutacje "$napis"); do
        if [ $(czy_palindrom "$permutacja") == "true" ]; then
            echo "$permutacja"
        fi
    done
}

test_permutacje_palindromiczne() {
    local wynik=($(permutacje_palindromiczne "adamm"))
    local oczekiwane=("madam" "amdma")
    assertIdenticalElements oczekiwane wynik $LINENO
}

main() {
    test_permutacje_palindromiczne
}

main "$@"
