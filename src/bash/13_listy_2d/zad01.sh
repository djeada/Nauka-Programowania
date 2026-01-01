# ZAD-01 — Macierz z identycznymi wierszami 0..b
#
# **Poziom:** ★☆☆
# **Tagi:** `macierze`, `pętle`, `print`
#
# ### Treść
#
# Wczytaj `a` i `b`. Wypisz macierz składającą się z `a` identycznych wierszy, gdzie każdy wiersz to liczby od `0` do `b` włącznie.
#
# ### Wejście
#
# * 1. linia: `a`
# * 2. linia: `b`
#
# ### Wyjście
#
# * `a` wierszy, w każdym: `0 1 2 ... b`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3
# 2
# ```
#
# **Wyjście:**
#
# ```
# 0 1 2
# 0 1 2
# 0 1 2
# ```

# Funkcja generujaca macierz z identycznymi wierszami 0..b
# Zlozonosc czasowa: O(a * b), gdzie a to liczba wierszy, b to liczba kolumn
# Zlozonosc pamieciowa: O(1)
generuj_macierz() {
    local a=$1
    local b=$2
    
    # Generowanie a wierszy
    for ((i = 0; i < a; i++)); do
        # W kazdym wierszu liczby od 0 do b
        for ((j = 0; j <= b; j++)); do
            if [ $j -eq $b ]; then
                echo -n "$j"
            else
                echo -n "$j "
            fi
        done
        echo ""
    done
}

main() {
    local a=3
    local b=2
    generuj_macierz $a $b
}

main "$@"
