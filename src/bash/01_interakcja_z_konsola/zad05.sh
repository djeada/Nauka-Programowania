# ZAD-05A — Funkcja liniowa: y = 3x + 10
#
# **Poziom:** ★★☆
# **Tagi:** `arytmetyka`, `float`, `formatowanie`
#
# ### Wejście
#
# 1 liczba: `x` (może być całkowita lub zmiennoprzecinkowa)
#
# ### Wyjście
#
# 1 liczba: `y` wypisana z dokładnością do **3 miejsc po przecinku**.
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
# 19.000
# ```
#
# ZAD-05B — Funkcja liniowa: y = ax + b
#
# **Poziom:** ★★☆
# **Tagi:** `arytmetyka`, `float`
#
# ### Wejście
#
# 3 liczby (każda w osobnej linii): `a`, `b`, `x`
#
# ### Wyjście
#
# `y` do 3 miejsc po przecinku.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 1
# 2
# 3
# ```
#
# **Wyjście:**
#
# ```
# 5.000
# ```
#
# ZAD-05C — Funkcja sześcienna: y = x³ + 2
#
# **Poziom:** ★★☆
# **Tagi:** `potęgi`, `float`
#
# ### Treść
#
# Oblicz: `y = x^3 + 22 - 20`, czyli równoważnie `y = x^3 + 2`.
#
# ### Wejście
#
# 1 liczba: `x`
#
# ### Wyjście
#
# `y` do 3 miejsc po przecinku.
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 5
# ```
#
# **Wyjście:**
#
# ```
# 127.000
# ```
#
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
#
# ZAD-05E — Funkcja z trygonometrią, wykładniczą i logarytmem
#
# **Poziom:** ★★★☆
# **Tagi:** `math`, `trygonometria`, `log`, `exp`, `float`
#
# ### Treść
#
# Dla `x` (w radianach) oblicz:
# [
# y=\sin^3(x)\cdot\cos^2(x)+e^{x^2}+\ln(x^3+2x^2-x-3)
# ]
#
# ### Wejście
#
# 1 liczba zmiennoprzecinkowa: `x` (w radianach)
#
# ### Wyjście
#
# `y` do 3 miejsc po przecinku.
#
# ### Ograniczenia / gwarancje
#
# * Dane testowe spełniają warunek dziedziny logarytmu:
#
#   * (x^3+2x^2-x-3 > 0)
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
# 57.179
# ```

main() {
    # ZAD-05A: y = 3x + 10
    read x
    result=$(echo "scale=3; 3 * $x + 10" | bc)
    printf "%.3f\n" "$result"

    # ZAD-05B: y = ax + b
    read a
    read b
    read x
    result=$(echo "scale=3; $a * $x + $b" | bc)
    printf "%.3f\n" "$result"

    # ZAD-05C: y = x^3 + 2
    read x
    result=$(echo "scale=3; $x^3 + 2" | bc)
    printf "%.3f\n" "$result"

    # ZAD-05D: y = a*x^m + b*x^n + c - a
    read a
    read b
    read c
    read m
    read n
    read x
    result=$(echo "scale=3; $a * ($x^$m) + $b * ($x^$n) + $c - $a" | bc)
    printf "%.3f\n" "$result"

    # ZAD-05E: y = sin^3(x)*cos^2(x) + e^(x^2) + ln(x^3 + 2x^2 - x - 3)
    read x
    result=$(echo "scale=10; s_x=s($x); c_x=c($x); sin3=s_x*s_x*s_x; cos2=c_x*c_x; exp_part=e($x*$x); ln_arg=$x^3 + 2*$x^2 - $x - 3; ln_part=l(ln_arg); sin3*cos2 + exp_part + ln_part" | bc -l)
    printf "%.3f\n" "$result"
}

main "$@"
