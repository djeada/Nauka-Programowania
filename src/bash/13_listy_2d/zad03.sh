# ZAD-03 — Macierz 2-kolumnowa z dwóch list
#
# **Poziom:** ★☆☆
# **Tagi:** `listy`, `macierze`
#
# ### Treść
#
# Wczytaj dwie listy. Jeśli mają tę samą długość, wypisz macierz 2-kolumnową: wiersz `i` to `(lista1[i], lista2[i])`.
# Jeśli długości są różne, wypisz: `Pusta macierz`
#
# ### Wejście
#
# * 1. linia: `n`
# * 2. linia: `m`
# * następnie `n` liczb (pierwsza lista)
# * następnie `m` liczb (druga lista)
#
# ### Wyjście
#
# * Jeśli `n = m`: `n` wierszy `x y`
# * Jeśli `n ≠ m`: jedna linia `Pusta macierz`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 3
# 3
# 5
# 2
# 2
# 8
# 1
# ```
#
# **Wyjście:**
#
# ```
# 3 2
# 5 8
# 2 1
# ```

# Funkcja tworzaca macierz z dwoch list
# Zlozonosc czasowa: O(n), gdzie n to dlugosc list
# Zlozonosc pamieciowa: O(n)
macierz_z_list() {
    local n=$1
    local m=$2
    shift 2
    
    # Wczytanie pierwszej listy
    local lista1=()
    for ((i = 0; i < n; i++)); do
        lista1+=("$1")
        shift
    done
    
    # Wczytanie drugiej listy
    local lista2=()
    for ((i = 0; i < m; i++)); do
        lista2+=("$1")
        shift
    done
    
    # Sprawdzenie dlugosci
    if [ $n -ne $m ]; then
        echo "Pusta macierz"
        return
    fi
    
    # Wypisanie macierzy
    for ((i = 0; i < n; i++)); do
        echo "${lista1[$i]} ${lista2[$i]}"
    done
}

main() {
    macierz_z_list 3 3 3 5 2 2 8 1
}

main "$@"
