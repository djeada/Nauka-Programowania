# ZAD-08 — Maksymalny zysk ze sprzedaży sznurka
#
# **Poziom:** ★★★
# **Tagi:** `dp`, `rod cutting`, `optymalizacja`
#
# ### Treść
#
# Masz sznurek o długości `n` i cennik: ceny kawałków długości od `1` do `n`. Możesz pociąć sznurek na kawałki o całkowitych długościach. Znajdź maksymalny zysk.
#
# ### Wejście
#
# * 1 linia: lista `prices` (długości 1..n)
# * 2 linia: `n` (liczba naturalna)
#
# ### Wyjście
#
# * 1 linia: maksymalny zysk (liczba całkowita)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [1, 5, 8, 9, 10, 17, 17, 20]
# 4
# ```
#
# **Wyjście:**
#
# ```
# 10
# ```

source ../assert.sh

# Oblicza maksymalny zysk z cięcia sznurka.
# Złożoność czasowa: O(n^2), gdzie n to długość sznurka
# Złożoność pamięciowa: O(n)
maksymalny_zysk_sznurek() {
    local -n _ceny_ref=$1
    local n=$2
    
    # dp[i] = maksymalny zysk dla sznurka długości i
    local dp=()
    dp[0]=0
    
    for ((i=1; i<=n; i++)); do
        local max_val=0
        for ((j=1; j<=i && j<=${#_ceny_ref[@]}; j++)); do
            local cena_idx=$((j-1))
            if [ $cena_idx -lt ${#_ceny_ref[@]} ]; then
                local val=$((${_ceny_ref[$cena_idx]} + ${dp[$((i-j))]}))
                [ $val -gt $max_val ] && max_val=$val
            fi
        done
        dp[$i]=$max_val
    done
    
    echo ${dp[$n]}
}

test_maksymalny_zysk_sznurek() {
    local ceny=(1 5 8 9 10 17 17 20)
    local wynik=$(maksymalny_zysk_sznurek ceny 4)
    assertEqual "$wynik" "10" $LINENO
}

main() {
    test_maksymalny_zysk_sznurek
}

main "$@"
