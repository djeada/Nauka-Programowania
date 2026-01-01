# Tytul: Permutacje slowa, ktore sa palindromami.
# Tresc: Napisz program, ktory znajdzie permutacje danego slowa, ktore sa palindromami.
# Dane wejsciowe: Napis.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanego napisu: "taco", powinna zostac zwrocona lista: ["taco", "toca"].

source ../assert.sh

# Funkcja generujaca wszystkie permutacje napisu (rekurencyjnie)
# Zlozonosc czasowa: O(n!)
# Zlozonosc pamieciowa: O(n!)
permutacje() {
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

# Funkcja sprawdzajaca czy slowo jest palindromem
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
czy_palindrom() {
    local slowo="$1"
    local slowo_odwrocone=$(echo "$slowo" | rev)
    if [ "$slowo" == "$slowo_odwrocone" ]; then
        echo "true"
    else
        echo "false"
    fi
}

# Funkcja znajdujaca permutacje, ktore sa palindromami
# Zlozonosc czasowa: O(n! * n)
# Zlozonosc pamieciowa: O(n!)
permutacje_palindromy() {
    local napis="$1"
    local wszystkie_permutacje=$(permutacje "$napis")
    
    for permutacja in $wszystkie_permutacje; do
        if [ "$(czy_palindrom "$permutacja")" == "true" ]; then
            echo "$permutacja"
        fi
    done
}

test_permutacje_palindromy() {
    local wynik=($(permutacje_palindromy "taco"))
    local oczekiwane=(taco toca)
    assertArrayEqual wynik oczekiwane $LINENO
}

main() {
    test_permutacje_palindromy
}

main "$@"
