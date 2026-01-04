# ZAD-02 — Macierz n×n: iloczyn indeksów
# 
# **Poziom:** ★☆☆
# **Tagi:** `macierze`, `pętle zagnieżdżone`
# 
# ### Treść
# 
# Wczytaj `n`. Utwórz i wypisz macierz `n×n`, gdzie element `[i][j]` (indeksy od 0) ma wartość `i*j`.
# 
# ### Wejście
# 
# * 1. linia: `n`
# 
# ### Wyjście
# 
# * `n` wierszy po `n` liczb
# 
# ### Przykład
# 
# **Wejście:**
# 
# ```
# 3
# ```
# 
# **Wyjście:**
# 
# ```
# 0 0 0
# 0 1 2
# 0 2 4
# ```
macierz_iloczyn() {
    local n=$1
    
    for ((i = 0; i < n; i++)); do
        for ((j = 0; j < n; j++)); do
            local wartość=$((i * j))
            if [ $j -eq $((n - 1)) ]; then
                echo -n "$wartość"
            else
                echo -n "$wartość "
            fi
        done
        echo ""
    done
}

main() {
    local n=3
    macierz_iloczyn $n
}

main "$@"
