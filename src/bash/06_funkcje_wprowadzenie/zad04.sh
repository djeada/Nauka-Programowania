# ZAD-04A — Minimum z dwóch liczb
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `min`
#
# ### Treść
#
# Napisz funkcję `min_z_dwoch(a, b)`, która zwraca mniejszą z dwóch liczb naturalnych.
#
# ### Wejście
#
# Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)
#
# ### Wyjście
#
# Funkcja zwraca:
#
# * `min(a, b)`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(min_z_dwoch(3, 1))
# ```
#
# **Wyjście:**
#
# ```
# 1
# ```
#
# ZAD-04B — Maksimum z dwóch liczb
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `max`
#
# ### Treść
#
# Napisz funkcję `max_z_dwoch(a, b)`, która zwraca większą z dwóch liczb naturalnych.
#
# ### Wejście
#
# Dwa argumenty: `a`, `b` (`a ≥ 0`, `b ≥ 0`)
#
# ### Wyjście
#
# Funkcja zwraca:
#
# * `max(a, b)`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(max_z_dwoch(3, 1))
# ```
#
# **Wyjście:**
#
# ```
# 3
# ```
#
# ZAD-04C — Minimum z trzech liczb
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `min`
#
# ### Treść
#
# Napisz funkcję `min_z_trzech(a, b, c)`, która zwraca najmniejszą z trzech liczb naturalnych.
#
# ### Wejście
#
# Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)
#
# ### Wyjście
#
# Funkcja zwraca:
#
# * `min(a, b, c)`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(min_z_trzech(3, 2, 1))
# ```
#
# **Wyjście:**
#
# ```
# 1
# ```
#
# ZAD-04D — Maksimum z trzech liczb
#
# **Poziom:** ★☆☆
# **Tagi:** `funkcje`, `max`
#
# ### Treść
#
# Napisz funkcję `max_z_trzech(a, b, c)`, która zwraca największą z trzech liczb naturalnych.
#
# ### Wejście
#
# Trzy argumenty: `a`, `b`, `c` (`a ≥ 0`, `b ≥ 0`, `c ≥ 0`)
#
# ### Wyjście
#
# Funkcja zwraca:
#
# * `max(a, b, c)`
#
# ### Przykład
#
# **Wywołanie funkcji:**
#
# ```python
# print(max_z_trzech(3, 2, 1))
# ```
#
# **Wyjście:**
#
# ```
# 3
# ```

min2() {

    if [[ $1 -lt $2 ]]; then
        return $1
    else
        return $2
    fi
}

maks2() {

    if [[ $1 -gt $2 ]]; then
        return $1
    else
        return $2
    fi
}

min3() {
    if [[ $1 -le $2 && $1 -le $3 ]]; then
        return $1
    elif [[ $2 -le $1 && $2 -le $3 ]]; then
        return $2
    else
        return $3
    fi
}

maks3() {
    if [[ $1 -ge $2 && $1 -ge $3 ]]; then
        return $1
    elif [[ $2 -ge $1 && $2 -ge $3 ]]; then
        return $2
    else
        return $3
    fi
}

main() {
    read a
    read b

    min2 $a $b
    wynik=$?
    echo "mniejsza liczba to $wynik"

    maks2 $a $b
    wynik=$?
    echo "wieksza liczba to $wynik"

    read a
    read b
    read c

    min3 $a $b $c
    wynik=$?
    echo "najmniejsza liczba to $wynik"

    maks3 $a $b $c
    wynik=$?
    echo "najwieksza liczba to $wynik"

}

main "$@"
