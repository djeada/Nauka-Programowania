# ZAD-06A — Kilogramy → gramy
#
# **Poziom:** ★☆☆
# **Tagi:** `konwersje`
#
# ### Treść
#
# Wczytaj wartość w kilogramach `kg` i przelicz na gramy.
#
# ### Wejście
#
# * 1 linia: `kg`
#
# ### Wyjście
#
# * 1 linia: `g` jako **liczba całkowita**, gdzie:
#   `g = kg * 1000`
#
# ### Gwarancje
#
# * `kg` jest liczbą całkowitą **lub** taką, że wynik w gramach jest całkowity.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2.5
# ```
#
# **Wyjście:**
#
# ```
# 2500
# ```

main() {
    read kg
    result=$(echo "scale=0; $kg * 1000 / 1" | bc)
    echo "$result"
}

main "$@"
