#!/usr/bin/env bash

source ../assert.sh

# Otrzymujesz tekst w postaci napisu. Znajdz wszystkie slowa, w ktorych te same 
# znaki wystepuja ta sama liczbe razy. Inaczej, znajdz wszystkie anagramy w 
# tekscie. Zignoruj roznice miedzy malymi i wielkimi literami. Pamietaj, slowa 
# skladaja sie wylacznie z liter.

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    for slowo in "${lista_slow[@]}"; do
        # sparawdz czy napis jest alfanumeryczny
        # i zawiera co najmniej jedna litere
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            echo "$slowo" | tr '[:upper:]' '[:lower:]'
        fi
    done

}

sortuj_napis() {
    # Funkcja sortuje alfabetycznie napis.
    local napis=$1
    echo "$napis" | tr -d ' ' | tr -d '\n' | tr -d '\t' | tr -d '\r' | grep -o . | sort | tr -d "\n"
}

czy_anagramy() {
    # Funkcja sprawdza czy dane napisy sa anagramami.
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

anagramy_w_tekscie() {
    local tekst="$1"
    local slowa=$(wypisz_slowa "$tekst")
    slowa=($(echo "$slowa" | tr ' ' '\n' | sort -u | tr '\n' ' '))
    local -A anagramy=()
    for slowo in "${slowa[@]}"; do
        for inne_slowo in "${slowa[@]}"; do
            if [ "$slowo" != "$inne_slowo" ]; then
                if $(czy_anagramy "$slowo" "$inne_slowo"); then
                    if [ -z "${anagramy[$inne_slowo]}" ]; then
                        anagramy["$slowo"]="${anagramy[$slowo]} $inne_slowo"
                    fi
                fi
            fi
        done
    done

    for slowo in "${!anagramy[@]}"; do
        echo "$slowo:${anagramy[$slowo]}"
    done
}

test_anagramy_w_tekscie() {
    local tekst="To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. Burza nad galeria i alergia na narty to zadna zbrodnia, jak bandzior i jego arbuz."
    local wynik=($(anagramy_w_tekscie "$tekst"))
    local oczekiwane=(
        "arbuz: burza"
        "narty: tyran"
        "bandzior: zbrodnia"
        "absurd: brudas"
        "alergia: galeria"
    )
    assertElementsEqual wynik oczekiwane $LINENO
}

main() {
    test_anagramy_w_tekscie
}


main "$@"

