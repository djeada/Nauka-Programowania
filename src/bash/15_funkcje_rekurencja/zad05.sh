# ZAD-05 — k-ta pochodna wielomianu
#
# **Poziom:** ★★☆
# **Tagi:** `pochodna`, `wielomiany`, `I/O`
#
# ### Treść
#
# Wczytaj wielomian stopnia `n` oraz liczbę `k`. Wypisz współczynniki wielomianu będącego `k`-tą pochodną.
#
# ### Wejście
#
# * 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
# * 2. linia: `n+1` liczb: `a_n ... a_0`
# * 3. linia: `k` — rząd pochodnej (`k ≥ 1`)
#
# ### Wyjście
#
# * Jeśli po zróżniczkowaniu `k` razy zostaje wielomian niezerowy: wypisz jego współczynniki w jednej linii (spacje).
# * Jeśli wielomian „znika” (stopień < k): wypisz dokładnie `[]`.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# 4 -3 2
# 1
# ```
#
# **Wyjście:**
#
# ```
# 8 -3
# ```
#
# ### Uwagi o formatowaniu
#
# * Pochodna: jeśli aktualne współczynniki to `[c_d, c_{d-1}, ..., c_0]`, to pochodna ma współczynniki:

# Funkcja do zaimplementowania
# Zlozonosc czasowa: O(n)
# Zlozonosc pamieciowa: O(n)
funkcja_glowna() {
    # TODO: Implementacja funkcjonalnosci opisanej w docstringu
    echo "Funkcjonalnosc wymaga pelnej implementacji"
}

main() {
    funkcja_glowna
}

main "$@"
