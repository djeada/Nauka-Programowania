# ZAD-09 — N pierwszych liczb pierwszych
#
# **Poziom:** ★★☆
# **Tagi:** `pętle`, `pierwszość`, `wydajność`
#
# ### Treść
#
# Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz pierwsze `N` liczb pierwszych w **jednej linii**, oddzielone pojedynczą spacją.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
#
# ### Wyjście
#
# Jedna linia: `N` liczb pierwszych oddzielonych spacjami.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# ```
#
# **Wyjście:**
#
# ```
# 2 3 5 7 11
# ```
#
# ### Uwagi o formatowaniu
#
# * Nie dodawaj spacji na końcu linii.
# * Do sprawdzania pierwszości wystarczy test dzielnikami do `⌊sqrt(x)⌋`.
main() {
    read n
    count=0
    num=2
    while [[ $count -lt $n ]]; do
        is_prime=1
        if [[ $num -gt 2 ]]; then
            for ((i = 2; i * i <= num; i++)); do
                if [[ $((num % i)) -eq 0 ]]; then
                    is_prime=0
                    break
                fi
            done
        fi
        if [[ $is_prime -eq 1 ]]; then
            if [[ $count -eq 0 ]]; then
                echo -n "$num"
            else
                echo -n " $num"
            fi
            count=$((count + 1))
        fi
        num=$((num + 1))
    done
    echo ""
}
main "$@"
