# ZAD-17 — Wszystkie pary o sumie x (wartości)
#
# **Poziom:** ★★☆
# **Tagi:** `listy`, `2-sum`, `pary`
#
# ### Treść
#
# Wczytaj listę liczb całkowitych oraz `x`. Wypisz wszystkie pary **wartości** `(a, b)` z listy (nie indeksy), takie że `a + b == x`. Każdą parę wypisz w osobnej linii jako:
# `a b`
#
# Każdą parę wypisz tylko raz (nie dubluj `(a,b)` i `(b,a)`).
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 2`)
# * kolejne `N` linii: liczby całkowite
# * ostatnia linia: `x` (liczba całkowita)
#
# ### Wyjście
#
# Wiele linii — po jednej parze na linię.
# Jeśli brak par — brak wyjścia.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# 1
# 2
# 4
# 3
# 7
# 5
# ```
#
# **Wyjście:**
#
# ```
# 1 4
# 2 3
# ```
source ../assert.sh

suma_dwoch() {
    local n=${#lista[@]}
    local liczba=$1

    for ((i = 0; i < n; i++)); do
        for ((j = i + 1; j < n; j++)); do
            if [ $((lista[i] + lista[j])) -eq $liczba ]; then
                echo "($i, $j)"
                return
            fi
        done
    done

    echo "(-1, -1)"
}

test1() {
    local lista=(1 3 4 5 2)
    local liczba=5
    local wynik="(0, 2)"
    assertEqual "$(suma_dwoch $liczba)" "$wynik" $LINENO
}

test2() {
    local lista=(2 -6 10 21 8)
    local liczba=7
    local wynik="(-1, -1)"
    assertEqual "$(suma_dwoch $liczba)" "$wynik" $LINENO
}

main() {
    test1
    test2
}

main "$@"
