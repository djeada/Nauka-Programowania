# ZAD-09 — Kalkulator kredytowy (rata annuitetowa)
#
# **Poziom:** ★★☆
# **Tagi:** `finanse`, `float`, `formatowanie`
#
# ### Treść
#
# Wczytaj:
#
# * roczną stopę procentową `R` (w %),
# * okres spłaty `Y` (w latach),
# * kwotę kredytu `P`.
#
# Oblicz miesięczną ratę `M` oraz całkowity koszt `C = M * n`, gdzie `n = 12 * Y`.
#
# Dla `R > 0` użyj wzoru:
# [
# M = P \cdot \frac{r(1+r)^n}{(1+r)^n-1}
# ]
# gdzie `r = R / (12*100)`.
#
# Dla `R = 0` przyjmij:
#
# * `M = P / n`.
#
# ### Wejście
#
# 3 liczby (w osobnych liniach):
#
# 1. `R` (float, `R ≥ 0`)
# 2. `Y` (int, `Y > 0`)
# 3. `P` (float, `P > 0`)
#
# ### Wyjście
#
# Dwie linie (do **2 miejsc po przecinku**):
#
# 1. miesięczna rata `M`
# 2. całkowity koszt `C`
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 3.5
# 8
# 12000
# ```
#
# **Wyjście:**
#
# ```
# 143.50
# 13776.00
# ```
main() {
    read R
    read Y
    read P

    n=$((12 * $Y))

    # Check if R > 0
    is_zero=$(echo "$R == 0" | bc)
    
    if [ "$is_zero" -eq 1 ]; then
        # R = 0, simple division
        M=$(echo "scale=10; $P / $n" | bc)
    else
        # R > 0, use annuity formula
        r=$(echo "scale=10; $R / (12 * 100)" | bc)
        
        # Calculate (1+r)^n
        one_plus_r=$(echo "scale=10; 1 + $r" | bc)
        power=$(echo "scale=10; e($n * l($one_plus_r))" | bc -l)
        
        # M = P * r * power / (power - 1)
        numerator=$(echo "scale=10; $P * $r * $power" | bc)
        denominator=$(echo "scale=10; $power - 1" | bc)
        M=$(echo "scale=10; $numerator / $denominator" | bc)
    fi
    
    # Calculate total cost C = M * n
    C=$(echo "scale=10; $M * $n" | bc)
    
    # Output with 2 decimal places
    printf "%.2f\n" "$M"
    printf "%.2f\n" "$C"
}

main "$@"
