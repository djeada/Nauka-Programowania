# ZAD-04 — Dodawanie i odejmowanie macierzy
#
# **Poziom:** ★☆☆
# **Tagi:** `macierze`, `arytmetyka`
#
# ### Treść
#
# Wczytaj dwie macierze `n×m`.
# a) Wypisz ich sumę.
# b) Wypisz różnicę: (pierwsza − druga).
#
# ### Wejście
#
# * 1. linia: `n`
# * 2. linia: `m`
# * potem `n` wierszy pierwszej macierzy (po `m` liczb)
# * potem `n` wierszy drugiej macierzy (po `m` liczb)
#
# ### Wyjście
#
# Najpierw `n` wierszy sumy, potem `n` wierszy różnicy (bez dodatkowych napisów).
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# 2
# 1 2
# -2 0
# 5 -3
# 1 7
# ```
#
# **Wyjście:**
#
# ```
# 6 -1
# -1 7
# -4 5
# -3 -7
# ```
operacje_na_macierzach() {
    local n=$1
    local m=$2
    shift 2

    # Wczytanie pierwszej macierzy
    local macierz1=()
    for ((i = 0; i < n * m; i++)); do
        macierz1+=("$1")
        shift
    done

    # Wczytanie drugiej macierzy
    local macierz2=()
    for ((i = 0; i < n * m; i++)); do
        macierz2+=("$1")
        shift
    done

    # Dodawanie
    echo "Suma:"
    for ((i = 0; i < n; i++)); do
        for ((j = 0; j < m; j++)); do
            local idx=$((i * m + j))
            local suma=$((macierz1[$idx] + macierz2[$idx]))
            if [ $j -eq $((m - 1)) ]; then
                echo -n "$suma"
            else
                echo -n "$suma "
            fi
        done
        echo ""
    done

    # Odejmowanie
    echo "Roznica:"
    for ((i = 0; i < n; i++)); do
        for ((j = 0; j < m; j++)); do
            local idx=$((i * m + j))
            local roznica=$((macierz1[$idx] - macierz2[$idx]))
            if [ $j -eq $((m - 1)) ]; then
                echo -n "$roznica"
            else
                echo -n "$roznica "
            fi
        done
        echo ""
    done
}

main() {
    operacje_na_macierzach 2 2 1 2 3 4 5 6 7 8
}

main "$@"
