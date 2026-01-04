# ZAD-09 — Najdłuższy wspólny podnapis
#
# **Poziom:** ★★★
# **Tagi:** `string`, `dp`, `substring`
#
# ### Treść
#
# Otrzymujesz dwa napisy. Znajdź **najdłuższy wspólny podnapis** (ciągły fragment), który występuje w obu napisach.
#
# ### Wejście
#
# * 1 linia: napis `A`
# * 2 linia: napis `B`
#
# ### Wyjście
#
# * 1 linia: najdłuższy wspólny podnapis
#   (jeśli jest kilka o tej samej długości — wybierz ten, który występuje **najwcześniej w A**; jeśli nadal remis, najwcześniej w B)
#
# ### Przykład
#
# **Wejście:**
#
# ```
# ijkabcdl
# xxxxabcd
# ```
#
# **Wyjście:**
#
# ```
# abcd
# ```
source ../assert.sh

# Znajduje najdłuższy wspólny podnapis.
# Złożoność czasowa: O(n*m*min(n,m)), gdzie n i m to długości napisów
# Złożoność pamięciowa: O(1)
najdluzszy_wspolny_podnapis() {
    local napis_a="$1"
    local napis_b="$2"
    local len_a=${#napis_a}
    local len_b=${#napis_b}

    local max_len=0
    local end_pos=0

    # DP approach: dp[i][j] = długość wspólnego podnapisu kończącego się na i w A i j w B
    for ((i = 0; i < len_a; i++)); do
        for ((j = 0; j < len_b; j++)); do
            if [ "${napis_a:$i:1}" = "${napis_b:$j:1}" ]; then
                # Zlicz długość wspólnego ciągu
                local len=1
                local k=1
                while [ $((i + k)) -lt $len_a ] && [ $((j + k)) -lt $len_b ] && [ "${napis_a:$((i + k)):1}" = "${napis_b:$((j + k)):1}" ]; do
                    ((len++))
                    ((k++))
                done

                if [ $len -gt $max_len ]; then
                    max_len=$len
                    end_pos=$i
                fi
            fi
        done
    done

    if [ $max_len -gt 0 ]; then
        echo "${napis_a:$end_pos:$max_len}"
    else
        echo ""
    fi
}

test_najdluzszy_wspolny_podnapis() {
    local wynik=$(najdluzszy_wspolny_podnapis "ijkabcdl" "xxxxabcd")
    assertEqual "$wynik" "abcd" $LINENO
}

main() {
    test_najdluzszy_wspolny_podnapis
}

main "$@"
