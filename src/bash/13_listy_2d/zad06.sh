# ZAD-06 — Scalanie przedziałów
#
# **Poziom:** ★★☆
# **Tagi:** `sortowanie`, `przedziały`, `algorytmy`
#
# ### Treść
#
# Wczytaj `n` przedziałów `[a_i, b_i]` (a_i ≤ b_i). Scal przedziały nachodzące na siebie i wypisz wynik w kolejności rosnącej po początku.
#
# ### Wejście
#
# * 1. linia: `n`
# * następnie `n` linii: `a_i b_i`
#
# ### Wyjście
#
# * Każdy scalony przedział w osobnej linii: `a b`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 7
# 23 67
# 23 53
# 45 88
# 77 88
# 10 22
# 11 12
# 42 45
# ```
#
# **Wyjście:**
#
# ```
# 10 22
# 23 88
# ```
#
# ### Uwagi
#
# * Przedziały uznajemy za nachodzące, gdy `next_start <= current_end`.
main() {
}

main "$@"
