# ZAD-06C — Sekundy → pełne godziny
#
# **Poziom:** ★☆☆
# **Tagi:** `dzielenie całkowite`
#
# ### Treść
#
# Wczytaj liczbę sekund `s` i wypisz liczbę **pełnych godzin**.
#
# ### Wejście
#
# * 1 linia: `s` (liczba całkowita, `s ≥ 0`)
#
# ### Wyjście
#
# * 1 linia: `s // 3600`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 8639
# ```
#
# **Wyjście:**
#
# ```
# 2
# ```

main() {
    read s
    echo "$(($s / 3600))"
}

main "$@"
