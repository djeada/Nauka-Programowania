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

    echo "Podaj liczbe:"
    read x
    pi=$(echo "scale=2; 4*a(1)" | bc -l)
    potega=$pi

    for ((i = 1; i <= $x; i++)); do
        potega=$(echo "scale=2; $potega * $pi" | bc)
    done

    echo "liczbe Pi podniesiona do potegi rownej pobranej liczbie, wynosi $potega"

}

main "$@"
