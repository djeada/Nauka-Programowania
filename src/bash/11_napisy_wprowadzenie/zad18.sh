# ZAD-18 — Odwróć słowa w zdaniu
# 
# **Poziom:** ★★☆
# **Tagi:** `split`, `string`, `pętle`
# 
# ### Treść
# 
# Wczytaj zdanie i odwróć litery **w każdym słowie osobno**, zachowując kolejność słów.
# 
# ### Wejście
# 
# * 1. linia: zdanie
# 
# ### Wyjście
# 
# * 1. linia: zdanie z odwróconymi słowami
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
# alA am atok
# ```

source ../assert.sh

wypisz_slowa() {

    local zdanie="$1"

    zdanie=$(echo "$zdanie" | sed -r 's/[.,:;!?]+/ /g')

    read -ra lista_slow <<<"$zdanie"

    local wynik=""

    for slowo in "${lista_slow[@]}"; do
        if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
            if [[ "$slowo" =~ ^[[:alnum:]]*$ ]] && [[ ! "$slowo" =~ ^[[:digit:]]+$ ]]; then
                local wynik="$wynik$(echo "$slowo" | rev) "
            fi
        done

        if [ ${#wynik} -gt 0 ]; then
            echo "${wynik::-1}"
        else
            echo ""
        fi
    }

    test1() {
        local napis="Cameron Diaz"
        local wynik="noremaC zaiD"
        assertEqual "$(wypisz_slowa "$napis")" "$wynik" $LINENO
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

