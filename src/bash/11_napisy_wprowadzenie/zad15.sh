# ZAD-15 — Słowa jako lista
# 
# **Poziom:** ★☆☆
# **Tagi:** `split`, `list`
# 
# ### Treść
# 
# Wczytaj zdanie i wypisz listę słów w formacie `["Ala", "ma", "kota"]`.
# 
# ### Wejście
# 
# * 1. linia: zdanie
# 
# ### Wyjście
# 
# * 1. linia: lista słów (jak w przykładzie)
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# Ala ma kota
# ```
# 
# **Wyjście:**
# 
# ```
# ["Ala", "ma", "kota"]
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

    test1() {
        local napis="We think in generalities, but we live in details"
        local oczekiwane=('we' 'think' 'in' 'generalities' 'but' 'we' 'live' 'in' 'details')
        readarray -t wynik <<< "$(wypisz_slowa "$napis")"
        assertArrayEqual wynik oczekiwane $LINENO
    }

    test2() {
        local napis=""
        local wynik=""
        assertEqual "$(wypisz_slowa "$napis")" "$wynik" $LINENO
    }

    main() {
        test1
        test2
    }

    main "$@"

