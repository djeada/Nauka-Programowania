# ZAD-02 — Połączenie dwóch list
#
# **Poziom:** ★☆☆
# **Tagi:** `list`, `indeksy`, `concat`
#
# ### Treść
#
# Wczytaj dwie listy liczb całkowitych i wykonaj niezależnie:
#
# **a)** Połącz listy, doklejając drugą listę na koniec pierwszej.
# **b)** W pierwszej liście **podmień** elementy o parzystych indeksach (0, 2, 4, …) elementami z drugiej listy o tych samych indeksach — o ile taki indeks istnieje w obu listach.
#
# ### Wejście
#
# * 1 linia: lista 1
# * 2 linia: lista 2
#
# ### Wyjście
#
# * 1 linia: wynik dla **a)** jako lista
# * 2 linia: wynik dla **b)** jako lista
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [1, 2, 3]
# [4, 5, 6]
# ```
#
# **Wyjście:**
#
# ```
# [1, 2, 3, 4, 5, 6]
# [4, 2, 6]
# ```
source ../assert.sh

dostaw() {
    wynik=("${lista_a[@]}" "${lista_b[@]}")
}

podmien() {
    local n=${#lista_a[@]}
    wynik=("${lista_a[@]}")

    for ((i = 0; i < n; i += 2)); do
        wynik[$i]=${lista_b[$i]}
    done
}

test1() {
    local lista_a=(-2 8 3 6)
    local lista_b=(7 5 0)
    local oczekiwane=(-2 8 3 6 7 5 0)
    dostaw
    assertArrayEqual oczekiwane wynik $LINENO
}

test2() {
    local lista_a=(-2 8 3 6)
    local lista_b=(7 5 0)
    local oczekiwane=(7 8 0 6)
    podmien
    assertArrayEqual oczekiwane wynik $LINENO
}

main() {
    test1
    test2
}

main "$@"
