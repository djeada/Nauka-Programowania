# ZAD-01 — Wypisanie elementów dwóch list na przemian
#
# **Poziom:** ★☆☆
# **Tagi:** `list`, `iteracja`
#
# ### Treść
#
# Wczytaj dwie listy liczb całkowitych i wypisz ich elementy **na przemian**:
# pierwszy z listy 1, pierwszy z listy 2, drugi z listy 1, drugi z listy 2, itd.
#
# Jeśli listy mają różne długości, po wyczerpaniu krótszej listy dopisz pozostałe elementy dłuższej listy w tej samej kolejności.
#
# ### Wejście
#
# * 1 linia: lista 1
# * 2 linia: lista 2
#
# ### Wyjście
#
# * 1 linia: elementy obu list wypisane na przemian, oddzielone przecinkami **bez spacji**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# [5, 3, 7, 2]
# [1, -2, 3]
# ```
#
# **Wyjście:**
#
# ```
# 5,1,3,-2,7,3,2
# ```

wypisz() {

    local n=$((${#lista_a[@]}))
    local m=$((${#lista_b[@]}))
    local min_dlugosc=$((n < m ? n : m))

    for ((i = 0; i < min_dlugosc; i++)); do
        echo -n "${lista_a[$i]}, "
        echo -n "${lista_b[$i]}, "
    done

    for ((i = min_dlugosc; i < n; i++)); do
        echo -n "${lista_a[$i]}, "
    done

    for ((i = min_dlugosc; i < m; i++)); do
        echo -n "${lista_b[$i]}, "
    done

    echo
}

main() {

    lista_a=(5 3 7 2)
    lista_b=(1 -2 3)

    wypisz

}

main "$@"
