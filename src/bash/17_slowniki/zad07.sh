# ZAD-07 — Histogram słów w tekście (ignoruj wielkość liter)
# 
# **Poziom:** ★☆☆
# **Tagi:** `dict`, `string`, `tekst`
# 
# ### Treść
# 
# Wczytaj tekst. Policz częstość występowania słów (tylko litery), ignorując wielkość liter. Wypisz słownik: słowo (małe litery) → liczba wystąpień.
# 
# ### Wejście
# 
# * 1 linia: tekst
# 
# ### Wyjście
# 
# * Słownik
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# Ala ma kota. Ala lubi koty.
# ```
# 
# **Wyjście:**
# 
# ```
# {'ala': 2, 'ma': 1, 'kota': 1, 'lubi': 1, 'koty': 1}
# ```

source ../assert.sh

wypisz_slowa() {

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

    histogram_slow_w_tekscie() {
        local tekst="$1"
        local -A histogram=()
        for slowo in $(wypisz_slowa "$tekst"); do
            ((histogram["$slowo"]++))
        done
        for slowo in ${!histogram[@]}; do
            echo "$slowo: ${histogram[$slowo]};"
        done
    }

    test_histogram_slow_w_tekscie() {
        local tekst="Ala ma kota."
        local wynik=($(histogram_slow_w_tekscie "$tekst"))
        local oczekiwane=('ala: 1;' 'ma: 1;' 'kota: 1;')
        assertIdenticalElements wynik oczekiwane $LINENO
    }

    main() {
        test_histogram_slow_w_tekscie
    }

    main "$@"

