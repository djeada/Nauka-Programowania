# ZAD-07A — Pole trójkąta
#
# **Poziom:** ★☆☆
# **Tagi:** `geometria`, `float`
#
# ### Treść
#
# Oblicz pole trójkąta ze wzoru:
# ( P = \frac{1}{2} a h )
#
# ### Wejście
#
# * 1 linia: `a`
# * 2 linia: `h`
#
# ### Wyjście
#
# * 1 linia: `P` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 6
# 4
# ```
#
# **Wyjście:**
#
# ```
# 12.000
# ```
#
# ZAD-07B — Pole prostokąta
#
# **Poziom:** ★☆☆
# **Tagi:** `geometria`, `float`
#
# ### Treść
#
# Oblicz pole prostokąta:
# ( P = ab )
#
# ### Wejście
#
# * 1 linia: `a`
# * 2 linia: `b`
#
# ### Wyjście
#
# * 1 linia: `P` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2.5
# 4
# ```
#
# **Wyjście:**
#
# ```
# 10.000
# ```
#
# ZAD-07C — Pole rombu
#
# **Poziom:** ★☆☆
# **Tagi:** `geometria`, `float`
#
# ### Treść
#
# Oblicz pole rombu z przekątnych:
# ( P = \frac{1}{2} d_1 d_2 )
#
# ### Wejście
#
# * 1 linia: `d1`
# * 2 linia: `d2`
#
# ### Wyjście
#
# * 1 linia: `P` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 10
# 6
# ```
#
# **Wyjście:**
#
# ```
# 30.000
# ```
#
# ZAD-07D — Objętość kuli
#
# **Poziom:** ★★☆
# **Tagi:** `geometria`, `pi`, `float`
#
# ### Treść
#
# Oblicz objętość kuli:
# ( V = \frac{4}{3}\pi r^3 )
#
# ### Wejście
#
# * 1 linia: `r`
#
# ### Wyjście
#
# * 1 linia: `V` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 1
# ```
#
# **Wyjście:**
#
# ```
# 4.189
# ```
#
# ZAD-07E — Objętość stożka
#
# **Poziom:** ★★☆
# **Tagi:** `geometria`, `pi`, `float`
#
# ### Treść
#
# Oblicz objętość stożka:
# ( V = \frac{1}{3}\pi r^2 h )
#
# ### Wejście
#
# * 1 linia: `r`
# * 2 linia: `h`
#
# ### Wyjście
#
# * 1 linia: `V` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# 3
# ```
#
# **Wyjście:**
#
# ```
# 12.566
# ```
#
# ZAD-07F — Objętość prostopadłościanu
#
# **Poziom:** ★☆☆
# **Tagi:** `geometria`, `float`
#
# ### Treść
#
# Oblicz objętość prostopadłościanu:
# ( V = abc )
#
# ### Wejście
#
# * 1 linia: `a`
# * 2 linia: `b`
# * 3 linia: `c`
#
# ### Wyjście
#
# * 1 linia: `V` do **3 miejsc po przecinku**
#
# ### Przykład
#
# **Wejście:**
#
# ```
# 2
# 3
# 4
# ```
#
# **Wyjście:**
#
# ```
# 24.000
# ```
main() {
    # ZAD-07A: Pole trójkąta P = 0.5 * a * h
    read a
    read h
    result=$(echo "scale=3; 0.5 * $a * $h" | bc)
    printf "%.3f\n" "$result"

    # ZAD-07B: Pole prostokąta P = a * b
    read a
    read b
    result=$(echo "scale=3; $a * $b" | bc)
    printf "%.3f\n" "$result"

    # ZAD-07C: Pole rombu P = 0.5 * d1 * d2
    read d1
    read d2
    result=$(echo "scale=3; 0.5 * $d1 * $d2" | bc)
    printf "%.3f\n" "$result"

    # ZAD-07D: Objętość kuli V = (4/3) * π * r^3
    read r
    # Użyj wbudowanej funkcji arctangent w bc do obliczenia pi: pi = 4 * atan(1)
    result=$(echo "scale=10; pi = 4 * a(1); (4.0/3.0) * pi * $r^3" | bc -l)
    printf "%.3f\n" "$result"

    # ZAD-07E: Objętość stożka V = (1/3) * π * r^2 * h
    read r
    read h
    # Użyj wbudowanej funkcji arctangent w bc do obliczenia pi: pi = 4 * atan(1)
    result=$(echo "scale=10; pi = 4 * a(1); (1.0/3.0) * pi * $r^2 * $h" | bc -l)
    printf "%.3f\n" "$result"

    # ZAD-07F: Objętość prostopadłościanu V = a * b * c
    read a
    read b
    read c
    result=$(echo "scale=3; $a * $b * $c" | bc)
    printf "%.3f\n" "$result"
}

main "$@"
