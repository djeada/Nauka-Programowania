# ZAD-07 — Potęgowanie liczby π
#
# **Poziom:** ★☆☆
# **Tagi:** `math.pi`, `potęgi`, `formatowanie`
#
# ### Treść
#
# Wczytaj liczbę naturalną `n` (`n ≥ 0`), oblicz wartość ( \pi^n ) i wypisz wynik z dokładnością do **dwóch miejsc po przecinku**.
#
# ### Wejście
#
# Jedna liczba naturalna:
#
# * 1. linia: `n` (`n ≥ 0`)
#
# ### Wyjście
#
# Jedna liczba zmiennoprzecinkowa — ( \pi^n ) z dokładnością do dwóch miejsc po przecinku.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# ```
#
# **Wyjście:**
#
# ```
# 9.87
# ```
#
# ### Uwagi o formatowaniu
#
# * Dla `n = 0` wypisz `1.00`.
main() {
    read n

    if [[ $n -eq 0 ]]; then
        echo "1.00"
    else
        # Oblicz pi
        pi=$(echo "scale=10; 4*a(1)" | bc -l)

        # Oblicz pi^n
        wynik=$(echo "scale=10; $pi^$n" | bc -l)

        # Wypisz z dokładnością do 2 miejsc po przecinku
        printf "%.2f\n" "$wynik"
    fi
}

main "$@"
