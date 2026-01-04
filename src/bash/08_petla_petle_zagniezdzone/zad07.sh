# ZAD-07 — Choinka z N trójkątów
#
# **Poziom:** ★★☆
# **Tagi:** `pętle zagnieżdżone`, `generowanie`, `print`
#
# ### Treść
#
# Wczytaj liczbę naturalną `N` (`N ≥ 1`). Wypisz choinkę składającą się z `N` trójkątów ustawionych jeden pod drugim:
#
# * 1. trójkąt ma wysokość 1,
# * 2. trójkąt ma wysokość 2,
# * …
# * `N`-ty trójkąt ma wysokość `N`.
#
# Każdy trójkąt jest „rosnący” (jak w ZAD-02): w jego wierszu `i` wypisz `i` gwiazdek.
#
# ### Wejście
#
# * 1. linia: `N` (`N ≥ 1`)
#
# ### Wyjście
#
# Suma wysokości wszystkich trójkątów, czyli `1 + 2 + ... + N` linii.
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
# *
# *
# **
# *
# **
# ***
# ```
#
# ### Uwagi o formatowaniu
#
# * Nie dodawaj pustych linii między trójkątami.
main() {
    read n
    for ((size = 1; size <= n; size++)); do
        for ((i = 1; i <= size; i++)); do
            for ((j = 0; j < i; j++)); do
                echo -n "*"
            done
            echo ""
        done
    done
}
main "$@"
