# Tytul: Znalezienie anagramow slowa w zdaniu.
# Tresc: Napisz program, ktory otrzymuje napis reprezentujacy zdanie oraz slowo. Twoim zadaniem jest znalezienie wszystkich anagramow otrzymanego slowa w zdaniu. Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.
# Dane wejsciowe: Dwa napisy.
# Dane wyjsciowe: Lista napisow.
# Przyklad:
# Dla otrzymanych napisow: “Sroga kara.” oraz “arak”, powinna zostac zwrocona lista: [“kara”].

sortuj_napis() {
    local napis=$1
    local napis=$1
    echo "$napis" | tr -d ' ' | tr -d '\n' | tr -d '\t' | tr -d '\r' | grep -o . | sort | tr -d "\n"
}

czy_anagramy() {
    local napis_a="$1"
    local napis_a="$1"
    local napis_b="$2"

    if [ ${#napis_a} -ne ${#napis_b} ]; then
        echo false
        return
    fi

    local napis_a_sorted=$(sortuj_napis "$napis_a")
    local napis_b_sorted=$(sortuj_napis "$napis_b")

    if [ "$napis_a_sorted" == "$napis_b_sorted" ]; then
        echo true
    else
        echo false
    fi
}

wypisz_slowa() {
    local zdanie="$1"
    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                echo "$slowo" | tr '[:upper:]' '[:lower:]'
            fi
        done

    }

    anagramy_w_zdaniu() {
        local zdanie="$1"
        local zdanie="$1"
        local slowo="$2"
        local slowa=$(wypisz_slowa "$zdanie")
        for inne_slowo in $slowa; do
            if [ "$(czy_anagramy "$slowo" "$inne_slowo")" == "true" ]; then
                echo "$inne_slowo"
            fi
        done
    }

    test_anagramy_w_zdaniu() {
        local zdanie="Za jego nikczemne uczynki, spotakla go wysoce sroga kara."
        local slowo="arak"
        local wynik=$(anagramy_w_zdaniu "$zdanie" "$slowo")
        local oczekiwane=(kara)
        assertIdenticalElements wynik oczekiwane $LINENO
    }

    main() {
        test_anagramy_w_zdaniu
    }

    main "$@"

