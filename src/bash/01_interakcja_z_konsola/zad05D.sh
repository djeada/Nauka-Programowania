# ZAD-05D — Wielomian z potęgami: y = a·x^m + b·x^n + c − a
#
# **Poziom:** ★★☆
# **Tagi:** `potęgi`, `float`
#
# ### Wejście
#
# 6 liczb (w osobnych liniach): `a`, `b`, `c`, `m`, `n`, `x`
#
# ### Wyjście
#
# `y` do 3 miejsc po przecinku.
#
# ### Ograniczenia / gwarancje
#
# * `m` i `n` są liczbami całkowitymi (np. nieujemnymi), aby potęgowanie było jednoznaczne w typowych językach.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 1
# 1
# 1
# 1
# 1
# 1
# ```
#
# **Wyjście:**
#
# ```
# 2.000
# ```

main() {
    read a
    read b
    read c
    read m
    read n
    read x
    result=$(echo "scale=3; $a * ($x^$m) + $b * ($x^$n) + $c - $a" | bc)
    printf "%.3f\n" "$result"
}

main "$@"
